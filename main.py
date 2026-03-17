from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import Model_trainer_trainer_pipeline
from mlproject.pipeline.stage_05_model_evaluation import Model_evaluation__pipeline


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data transformation stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e 





STAGE_NAME = "Model trainer stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    model_train = Model_trainer_trainer_pipeline()
    model_train.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e 



STAGE_NAME = "Model evaluation stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
    model_evaluation = Model_evaluation__pipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e 