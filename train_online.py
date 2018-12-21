from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def run_gev1_online(interpreter,
                          domain_file="/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml",
                          training_data_file='/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")						  
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy(epochs = 500)],
                  interpreter=interpreter,
				  action_endpoint=action_endpoint)
    				  
    data = agent.load_data(training_data_file)			   
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    nlu_interpreter = RasaNLUInterpreter('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')
    run_gev1_online(nlu_interpreter)

