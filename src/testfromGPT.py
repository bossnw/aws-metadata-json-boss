import requests
import json

# Step 1: Get the token
token_url = "http://169.254.169.254/latest/api/token"
headers_for_token = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}

try:
    token_response = requests.put(token_url, headers=headers_for_token, timeout=1)
    token_response.raise_for_status()
    token = token_response.text  # Extract the token
except requests.RequestException as e:
    print(f"Error fetching token: {e}")
    exit(1)

# Step 2: Use the token to get metadata
metadata_url = "http://169.254.169.254/latest/meta-data"
headers_for_metadata = {"X-aws-ec2-metadata-token": token}

try:
    metadata_response = requests.get(metadata_url, headers=headers_for_metadata, timeout=1)
    metadata_response.raise_for_status()
    metadata_paths = metadata_response.text.splitlines()  # Extract metadata paths as a list
except requests.RequestException as e:
    print(f"Error fetching metadata: {e}")
    exit(1)

# Step 3: Fetch metadata values and convert to JSON
metadata_dict = {}

for path in metadata_paths:
    try:
        full_url = f"{metadata_url}/{path.rstrip('/')}"  # Remove trailing slashes for fetching
        response = requests.get(full_url, headers=headers_for_metadata, timeout=1)
        response.raise_for_status()
        
        # Add the response to the dictionary
        metadata_dict[path] = response.text
    except requests.RequestException as e:
        metadata_dict[path] = f"Error fetching value: {e}"

# Convert dictionary to JSON and print
metadata_json = json.dumps(metadata_dict, indent=4)
print("Metadata in JSON format:")
print(metadata_json)

# Save to a file (optional)
with open("metadata.json", "w") as json_file:
    json_file.write(metadata_json)
