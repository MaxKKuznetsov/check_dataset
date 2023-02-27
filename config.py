import os

PATH_TO_USERS_TABLE = os.environ.get('REGISTRED_FACES_DATA', '../faceid_datasets/terminals/users.csv')
PATH_TO_USERS_FOLDER = os.environ.get('PASS_HISTORY_DATA', '../faceid_datasets/terminals/users')
PATH_TO_HISTORY_TABLE = os.environ.get('PASS_HISTORY_DATA', '../faceid_datasets/terminals/pass_histories.csv')
PATH_HISTORY_FOLDER = os.environ.get('PASS_HISTORY_FOLDER', '../faceid_datasets/terminals/success')
OUTPUT_FILE = os.environ.get('OUTPUT_FILE', os.path.join(PATH_HISTORY_FOLDER + 'dataset.csv'))

IMG_SIZE = int(os.environ.get('IMG_SIZE', 300))
IMG_TYPE = str(os.environ.get('IMG_TYPE', '.jpg'))
