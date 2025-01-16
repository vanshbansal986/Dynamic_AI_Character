from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelDetails:
    gpt_model_name: str

@dataclass
class TweetGen:
    root_dir: Path
    system_prompt_file_path: Path
    output_tweets_file_path: Path
    audio_file_path : Path
    image_file_path : Path