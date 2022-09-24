# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
from rasa_sdk.events import SlotSet

restaurant_dict = {
    "chinese": ['CR1', 'CR2', 'CR3', 'CR4'],
    "italian": ['IR1', 'IR2', 'IR3', 'IR4', 'IR5'],
    "english": ['ER1', 'ER2', 'ER3'],
    "american": ['AR1', 'AR2'],
    "japanese": ['JR1', 'JR2', 'JR3', 'JR4', 'JR5', 'JR6']
}

class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Ant]]:
        restaurant_type = tracker.get_latest_entity_values("restaurant_type")[0].lower()
        restaurant_names = restaurant_dict[restaurant_type]
        index = int(random.random() * len(restaurant_names))
        return [SlotSet("restaurant_name", restaurant_names[index])]

class ActionSetTimeSlot(Action):

    def name(self) -> Text:
        return "action_concat_reserve_time"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        weekday = tracker.get_latest_entity_values("weekday")[0]
        t = tracker.get_latest_entity_values("time")[0]
        ans = week + ' ' + t
        return [SlotSet("reserve_time", ans)]

