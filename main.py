from src.pipeline.tweet_generation import TweetGenPipeline

STAGE_NAME = "Cover Letter Generation Stage"

if __name__ == '__main__':
    try:
        obj = TweetGenPipeline()
        obj.initiate()
    except Exception as e:
        raise e