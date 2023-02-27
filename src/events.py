import cv2
import os
import pandas as pd
import base64

from src.data_extractor import DataExtractor


class Events(DataExtractor):
    def __init__(self, path_to_history_table, path_to_history_folder):
        super().__init__(path_to_history_table, path_to_history_folder)

    def get_data(self, event_index):
        try:
            event_row = self.df.iloc[[event_index]]
            face_img_path = os.path.join(self.path_to_img_folder, event_row['debug_photo'].values[0])

            frame_b64 = self.read_img(face_img_path)

            event = {'event_index': event_index,
                     'event_id': event_row['id'].values[0],
                     'identified_user_id': event_row['user_id'].values[0],
                     'terminal': event_row['terminal'].values[0],
                     'pass_at': event_row['pass_at'].values[0],
                     'face_img_path': face_img_path,
                     'face_img_b64': frame_b64
                     }

            return event

        except Exception as exc:
            print(exc)
            return None
