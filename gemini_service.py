
import google.generativeai as genai
from PIL import Image

from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_story(images, language, theme):

     prompt = f"""
IMPORTANT: The user selected the language "{language}".

You MUST write the ENTIRE story ONLY in {language}.

Do NOT write in English unless the selected language is English.

If the selected language is:
- Tamil → Write only in Tamil script.
- Hindi → Write only in Devanagari script.
- German → Write only in German.
- French → Write only in French.

Theme: {theme}

Now observe ALL the uploaded images carefully and create ONE connected children's story.

Rules:
- Use all the images.
- Do not describe each image separately.
- Create one continuous magical adventure.
- Around 300–500 words.
- Suitable for children aged 5–12.
- Give interesting character names.
- Add a title.
- End with a positive moral.
"""

     response = model.generate_content(
        [prompt] + images
    )

     return response.text