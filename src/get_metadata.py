import requests
import json

metadata_url = 'http://169.254.169.254/latest/'


def expand_tree(url, arr):
    print("url")    
    print(url)
    print("")
    print("arr")
    print(arr)
    print("")
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        print("text")
        print(text)
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            print("list_of_values")    
            print(list_of_values)
            print("")
            output[item[:-1]] = expand_tree(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output


def get_metadata():
    initial = ["meta-data"]
    result = expand_tree(metadata_url, initial)
    print("result")
    print(result)
    print("")
    return result


def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_metadata_json())
