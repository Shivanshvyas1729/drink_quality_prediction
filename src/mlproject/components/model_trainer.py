import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from mlproject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        
        # ============================
        # 1️⃣ Load Data
        # ============================
        
        X_train = pd.read_csv(self.config.X_train_path)
        
        y_train = pd.read_csv(self.config.y_train_path).values.ravel()
        

        # ============================
        # 2️⃣ Initialize Model with YAML Params
        # ============================
        
        rf = RandomForestClassifier(**self.config.params)

        # ============================
        # 3️⃣ Train Model
        # ============================
        
        rf.fit(X_train, y_train)

        # ============================
        # 5️⃣ Save Model
        # ============================
        
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(rf, model_path)

        print(f"\nModel saved at: {model_path}")

        