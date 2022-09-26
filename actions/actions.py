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

reverse_mapping = {
    'CR': 'chinese',
    'IR': 'italian',
    'ER': 'english',
    'AR': 'american',
    'JR': 'japanese'
}

class ActionSearchRestaurant(Action):

    def name(self):
        return "action_search_restaurant"
    
    def run(self, dispatcher, tracker, domain):
        restaurant_type = list(tracker.get_latest_entity_values("restaurant_type"))[0].lower()
        restaurant_names = restaurant_dict[restaurant_type]
        index = int(random.random() * len(restaurant_names))
        return [SlotSet("restaurant_name", restaurant_names[index])]

class ActionSetTimeSlot(Action):

    def name(self):
        return "action_concat_reserve_time"
    
    def run(self, dispatcher, tracker, domain):
        weekday = list(tracker.get_latest_entity_values("weekday"))[0]
        t = list(tracker.get_latest_entity_values("time"))[0]
        ans = weekday + ' ' + t
        return [SlotSet("reserve_time", ans)]

class ActionSearchOther(Action):

    def name(self):
        return "action_search_other"

    def run(self, dispatcher, tracker, domain):
        last_recommend = tracker.get_slot('restaurant_name')
        prefix = last_recommend[0:2]
        restaurant_type = reverse_mapping[prefix]
        restaurant_names = restaurant_dict[restaurant_type]
        length = len(restaurant_names)
        index = int(random.random() * length)
        while index >= length or restaurant_names[index] == last_recommend:
            index = int(random.random() * length)
        return [SlotSet("restaurant_name", restaurant_names[index])]

