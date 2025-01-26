import requests
import json

# Step 1: Get the token
token_url = "http://169.254.169.254/latest/api/token"
headers_for_token = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}

token_response = requests.put(token_url, headers=headers_for_token, timeout=1)
token = token_response.text  # Extract the token

# Step 2: Use the token to get metadata
metadata_url = "http://169.254.169.254/latest/meta-data"
headers_for_metadata = {"X-aws-ec2-metadata-token": token}

metadata_response = requests.get(metadata_url, headers=headers_for_metadata, timeout=1)
metadata = metadata_response.text  # Extract metadata content

metadata = json.loads(metadata)
print(metadata)

if __name__ == '__main__':
    
    print(metadata)
