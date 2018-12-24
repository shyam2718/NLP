from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from nltk import word_tokenize

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.events import AllSlotsReset

class ActionSlot1(Action):
    def name(self):
        return 'action_slots'
        
    def run(self, dispatcher, tracker, domain):

        text = (tracker.latest_message)['text']
        Input_tokens = word_tokenize(text)

        
        # ED = tracker.get_slot('electrical_device')
        # PLUM = tracker.get_slot('bath_utilities')
        # CARP = tracker.get_slot('object')

        #Bag of words:
        Electricity = ['ac']
        Plumbing = []
        Carpenting = []

        # Check
        if len (set(Input_tokens) & set(Electricity)) > 0:
            dispatcher.utter_message('Electrical problem')

        elif len (set(Input_tokens) & set(Plumbing)) > 0:
            dispatcher.utter_message('Plumbing problem')

        elif len (set(Input_tokens) & set(Carpenting)) > 0:
            dispatcher.utter_message('Carpenting problem')

        else:
            dispatcher.utter_message('Can you try something simpler')

        return []


class ActionSlot2(Action):
    def name(self):
        return 'action_slots2'

    def run(self, dispatcher, tracker, domain):

        # PER = tracker.get_slot('maid')
        text = (tracker.latest_message)['text']
        Input_tokens = word_tokenize(text)

        #Bag of words
        Maid = []
        Water_service = []

        # Check
        if len (set(Input_tokens) & set(Maid)) > 0:
            dispatcher.utter_message('Maid issues')

        if len (set(Input_tokens) & set(Water_service)) > 0:
            dispatcher.utter_message('Water service issues')


        return []


class ActionReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
       
        return[SlotSet(slot,None) for slot in tracker.slots]