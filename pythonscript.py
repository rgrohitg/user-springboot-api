import subprocess
import requests
import json
import os

# Step 1: Stop the Docker container
print("Stopping Docker container...")
subprocess.run(["docker", "stop", "cubejs-dc"], check=True)

# Step 2: Remove the Docker container
print("Removing Docker container...")
subprocess.run(["docker", "rm", "cubejs-dc"], check=True)

# Step 3: Prune Docker containers
print("Pruning Docker containers...")
subprocess.run(["docker", "container", "prune", "-f"], check=True)

# Step 4: Execute curl command to get JWT token
print("Getting JWT token...")
response = requests.post(
    "http://example.com/api/token",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"username": "your_username", "password": "your_password"})
)
jwt_response = response.json()
print("JWT Response:", jwt_response)

# Step 5: Extract access_token from the response
access_token = jwt_response.get("access_token")
print("Access Token:", access_token)

# Step 6: Update the .env file with the new access token
print("Updating .env file with the new access token...")
env_file_path = ".env"

# Read the .env file
with open(env_file_path, 'r') as file:
    lines = file.readlines()

# Write back with the updated access token
with open(env_file_path, 'w') as file:
    for line in lines:
        if line.startswith("ACCESS_TOKEN="):
            file.write(f"ACCESS_TOKEN={access_token}\n")
        else:
            file.write(line)

# Step 7: Build the Docker image
print("Building Docker image...")
subprocess.run(["docker", "build", "-t", "cubejs-dc", "."], check=True)

# Step 8: Run the Docker container
print("Running Docker container...")
subprocess.run(["docker", "run", "-p", "1000:1000", "--name", "cubejs-dc", "cubejs-dc"], check=True)
