import json
import easygui
import os

def select_and_load_json(file_path=None):
    if file_path is None:
        file_path = easygui.fileopenbox("Select json dataset")
    with open(file_path, 'r') as f:
        return json.load(f)


def get_healthy_7():
    folder = '/home/yana/ECG_DATA'
    filename = '7_pacients_ideally_healthy_and_normal_axis.json'
    path = os.path.join(folder, filename)
    return select_and_load_json(path)

if __name__ == "__main__":
    print(get_healthy_7())

