import json

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data["movies"]
    finally:
        file.close()

def load_stopwords(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        stopwords = content.splitlines()
        return stopwords
    finally:
        file.close()