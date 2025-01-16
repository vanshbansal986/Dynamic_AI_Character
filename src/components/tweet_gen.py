from src.config.configuration import ConfigurationManager
from src.entity.config_entity import TweetGen , ModelDetails
from src.utils.common import read_file
import langchain
import os
from pathlib import Path
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import random
from openai import OpenAI
import json
from src.utils.common import extract_tweet_info , generate_image , generate_audio
import requests
from PIL import Image
from io import BytesIO
import IPython.display as display
from src import logger
from src.components.tweet_post import TweetUpload
from src.components.system_prompt_creation import SystemPrompt



load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
stability_api_key = os.getenv("STABILITY_API_KEY")

class TweetGeneration:
    def __init__(self , model_config:ModelDetails , tweet_config: TweetGen):
        self.model_config = model_config
        self.tweet_config = tweet_config


    def generate_image_stability(self,image_desc:str , img_path: Path):
        
        logger.info("Trying to Generate an image...")
        
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/sd3",
            headers={
                "authorization": f"Bearer {stability_api_key}",  # Replace with your actual API key
                "accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": f"{image_desc}",
                "output_format": "jpeg",
                "model" : "sd3-medium"
            },
        )

        # Check the response status
        if response.status_code == 200:
            logger.info("Image Generated Successfully!!!")
            # Display the image in Jupyter Notebook
            img = Image.open(BytesIO(response.content))
            img.save(img_path, format="PNG")

            logger.info(f"Image saved at path : {img_path}")
        else:
            # Raise an error if the request fails
            raise Exception(str(response.json()))
    
    
    def generate_tweet(self):

        model = ChatOpenAI(model="gpt-4o-mini")
        
        logger.info(f"Reading system prompt file at path: {self.tweet_config.system_prompt_file_path}")
        syst_prompt_obj = SystemPrompt()
        system_prompt = syst_prompt_obj.create_system_prompt()
        logger.info("System prompt read successfully!!!")

        
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            system_prompt,
            template_format="jinja2"
        )


        tweet_type = "my name is?"
        human_template = f"""
            {tweet_type}
        """

        human_message_prompt = HumanMessagePromptTemplate.from_template(
            human_template,
            template_format="jinja2"
        )

        chat_prompt = ChatPromptTemplate.from_messages([
            system_message_prompt,
            MessagesPlaceholder(variable_name="messages"),
        ])


        workflow = StateGraph(state_schema=MessagesState)


        def call_model(state: MessagesState):
            prompt = chat_prompt.invoke(state)
            response = model.invoke(prompt)
            
            return {"messages": response}


        workflow.add_edge(START, "model")
        workflow.add_node("model", call_model)

        memory = MemorySaver()
        app = workflow.compile(checkpointer=memory)

        config = {"configurable": {"thread_id": "abc345"}}

        for i in range(2):
            
            type_list = ["text" , "image+text" , "image" , "audio"]
            type_list = [ "image+text" , "image" ]
            query = random.choice(type_list)

            logger.info(f"Generating a {query} only tweet!!!")

            input_messages = [HumanMessage(query)]

            logger.info("Getting response from LLM...")
            output = app.invoke({"messages": input_messages}, config)
            logger.info("LLM Response generated successfully!!!")
            resp = output["messages"][-1].content

            
            
            image_desc , text , audio = extract_tweet_info(resp)
            logger.info("Response has been decoded from json successfully!!!")

            if(query == "audio" and audio is not None):
                print(f"audio_desc : {audio}")
                generate_audio(audio , self.tweet_config.audio_file_path)
                continue

            if(image_desc != None):
                self.generate_image_stability(image_desc , self.tweet_config.image_file_path)
                #generate_image(image_desc , self.tweet_config.image_file_path)
                print(f"image_desc: {image_desc} " + "\n")
            else:
                print("image_desc : None")
            
            print(f"text : {text}" "\n")
            
            obj = TweetUpload()
            obj.post_tweet(query, tweet_text= text , media_path = self.tweet_config.image_file_path) 
            
