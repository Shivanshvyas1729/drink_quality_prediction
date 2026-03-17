import os 
from mlproject import logger 
from mlproject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config 
        
        
    def validate_all_columns(self)->bool:
        try:
            validation_status = True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns) 
            
            all_schema  = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status=False 
                    break 
                
            os.makedirs(os.path.dirname(self.config.STATUS_FILE), exist_ok=True)
            with open(self.config.STATUS_FILE,'w') as f:
                f.write(f"Validation status: {validation_status}")
                
                
            return validation_status 
        
        
        except Exception as e :
            raise e 
        
        
                    
                
                    
                    
                
            
            