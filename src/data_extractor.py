import base64
import cv2
import pandas as pd

from abc import ABC, abstractmethod

from config import IMG_SIZE, IMG_TYPE


class DataExtractor(ABC):
    def __init__(self,  path_to_csv_table, path_to_img_folder):
        self.df = pd.read_csv(path_to_csv_table)
        self.path_to_img_folder = path_to_img_folder
        self.img_size = (IMG_SIZE, int(IMG_SIZE*1.2))
        self.img_type = IMG_TYPE

    @abstractmethod
    def get_data(self, id):
        pass

    def read_img(self, face_img_path):
        try:
            face_img = cv2.imread(face_img_path)
        except Exception as exc:
            print(exc)
            return None

        if not face_img.size:
            print('No image: %s' % face_img_path)
            return None

        face_img = cv2.resize(face_img, self.img_size)
        ret, frame_buff = cv2.imencode(self.img_type, face_img)  # could be png, update html as well
        frame_b64 = base64.b64encode(frame_buff).decode("utf-8")

        return frame_b64
