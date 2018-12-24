from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	trainer.persist(model_dir, fixed_model_name = 'GereV2')
	
def run_nlu():
	interpreter = Interpreter.load('/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu/default/GereV2')
	print(interpreter.parse(u"water is too hard"))
	
if __name__ == '__main__':

    model_path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/models/nlu'

    path = '/media/hticdeep/drive3/shyam/IDAI/RASA/Gere_version2/data/modified_data.json'
	
    train_nlu(path, 'config_spacy.yml', model_path)
	
    run_nlu()
