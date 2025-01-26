import requests
import json  # Ensure the JSON module is imported

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
    metadata = metadata_response.text  # Extract metadata content
except requests.RequestException as e:
    print(f"Error fetching metadata: {e}")
    exit(1)

# Step 3: Handle metadata
print("Raw metadata response:")
print(metadata)

# If the metadata is JSON, parse it; otherwise, handle it as plain text
try:
    parsed_metadata = json.loads(metadata)
    print("Parsed Metadata:")
    print(parsed_metadata)
except json.JSONDecodeError:
    print("Metadata is not in JSON format. Displaying raw text:")
    print(metadata)

if __name__ == "__main__":
    print("Final Metadata Output:")
    print(metadata)
