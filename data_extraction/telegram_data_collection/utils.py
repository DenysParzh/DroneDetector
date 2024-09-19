import os 
import json
import pandas as pd

def read_txt_file(path):
    with open(path) as f: data = f.readlines()

    return data
    
def load_json_data(json_path):
    data = []
    with open(json_path) as file:
        for line in file:
            data.append(json.loads(line))
    
    return data

def save_line_to_json(line, file):
    with open(file, 'a', encoding='utf-8') as json_file:
        json.dump(line, json_file)
        json_file.write('\n')

def save_line_txt_file(file_path, line):
    with open(file_path, 'a') as f:
        f.write("{}\n".format(line))

def load_data_frame(csv_path):
    return pd.read_csv(csv_path)

def delete_pictures_from_folder(folder_path, extensions=None):
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    if not os.path.isdir(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in extensions):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")