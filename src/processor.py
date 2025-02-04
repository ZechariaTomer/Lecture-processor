"""
This module provides a TextProcessor class for
processing text using the Anthropic API.
The processed text follows specified formatting guidelines
 and is suitable for high-level writing styles.
The class reads environment variables, manages API requests,
 and processes text from files.
"""

import os
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

import src.promts


class TextProcessor:
    """Processes text using Anthropic API to generate Torah-style writing."""

    def __init__(self):
        """Initializes the TextProcessor with API key from environment variables."""
        load_dotenv()
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

        self.client = Anthropic(api_key=api_key)
        self.prompt = src.promts.TORA_LECTURE

    def process_text(self, text: str) -> str:
        """Processes a single text using the Anthropic API."""
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": f"{self.prompt}\n\nהטקסט:\n{text}"
                }]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error accessing API: {e}")
            print("Please check your API key in the .env file.")
            raise

    def process_file(self, input_file: Path, output_file: Path):
        """Processes the content of a text file and writes the result to another file."""
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        processed_text = self.process_text(text)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_text)
