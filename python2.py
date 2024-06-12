import subprocess
import requests
import json
import os

def run_command(command):
    """ Run a shell command and return the result. """
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e.stderr}")
        raise
    except FileNotFoundError as e:
        print(f"Command not found: {command}. Error: {e}")
        raise

def stop_docker_container(container_name):
    print(f"Stopping Docker container '{container_name}'...")
    run_command(["docker", "stop", container_name])

def remove_docker_container(container_name):
    print(f"Removing Docker container '{container_name}'...")
    run_command(["docker", "rm", container_name])

def prune_docker_containers():
    print("Pruning Docker containers...")
    run_command(["docker", "container", "prune", "-f"])

def get_jwt_token(url, username, password):
    print("Getting JWT token...")
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "password": password})
    )
    response.raise_for_status()  # This will raise an error for bad status codes
    jwt_response = response.json()
    print("JWT Response:", jwt_response)
    return jwt_response.get("access_token")

def update_env_file(env_file_path, access_token):
    print("Updating .env file with the new access token...")
    with open(env_file_path, 'r') as file:
        lines = file.readlines()
    
    with open(env_file_path, 'w') as file:
        for line in lines:
            if line.startswith("ACCESS_TOKEN="):
                file.write(f"ACCESS_TOKEN={access_token}\n")
            else:
                file.write(line)

def build_docker_image(image_name):
    print(f"Building Docker image '{image_name}'...")
    run_command(["docker", "build", "-t", image_name, "."])

def run_docker_container(image_name, container_name, port_mapping):
    print(f"Running Docker container '{container_name}'...")
    run_command(["docker", "run", "-p", port_mapping, "--name", container_name, image_name])

def main():
    container_name = "cubejs-dc"
    image_name = "cubejs-dc"
    port_mapping = "1000:1000"
    env_file_path = ".env"
    token_url = "http://example.com/api/token"
    username = "your_username"
    password = "your_password"

    stop_docker_container(container_name)
    remove_docker_container(container_name)
    prune_docker_containers()
    
    access_token = get_jwt_token(token_url, username, password)
    print("Access Token:", access_token)

    update_env_file(env_file_path, access_token)
    build_docker_image(image_name)
    run_docker_container(image_name, container_name, port_mapping)

if __name__ == "__main__":
    # Debugging step to check if 'docker' is in PATH
    docker_path = shutil.which("docker")
    if docker_path:
        print(f"'docker' found at: {docker_path}")
    else:
        print("Error: 'docker' command not found in PATH. Please ensure Docker is installed and in PATH.")
    
    main()
