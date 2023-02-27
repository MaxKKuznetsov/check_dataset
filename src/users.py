import os

from src.data_extractor import DataExtractor


class Users(DataExtractor):
    def __init__(self, path_to_users_table, path_to_users_folder):
        super().__init__(path_to_users_table, path_to_users_folder)

    def get_data(self, user_id):
        try:
            user_row = self.df.loc[self.df['id'] == int(user_id)]
            face_img_path = os.path.join(self.path_to_img_folder, user_row['face_img_file'].values[0])

            frame_b64 = self.read_img(face_img_path)

            user = {'user_id': user_id,
                    'name': user_row['name'].values[0],
                    'face_img_path': face_img_path,
                    'created_at': user_row['created_at'].values[0],
                    'updated_at': user_row['updated_at'].values[0],
                    'face_img_b64': frame_b64
                    }

            return user

        except Exception as exc:
            print(exc)
            return None


