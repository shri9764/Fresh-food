import os
import logging
from datetime import datetime

# Date and Time
current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%H:%M:%S")

print(f"Today date = {current_time} ")

# Directory path code!!!
print("Directory Path!!!")

Directories_List = ['./templates', './Logs','./Sqlfiles','./Output','./static']

for directory in Directories_List:
    os.makedirs(directory,exist_ok=True)
    print(f"Created dir {directory}/")


# Log configuration code
log_dir = './Logs'
log_file = os.path.join(log_dir,'directory.txt')

if os.path.exists(log_dir):
    logging.basicConfig(filename=log_file,filemode='a',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%d-%M-%Y %H:%M:%S")

    logging.captureWarnings
    logging.error
    logging.critical('Error')
    logging.info
    print(f'Logs created successfully!!!! {current_date} {current_time}')
else:
    print(f'Error while creating Logs {current_date} {current_time}')

