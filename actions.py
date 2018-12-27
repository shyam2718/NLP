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


        #Bag of words:
        Electricity_Control_room = ['power','powercut','powershutdown','powerfailure','poweroff','powerclosedown','poweroutage','powersupplyinterruption','powerblackout','powerobstruction','powerlayoff','powerstandstill','powerdiscontinuance']
        Electricity_appl = ['electric','electrician','ac','airconditioner','microwaveoven','washingmachine','clothesdryer','refrigerator','waterheater','vacuumcleaner','waterboiler','coffeemaker','electriccooker','dishwasher','ironbox','television','ceilingfan','gasfireplace','light','airpurifier','juicer','blender','waterpurifier','aircooler','geyser','ups','generator','genset']
        Plumbing = ['plumber','plumbing','tap','pipe','closet','valve','tank','sink','washbasin','faucet','shower','lavatory','plumbing','tub','rack','adaptor','drain','seat','urinal','plumber','pipefitter','pipefixer','joint']
        Carpenting = ['carpenter','carpentery','sofa','table','cot','daybed','chair','bench','couch','bench','door','window','desk','shelf','wardrobe','cabinet','rack','stand','sheath','gate','ventilator','frame','carpenter','cabinetmaker','woodworker','craftsman','mason','woodman','latch','bolt','hinge','woodjoiner','artificer']
        Water_service = ['water','hard','dirty']
        # Check
        if len (set(Input_tokens) & set(Electricity_Control_room)) > 0:
            dispatcher.utter_message('I understand that you need electric power. Can I raise the concern to control room?')

        elif len (set(Input_tokens) & set(Electricity_appl)) > 0:
            dispatcher.utter_message('Problem with your electrical Appliances!! Do you consult to control room or book outsiders')

        elif len (set(Input_tokens) & set(Plumbing)) > 0:
            dispatcher.utter_message('It can be solved by a plumber!! Do you want to consult control room or book outsiders for this service')

        elif len (set(Input_tokens) & set(Carpenting)) > 0:
            dispatcher.utter_message('It seems carpentery issues!!Do you want to consult control room or book outsiders for this service')

        elif len (set(Input_tokens) & set(Water_service)) > 0:
            dispatcher.utter_message('I find water service issues with you! Do you want to report it to control room')
        else:
            dispatcher.utter_message('Hey sorry !!! May be you can try something simpler or service is not provided')

        return []


class ActionSlot2(Action):
    def name(self):
        return 'action_slots2'

    def run(self, dispatcher, tracker, domain):

        # PER = tracker.get_slot('maid')
        text = (tracker.latest_message)['text']
        Input_tokens = word_tokenize(text)

        #Bag of words
        Maid = ['maid','housemaid','maidservant','nursemaid','cleaninglady','cleaningwoman','housekeeper','housecleaner','caretaker','servant','chambermaid','attendent','servingmaid','babysitter','cookmaid','cleaner']
        

        # Check
        if len (set(Input_tokens) & set(Maid)) > 0:
            dispatcher.utter_message('Do you want raise a request for maid service?')

        else:
            dispatcher.utter_message('Hey sorry !!! May be you can try something simpler or service is not provided')

        return []


class ActionReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
       
        return[SlotSet(slot,None) for slot in tracker.slots]