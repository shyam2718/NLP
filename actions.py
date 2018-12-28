from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from nltk import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import nltk
from nltk.corpus import wordnet


from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.events import AllSlotsReset

class ActionSlot1(Action):

    def name(self):
        return 'action_slots'
        
    # def stem_ming(self,data):

    #     stemmer = nltk.PorterStemmer()
    #     new = [stemmer.stem(word) for word in data]
    #     Data = new + data
    #     return Data

    def condition_check(self,Input_tokens,text_check,Electricity_Control_room,Electricity_appl,Plumbing,Carpenting,Water_service,Maid,dispatcher):

        stat = 0
        # Check
        if len (set(Input_tokens) & set(Electricity_Control_room)) > 0 or len([word for word in Electricity_Control_room if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('I understand that you need electric power. Do you want to fix it?')
            stat = 1
        elif len (set(Input_tokens) & set(Electricity_appl)) > 0 or len([word for word in Electricity_appl if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('Problem with your electrical Appliances!! Are you looking for remedies?')
            stat = 1

        elif len (set(Input_tokens) & set(Plumbing)) > 0 or len([word for word in Plumbing if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('It can be solved by a plumber!! Report and solve this problem?')
            stat = 1

        elif len (set(Input_tokens) & set(Carpenting)) > 0 or len([word for word in Carpenting if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('It seems you have carpentery issues!! Need a help on it?')
            stat = 1

        elif len (set(Input_tokens) & set(Water_service)) > 0 or len([word for word in Water_service if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('I find water service issues with you! Looking for alternate solutions?')
            stat = 1

        elif len (set(Input_tokens) & set(Maid)) > 0 or len([word for word in Maid if text_check.find(word) > 0]) > 0:
            dispatcher.utter_message('Do you want raise a request for maid service')
            stat = 1

        else:
            # dispatcher.utter_message('Hey sorry !!! May be you can try something simpler or service is not provided')
            stat = 0

        return stat

    def search_dictionary(self,input_words):
        BoW = []
        for iwords in input_words:
            for syn in wordnet.synsets(iwords):
                for l in syn.lemmas():
                    BoW.append(l.name())

        return BoW

    def run(self, dispatcher, tracker, domain):

        # stemmer = nltk.PorterStemmer()
        text = (tracker.latest_message)['text']
        # text_check = text.replace(" ", "")       
        
        Input_tokens = word_tokenize(text)
        # Stemmed_Input_tokens = [stemmer.stem(word) for word in Input_tokens]

        filtered_sentence = [w for w in Input_tokens if not w in stop_words]
        text_check = ''.join(filtered_sentence)

        #Bag of words:
        Electricity_Control_room = ['power','powercut','powershutdown','powerfailure','poweroff','power closedown','poweroutage','powersupplyinterruption','powerblackout','powerobstruction','powerlayoff','powerstandstill','powerdiscontinuance']
        Electricity_appl = ['electric','electrician','ac','air','conditioner','microwave',' oven','washing', 'machine','dryer','refrigerator','heater','vacuum', 'cleaner','boiler','coffee', 'maker','electric', 'cooker','dish washer','ironbox','television','fan','gasfireplace','light','air', ' purifier','juicer','blender','purifier','cooler','geyser','ups','generator','genset']
        Plumbing = ['plumber','plumbing','tap','pipe','closet','valve','tank','sink','wash basin','faucet','shower','lavatory','plumbing','tub','rack','adaptor','drain','seat','urinal','plumber','pip fitter','pipefixer','joint']
        Carpenting = ['carpenter','carpentery','sofa','table','cot','daybed','chair','bench','couch','bench','door','window','desk','shelf','wardrobe','cabinet','rack','stand','sheath','gate','ventilator','frame','carpenter','cabinet maker','wood worker','craftsman','mason','woodman','latch','bolt','hinge','woodjoiner','artificer']
        Water_service = ['water','hard','dirty']   
        Maid = ['maid','housemaid','maidservant','nursemaid','cleaning',' lady','cleaningwoman','housekeeper','housecleaner','caretaker','servant','chambermaid','attendent','servingmaid','babysitter','cookmaid','cleaner','cook','cleaner']

        status = self.condition_check(Input_tokens,text_check,Electricity_Control_room,Electricity_appl,Plumbing,Carpenting,Water_service,Maid,dispatcher)

        if status == 1:
            Bagofwords = self.search_dictionary(filtered_sentence)
            C_status = self.condition_check(Bagofwords,text_check,Electricity_Control_room,Electricity_appl,Plumbing,Carpenting,Water_service,Maid,dispatcher)
            if C_status == 0:
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
        Maid = ['maid','housemaid','maidservant','nursemaid','cleaning',' lady','cleaningwoman','housekeeper','housecleaner','caretaker','servant','chambermaid','attendent','servingmaid','babysitter','cookmaid','cleaner']
        
        # Check
        if len (set(Input_tokens) & set(Maid)) > 0:
            dispatcher.utter_message('Do you want raise a request for maid service?')

        else:
            dispatcher.utter_message('Sorry !!! May be you can try something simpler or service is not provided')

        return []


class ActionReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
       
        return[SlotSet(slot,None) for slot in tracker.slots]