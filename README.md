# Dynamic AI Character: Social Media Post Generator

## Project Overview
This project involves creating a dynamic AI character capable of simulating human-like behavior and generating diverse social media posts. The AI character can post random tweets on Twitter, ranging from text, images, videos, and audio to a combination of these. The project leverages state-of-the-art AI APIs and models to ensure high-quality and engaging content generation.

## Features
- **Dynamic Personality:** The AI character has a unique personality, preferences, and daily routines.
- **Multi-format Post Generation:** The character generates tweets in various formats:
  - Text
  - Images
  - Audio
  - Video
  - Combination of text with images or other media.
- **AI Model Integration:** The project integrates multiple AI models to generate diverse and creative content.
- **Twitter Integration:** Tweets are uploaded directly to Twitter with the generated content.

# Character Summary: Josh Taylor

Josh Taylor is a 25-year-old Data Scientist with a passion for fitness, travel, and innovation. Born and raised in Los Angeles, USA, Josh currently lives in Chiang Mai, Thailand, embracing a digital nomad lifestyle while working remotely for Rippling. With a bachelor's degree in Computer Science from Arizona State University, he has grown his career in tech, earning a significant salary while planning to launch a consulting agency.

Josh's life is shaped by his diverse experiences, including excelling in rugby, overcoming personal challenges like a DUI arrest, and dealing with ADHD and bipolar disorder. Despite these hurdles, he remains driven, disciplined, and empathetic. His adventurous spirit fuels his interests in mixed martial arts (MMA), cultural exploration, and fitness training. 

Known for his outgoing personality and emotional depth, Josh starts his days with a morning jog and rigorous MMA training before diving into his professional work. On weekends, he explores local cultures and enjoys socializing. Fluent in English and learning Thai and Portuguese, Josh's goal is to excel in his career, explore the world, and grow personally and professionally.  


## Showcase of AI Character's Twitter Account

You can explore the dynamic AI character's creativity and diversity in action by visiting its official Twitter account. 

Follow the AI character here: [AI Character's Twitter Profile](https://x.com/JoshTaylor45012))  

## Key Technologies and Models
1. **Text Generation:**
   - **Model:** `gpt-4o-mini` by OpenAI
   - **Purpose:** Generates text content for tweets, including captions, descriptions, and standalone text.

2. **Image Generation:**
   - **Models:**
     - `sd3` by Stability AI
     - `DALL-E 2` by OpenAI
   - **Purpose:** Creates visually appealing images based on the AI character's prompts.

3. **Audio Generation:**
   - **Model:** `ElevenLabs`
   - **Purpose:** Synthesizes high-quality audio for tweets with voice or sound components.

4. **Video Generation:**
   - **Model:** `Synthesia`
   - **Purpose:** Generates videos to complement the tweets.

## Workflow
1. **Tweet Type Selection:**
   - Randomly selects the type of tweet to generate: text-only, image, image with text, or audio.

2. **Content Generation:**
   - Text is generated using `gpt-4o-mini`.
   - Images are generated using Stability AI's `sd3` or OpenAI's `DALL-E 2`.
   - Audio is created using `ElevenLabs`.
   - Videos are produced with `Synthesia`.

3. **Post Creation:**
   - Content is formatted and prepared for uploading to Twitter.

4. **Twitter Upload:**
   - The generated content is posted on Twitter via the Twitter API.

## Code Explanation
### `TweetGeneration` Class
#### **Initialization**
```python
    def __init__(self , model_config:ModelDetails , tweet_config: TweetGen):
        self.model_config = model_config
        self.tweet_config = tweet_config
```
- Initializes the class with model configuration (`model_config`) and tweet generation configuration (`tweet_config`).


#### **Tweet Generation**
```python
    def generate_tweet(self):
        ...
```
- Uses `gpt-4o-mini` to generate text content.
- Randomly selects the type of tweet (text, image, etc.).
- Extracts and processes tweet components (image description, text, audio).
- Calls `generate_image_stability` for image generation if needed.
- Posts the tweet to Twitter using the `TweetUpload` class.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vanshbansal986/Dynamic_AI_Character
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API keys:
   - Stability AI (`sd3`): Add your API key in the code.
   - OpenAI (`gpt-4o-mini`, `DALL-E 2`): Add your API key in the code.
   - ElevenLabs: Add your API key in the code.
   - Synthesia: Add your API key in the code.
   - X - Add all your API Keys related to X(twitter) in the code.

4. Configure paths and settings in the configuration file.

## Usage
1. Run the script to start generating tweets:
   ```bash
   python main.py
   ```
2. Check the logs for process updates.
3. Generated tweets will be posted directly to Twitter.


## Future Enhancements
- Expand the character's personality traits and backstory.
- Introduce multi-language support for tweets.
- Add support for other social media platforms.
- Enhance video generation capabilities.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Enjoy exploring the creative possibilities of dynamic AI characters!**
