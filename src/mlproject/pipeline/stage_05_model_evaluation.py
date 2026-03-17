
from mlproject import logger 
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import     ModelEvaluation


STAGE_NAME = "Model Evaluation stage"

class Model_evaluation__pipeline:
    def __init__(self):
        pass 


    def main(self):
        config = ConfigurationManager()
        Model_evaluation_config=config.get_model_evaluation_config()
        model_eval=ModelEvaluation(Model_evaluation_config)
        logger.debug("evaluation---...................---🌸")
        model_eval.evaluate()























