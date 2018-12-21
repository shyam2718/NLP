from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


if __name__ == '__main__':


        logging.basicConfig(level='INFO')

        training_data_file = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/stories.md'
        model_path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/dialogue'

        agent = Agent('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
        train_data = agent.load_data(training_data_file)
        agent.train(train_data,
                    augmentation_factor = 50,
                    # max_history = 3,
                    # epochs = 500,
                    # batch_size = 2,
                    validation_split = 0.1)			
        agent.persist(model_path)
