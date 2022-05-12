# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random


class ActionSuggestPlaces(Action):

    def name(self) -> Text:
        return "action_suggest_places"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        places = ["Merida", "Bilbao", "Salamanca", "Cuenca", "Ibiza", "Segovia", "Ronda", "Santiago de Compostela",
                  "Toledo", "Cordoba", "San Sebastian", "Valencia", "Seville", "Madrid", "Mallorca", "Barcelona",
                  "Granada", ]

        response = str(f"You can visit {str(random.choice(places))}")

        dispatcher.utter_message(text=response)

        return []
