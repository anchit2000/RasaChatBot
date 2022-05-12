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

        destination_value = tracker.get_slot("destination")

        if not destination_value:

            places = ["Merida", "Bilbao", "Salamanca", "Cuenca", "Ibiza", "Segovia", "Ronda", "Santiago de Compostela",
                      "Toledo", "Cordoba", "San Sebastian", "Valencia", "Seville", "Madrid", "Mallorca", "Barcelona",
                      "Granada", ]

            dispatcher.utter_message(text=f"You can visit {random.choice(places)}")

        else:
            dispatcher.utter_message(text=f"{destination_value} is a great place!")

        return []
