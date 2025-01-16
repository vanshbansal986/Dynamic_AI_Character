from src.components.tweet_gen import TweetGeneration
from src.config.configuration import ConfigurationManager

class TweetGenPipeline:
    def __init__(self):
        pass

    def initiate(self):
        try:
            config=ConfigurationManager()
            model_config = config.get_model_details_config()
            tweet_config = config.get_tweet_gen_config()

            tweet_gen = TweetGeneration(model_config=model_config , tweet_config= tweet_config)
            tweet_gen.generate_tweet()
            
        except Exception as e:
            raise e
        
    

