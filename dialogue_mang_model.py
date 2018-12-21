from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml',
					model_path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue',
					training_data_file = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/stories.md'):
					
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(max_history=3, epochs=1500, batch_size=10)])
	data = agent.load_data(training_data_file)	
	

	agent.train(data)
				
	agent.persist(model_path)
	return agent
	
def gev1(serve_forever=True):

	interpreter = RasaNLUInterpreter('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')
	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
	rasa_core.run.serve_application(agent ,channel='cmdline')
		
	return agent
	
if __name__ == '__main__':
	train_dialogue()
	gev1()
