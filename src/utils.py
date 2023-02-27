import os


def make_file_list(path_to_img_folder):
    # list of files in registration folder (one file for one user)
    list_of_img_extensions = ('.png', '.jpeg', '.jpg')

    img_file_list = []
    for root, dirs, files in os.walk(path_to_img_folder):
        for name in files:
            if name.endswith(list_of_img_extensions):
                img_file_list.append(name)

    return img_file_list


def make_path_list(path_to_img_folder):
    # list of files in registration folder (one file for one user)
    list_of_img_extensions = ('.png', '.jpeg', '.jpg')

    img_path_list = []
    for root, dirs, files in os.walk(path_to_img_folder):
        for name in files:
            if name.endswith(list_of_img_extensions) and not ('unsorted' in root):
                img_path_list.append(os.path.join(root, name))

    return img_path_list


