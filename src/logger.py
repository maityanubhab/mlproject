import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,

)

"""for testing this code
if __name__=="__main__":
    logging.info("logging has started")"""

Theoritical concept
1 'import logging' - imports the logging module, 
    which provides functionality for logging messages
    in Python scripts.

2 'import os' - imports the os module, which provides 
    functions for interacting with the operating system.

3 'from datetime import datetime' - 
    imports the datetime class from the datetime module,
    which provides functions for working with dates and times.

4 'LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"` - 
    creates a string containing the current date and time in a specific 
    format, and sets it as the filename for the log file.

5 'logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)' - creates 
    a path to the log file by joining the current working directory, the `logs` 
    directory, and the `LOG_FILE` variable.

6 `os.makedirs(logs_path,exist_ok = True)` - creates the logs directory 
    if it doesn't exist already. The `exist_ok` parameter is set to `True` 
    to prevent errors if the directory already exists.

7 `LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)` - creates a 
    path to the log file by joining the `logs_path` and `LOG_FILE` variables.

8 `logging.basicConfig(filename= LOG_FILE_PATH,format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",level = logging.INFO)` - 
    configures the logging system to write log messages to the file specified by `LOG_FILE_PATH`. The `format` parameter specifies the format for the 
    log messages, and the `level` parameter sets the logging level to `INFO`.