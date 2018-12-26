from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import logging

from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.utils import EndpointConfig

if __name__ == '__main__':

        logging.basicConfig(level='INFO')

        training_data_file = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/stories.md'
        model_path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue'
        domain_file="/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml"
        action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
        interpreter = RasaNLUInterpreter('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')
 
        # agent = Agent('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
        agent = Agent(domain_file,
                      policies=[MemoizationPolicy(), KerasPolicy(epochs = 50)],
                      interpreter=interpreter,
                      action_endpoint=action_endpoint)

        train_data = agent.load_data(training_data_file)
        agent.train(train_data,
                    augmentation_factor = 50,
                    # max_history = 3,
                    # epochs = 500,
                    # batch_size = 2,
                    validation_split = 0.1)			
        agent.persist(model_path)
        
        # action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
        # interpreter = RasaNLUInterpreter('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')
        agent = Agent.load('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
        
        print("Here we go...")
        while True:
                a = input()
                if a == 'stop':
                        break
                else:
                        responses = agent.handle_text(a)
                        for response in responses:
                                data = response["text"]
                        
                        print(data)

