import pandas as pd
from mlproject import logger
import joblib
from mlproject.entity.config_entity import ModelEvaluationConfig
from mlproject.utils.common import save_json


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)




class ModelEvaluation:
    
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    # ==========================================
    # 1️⃣ Separate Metrics Function
    # ==========================================
    def calculate_metrics(self, y_true, y_pred, y_prob):
        
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        roc_auc = roc_auc_score(y_true, y_prob)
        conf_matrix = confusion_matrix(y_true, y_pred)

        metrics = {
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1_score": round(f1, 4),
            "roc_auc": round(roc_auc, 4),
            "confusion_matrix": conf_matrix.tolist()
        }

        return metrics


    # ==========================================
    # 2️⃣ Main Evaluate Function
    # ==========================================
    def evaluate(self):

        # -----------------------------
        # Load Test Data
        # -----------------------------
        X_test = pd.read_csv(self.config.X_test_path)
        y_test = pd.read_csv(self.config.y_test_path).values.ravel()

        logger.info("Test data loaded successfully.")

        # -----------------------------
        # Load Model
        # -----------------------------
        model = joblib.load(self.config.model_path)

        logger.info("Trained model loaded successfully.")

        # -----------------------------
        # Prediction
        # -----------------------------
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]  # binary prob

        logger.info("Prediction completed.")

        # -----------------------------
        # Calculate Metrics (Separate FN)
        # -----------------------------
        metrics = self.calculate_metrics(y_test, y_pred, y_prob)

        print("\n📊 Binary Classification Metrics:\n")
        for key, value in metrics.items():
            print(f"{key}: {value}")

        print("\nClassification Report:\n")
        print(classification_report(y_test, y_pred))

        # -----------------------------
        # Save Metrics JSON
        # -----------------------------
        save_json(
            path=self.config.metric_file_name,
            data=metrics
        )

        logger.info("Metrics saved as JSON successfully.")

        return metrics