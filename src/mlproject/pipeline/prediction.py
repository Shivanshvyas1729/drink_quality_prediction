import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.scaler = joblib.load(Path("artifacts/data_transformation/scaler.pkl"))

        # Same skewed columns used in training
        self.skewed_cols = [
            'residual sugar',
            'chlorides',
            'free sulfur dioxide',
            'total sulfur dioxide',
            'sulphates'
        ]

    def predict(self, data: pd.DataFrame):

        # 1️⃣ Apply log transform
        data[self.skewed_cols] = np.log1p(data[self.skewed_cols])

        # 2️⃣ Scale using saved scaler
        data_scaled = self.scaler.transform(data)

        # 3️⃣ Predict
        prediction = self.model.predict(data_scaled)

        return prediction