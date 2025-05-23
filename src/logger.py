import logging
import os
from datetime import datetime

# Generate log file name with timestamp
log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")  
os.makedirs(log_path, exist_ok=True)  

log_file_path = os.path.join(log_path, log_file)


logging.basicConfig(
    filename=log_file_path,  
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Set the log level to INFO
)

