from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import logging

from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.utils import EndpointConfig

import pyrebase

if __name__ == '__main__':


    logging.basicConfig(level='INFO')

    training_data_file = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/stories.md'
    model_path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue'
    
    domain_file="/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml"
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    interpreter = RasaNLUInterpreter('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')

    agent = Agent('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
    agent = Agent(domain_file,
                    policies=[MemoizationPolicy(), KerasPolicy(epochs = 1000)],
                    interpreter=interpreter,
                    action_endpoint=action_endpoint)
                
    train_data = agent.load_data(training_data_file)
    agent.train(train_data,
                augmentation_factor = 50,
                # max_history = 3,
                # epochs = 500,
                # batch_size = 2,
                validation_split = 0.1)			
    
    # Save the model
    agent.persist(model_path)
    

    #Loading the model
    T_agent = Agent.load('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
    

    #Firebase Configuration

    config = {
    "apiKey": "AIzaSyBYBGUvb0vWScsmHxEukoR-WIDsLMaavuY",
    "authDomain": "hticmodule3.firebaseapp.com",
    "databaseURL": "https://hticmodule3.firebaseio.com",
    "storageBucket": "hticmodule3.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    #Authenticate
    auth = firebase.auth()
    db = firebase.database()


    def get_meth(data,T_agent):

        if data == None:
            print('Received None')
        else:
            data1 = data.split("$")
            data2 = data1[0]

            if data2 == 'actionrestart':
                #  db.child("ash").child("ashServer").set("System Restarting")
                print("...")
            
            else:
                responses = T_agent.handle_text(data2)
                for response in responses:
                    result = response["text"]
                
                # IF result is not set:
                db.child("ashServer").set(result)

        return

    #Streaming
    def stream_handler(message):
        # print(message["event"]) # put
        # print(message["path"]) 
        print(message["data"]) 
        current_data = message["data"]
        get_meth(current_data,T_agent)

    my_stream = db.child("ashClient").stream(stream_handler)
