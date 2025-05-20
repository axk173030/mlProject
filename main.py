
from src.components.data_ingestion import DataIngestion
from src.logger import logging

def main():
    try:
        logging.info("Starting the pipeline...")
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Pipeline completed successfully.")
    except Exception as e:
        logging.exception(f"Pipeline failed due to: {e}")

if __name__ == "__main__":
    main()