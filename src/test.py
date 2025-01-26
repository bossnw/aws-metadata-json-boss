import requests
import json

def getinstancemetadata():
    """
    Queries the AWS instance metadata and returns it as a JSON-formatted string.

    Returns:
        str: JSON-formatted string of the instance metadata.
    """
    baseurl = "http://169.254.169.254/latest/meta-data/"
    metadata = fetch_metadata(base_url)
    return json.dumps(metadata, indent=4)

def fetchmetadata(url, metadata=None):
    print("fetchmetadata")
    if metadata is None:
        metadata = {}

    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        content = response.text.splitlines()

        for item in content:
            item_url = f"{url}{item}"
            if item.endswith("/"):
                metadata[item[:-1]] = {}
                fetch_metadata(item_url, metadata[item[:-1]])
            else:
                item_response = requests.get(item_url, timeout=1)
                item_response.raise_for_status()
                metadata[item] = item_response.text
    except requests.RequestException as e:
        print(f"Error fetching metadata: {e}")

    return metadata

if __name__ == "__main":
    metadata_json = get_instance_metadata()
    print(metadata_json)
