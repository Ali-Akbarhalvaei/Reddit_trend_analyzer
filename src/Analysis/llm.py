# src/Analysis/llm.py

import os
import json
import google.generativeai as genai
from typing import Dict, Union
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)


try:
    google_api_key = os.getenv("GOOGLE_API_KEY")
    print(google_api_key)
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")

    genai.configure(api_key=google_api_key)

    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

except Exception as e:
    print(f"Error configuring Google AI client: {e}")
    model = None

# The prompt is the same, as it's model-agnostic.
PROMPT_TEMPLATE = """
You are a social media strategist. Your task is to analyze a trend title and provide a structured analysis.
Analyze the following trend to determine its potential to go viral on Instagram.

Trend Title: "{title}"

Return your analysis ONLY in a valid JSON format with the following keys: "score", "explanation", "hashtags".
"""


def analyze_trend(title: str) -> Union[Dict, None]:
    """
    Analyzes a given trend title using Google Gemini and returns a structured analysis.
    """
    if not model:
        print("Google AI Model is not initialized. Cannot proceed with analysis.")
        return None

    prompt = PROMPT_TEMPLATE.format(title=title)

    try:
        # --- NEW: Call the Gemini API ---
        # We also enable JSON mode with GenerationConfig
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json"
            ),
        )

        # The response text is directly the JSON string.
        content = response.text

        # Safely parse the JSON string.
        result = json.loads(content)
        return result

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from LLM response.")
        print("LLM Output:", content)
        return None
    except Exception as e:
        print(f"An unexpected error occurred during API call: {e}")
        return None


if __name__ == "__main__":
    test_title = "The rise of quiet vacationing trend in the workplace"
    analysis = analyze_trend(test_title)

    print("----- LLM Analysis Test (using Google Gemini) -----")
    if analysis:
        print(json.dumps(analysis, indent=2))
    else:
        print("Analysis failed.")
    print("--------------------------------------------------")
