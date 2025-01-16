from src.constants import CONFIG_FILE_PATH
from src.entity.config_entity import ModelDetails , TweetGen
from src.utils.common import read_yaml , create_directories

class ConfigurationManager:
    def __init__(self , config_file_path = CONFIG_FILE_PATH):
        config = read_yaml(config_file_path)
        self.config = config

        create_directories([self.config.artifacts_root])

    def get_model_details_config(self) -> ModelDetails:
        config = self.config.model_info

        model_details_config = ModelDetails(
            gpt_model_name = config.gpt_model_name
        )

        return model_details_config
    
    def get_tweet_gen_config(self) -> TweetGen:

        config = self.config.tweet_gen

        create_directories([config.root_dir])

        tweet_gen_config = TweetGen(
            root_dir = config.root_dir,
            system_prompt_file_path = config.system_prompt_file_path,
            output_tweets_file_path = config.output_tweets_file_path,
            audio_file_path = config.audio_file_path,
            image_file_path = config.image_file_path
        )

        return tweet_gen_config