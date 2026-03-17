import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from mlproject import logger
from mlproject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):

        try:
            logger.info("Starting Data Transformation")

            # ===============================
            # 1️⃣ Load Data
            # ===============================
            logger.info("Loading dataset")
            df = pd.read_csv(self.config.data_path)
            logger.info(f"Dataset loaded with shape: {df.shape}")

            # Remove duplicates
            df.drop_duplicates(inplace=True)
            logger.info(f"Shape after removing duplicates: {df.shape}")

            # ===============================
            # 2️⃣ Create Binary Target
            # ===============================
            logger.info("Creating binary target column")
            df["quality_binary"] = (df["quality"] >= 6).astype(int)

            # ===============================
            # 3️⃣ Define Features & Target
            # ===============================
            X = df.drop(columns=["quality", "quality_binary"])
            y = df["quality_binary"]

            # ===============================
            # 4️⃣ Train-Test Split
            # ===============================
            logger.info("Splitting data into train and test")
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.30,
                random_state=42,
                stratify=y
            )

            logger.info(f"X_train shape: {X_train.shape}")
            logger.info(f"X_test shape: {X_test.shape}")

            # ===============================
            # 5️⃣ Log Transform Skewed Columns
            # ===============================
            logger.info("Applying log transformation to skewed columns")

            skewed_cols = [
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide',
                'sulphates'
            ]

            X_train[skewed_cols] = np.log1p(X_train[skewed_cols])
            X_test[skewed_cols] = np.log1p(X_test[skewed_cols])

            # ===============================
            # 6️⃣ Feature Scaling
            # ===============================
            logger.info("Applying Standard Scaling")

            scaler = StandardScaler()

            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Convert back to DataFrame
            X_train_scaled = pd.DataFrame(
                X_train_scaled,
                columns=X_train.columns
            )

            X_test_scaled = pd.DataFrame(
                X_test_scaled,
                columns=X_test.columns
            )

            y_train = pd.DataFrame(y_train, columns=["quality_binary"])
            y_test = pd.DataFrame(y_test, columns=["quality_binary"])

            # ===============================
            # 7️⃣ Save Artifacts as CSV
            # ===============================
            logger.info("Saving transformation artifacts as CSV")

            os.makedirs(self.config.root_dir, exist_ok=True)

            X_train_scaled.to_csv(self.config.X_train_path, index=False)
            X_test_scaled.to_csv(self.config.X_test_path, index=False)
            y_train.to_csv(self.config.y_train_path, index=False)
            y_test.to_csv(self.config.y_test_path, index=False)

            logger.info("Train-test CSV files saved successfully")

            # Save scaler
            joblib.dump(scaler, self.config.transformer_path)
            logger.info("Scaler saved successfully")

            logger.info("Data Transformation Completed Successfully")

            return (
                self.config.X_train_path,
                self.config.X_test_path,
                self.config.y_train_path,
                self.config.y_test_path
            )

        except Exception as e:
            logger.exception("Error occurred during Data Transformation")
            raise e