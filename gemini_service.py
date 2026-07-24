
import google.generativeai as genai
from PIL import Image

from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_story(images):

    prompt = """
You are an expert children's storyteller.

Carefully observe ALL the uploaded images.

Write ONE connected story using everything you see.

Rules:
- Use all the images.
- Do not describe each image separately.
- Create one continuous adventure.
- Around 300–500 words.
- Suitable for children aged 5–12.
- Use simple English.
- Give the characters interesting names.
- Make the story imaginative and magical.
- Add a title at the beginning.
- End with a positive moral.
"""

    response = model.generate_content(
        [prompt] + images
    )

    return response.text