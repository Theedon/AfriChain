import os

from google.cloud import translate_v2 as translate
from langchain_core.tools import tool

os.environ["OPENWEATHERMAP_API_KEY"] = os.getenv("OPENWEATHERMAP_API_KEY")


@tool
def translate_text(target: str, text: str) -> dict:
    """
    Translates the given text to the specified target language using the Google Cloud Translate API.

    Args:
        target (str): The target language to translate the text to.
        text (str): The text to be translated.

    Returns:
        dict: A dictionary containing the translated text, the detected source language, and other relevant information.
    """
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return "translated texty"
