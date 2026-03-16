import logging
import os
import datetime

def setup_logger(name="STQA_Logger"):
    """
    Sets up a centralized logger that saves output to a file in the reports/logs directory.
    Returns the configured logger instance.
    """
    os.makedirs("reports/logs", exist_ok=True)
    
    # Create a unique log file per test run
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join("reports", "logs", f"test_execution_{timestamp}.log")
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger, log_file

# Initialize a global instance
log, current_log_file = setup_logger()
