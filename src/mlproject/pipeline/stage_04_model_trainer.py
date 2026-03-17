from mlproject import logger 
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import      ModelTrainer


STAGE_NAME = "Model trainer stage"

class Model_trainer_trainer_pipeline:
    def __init__(self):
        pass 


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)
        logger.debug("training...................🌸")
        model_trainer.train()
        














