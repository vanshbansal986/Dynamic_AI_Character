import os
import yaml
import subprocess
from src import logger
import json
import joblib
from openai import OpenAI
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import requests
from PIL import Image
from io import BytesIO
import IPython.display as display
import requests
from IPython.display import Audio, display
from elevenlabs import ElevenLabs, save , play
import elevenlabs



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
        


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def read_file(path: Path) -> str:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        with open(path, 'r') as file:
        # Read the content of the file
            str_data = file.read()
        
        logger.info("file read successfully")
        return str_data
    except Exception as e:
        raise e

import json

@ensure_annotations
def extract_tweet_info(resp:str):
   
    # Parse the string to a dictionary
    response_dict = json.loads(resp)

    # Extract the values
    image_desc = response_dict.get("image_desc")  # This will be None
    text = response_dict.get("text")  # This will contain the text
    audio = response_dict.get("audio")

    # Output the values
    return image_desc , text , audio


def generate_image(image_desc:str , img_path: Path):
        
    # Initialize OpenAI client
    client = OpenAI()

    # Generate image using DALL-E
    response = client.images.generate(
        model="dall-e-2",
        prompt = image_desc,
        size="512x512",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(f"Image URL: {image_url}")

    # Download the image from the URL
    image_response = requests.get(image_url)

    # Checking if the image was downloaded successfully
    if image_response.status_code == 200:
        # Load the image into PIL
        img = Image.open(BytesIO(image_response.content))
        # Save the image to a file
        img.save(img_path, format="PNG")  # You can change the filename and format
        
        print("Image saved as image.png")
    else:
        print(f"Failed to download the image. Status code: {image_response.status_code}")


def generate_audio(audio_desc:str , file_path: Path):
    # Initialize ElevenLabs client
    client = ElevenLabs(
        api_key="sk_612688b069a195e9bd2b7db838e2f53447916d44d2ed34ff",  # Replace with your actual API key
    )

    # Generate audio using text-to-speech
    response = client.text_to_speech.convert(
        voice_id="iP95p4xoKVk53GoZ742B",
        output_format="mp3_44100_128",
        text= audio_desc,
        model_id="eleven_multilingual_v2",
    )

    print("trying to save ****")
    elevenlabs.save(response, file_path)
    print("saved...")
