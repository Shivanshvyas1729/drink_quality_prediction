
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger 
from pathlib import Path



STAGE_NAME = "Data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 


    def main(self):
        
        try:
            with open(Path("artifacts\data_validation\status.txt")) as f:
                logger.debug("file loaded")
                status = f.read().split(" ")[-1]
                
                if status =="True":
                    
                    config = ConfigurationManager()
                    
                    data_transformation_config = config.get_data_transformation_config()
                    
                    data_transformation = DataTransformation(config=data_transformation_config)
                    
                    X_train_path, X_test_path, y_train_path, y_test_path = \
                        data_transformation.initiate_data_transformation()
                else:
                    raise Exception("=============== :your data schema is not valid :=========")
 
        except Exception as e:
            print(e)










  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
