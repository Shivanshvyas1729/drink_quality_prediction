from dataclasses import dataclass 
from pathlib import Path
from typing import Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path 
    source_URL: str 
    local_data_file: Path
    unzip_dir: Path 
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE : str 
    unzip_data_dir: Path 
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    transformer_path: Path
    X_train_path: Path
    X_test_path: Path
    y_train_path: Path
    y_test_path: Path






# no need of test data
@dataclass(frozen=True)
class ModelTrainerConfig:
    
    root_dir: Path
    
    X_train_path: Path
    
    
    y_train_path: Path
    
    
    model_name: str
    
    params: Dict
    
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    
    root_dir: Path
    
    X_test_path: Path
    y_test_path: Path
    
    model_path: Path
    
    params: Dict
    
    metric_file_name: Path   # ✅ ADD THIS
    
    target_column: str       # (optional if you use it)