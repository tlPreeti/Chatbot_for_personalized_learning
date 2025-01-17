from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import logging
logger = logging.getLogger(__name__)

def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    question = tracker.latest_message.get('text')
    logger.info(f"User question: {question}")  # Log the input for debugging
    answers = {
        "machine learning": "Machine learning is a subset of AI that focuses on creating systems that learn from data.",
        "python": "Python is a versatile programming language popular for web development, data science, and AI.",
        "ai": "AI, or Artificial Intelligence, enables machines to mimic human intelligence.",
        "deep learning": "Deep learning is a neural network-based approach to machine learning."
    }

    response = answers.get(question.lower(), "I don't have an answer for that. You can explore more on [Coursera](https://www.coursera.org).")
    dispatcher.utter_message(text=response)
    return []

