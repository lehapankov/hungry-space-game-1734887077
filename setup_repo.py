import os
import requests
import subprocess
import time

def setup_github_repo():
    # GitHub API endpoint
    api_url = "https://api.github.com/user/repos"
    
    # Repository data with timestamp to make it unique
    timestamp = int(time.time())
    repo_name = f"hungry-space-game-{timestamp}"
    repo_data = {
        "name": repo_name,
        "description": "A Hungry Space game clone built with Python and Pygame featuring spaceship movement, collectibles, and scoring system",
        "private": False
    }
    
    # Headers with token
    headers = {
        "Authorization": f"token {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Create repository
    response = requests.post(api_url, json=repo_data, headers=headers)
    
    if response.status_code == 201:
        print("Repository created successfully!")
        return response.json()["html_url"]
    else:
        print(f"Failed to create repository: {response.status_code}")
        print(response.json())
        return None

def setup_git():
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "config", "--global", "user.email", "replit@example.com"],
        ["git", "config", "--global", "user.name", "Replit User"],
        ["git", "commit", "-m", "Initial commit: Basic game implementation"],
        ["git", "branch", "-M", "main"],
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
            print(f"Successfully executed: {' '.join(cmd)}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {' '.join(cmd)}: {e}")
            return False
    return True

def push_to_github(repo_url):
    if not repo_url:
        return False
    
    remote_url = repo_url.replace("https://", f"https://{os.environ['GITHUB_TOKEN']}@")
    
    try:
        # Remove existing remote if it exists
        subprocess.run(["git", "remote", "remove", "origin"], check=False)
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Successfully pushed to GitHub!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
        return False

if __name__ == "__main__":
    if setup_git():
        repo_url = setup_github_repo()
        if repo_url:
            if push_to_github(repo_url):
                print(f"\nRepository URL: {repo_url}")
import os
import requests
import subprocess
import time

def setup_github_repo():
    # GitHub API endpoint
    api_url = "https://api.github.com/user/repos"
    
    # Repository data with timestamp to make it unique
    timestamp = int(time.time())
    repo_name = f"hungry-space-game-{timestamp}"
    repo_data = {
        "name": repo_name,
        "description": "A Hungry Space game clone built with Python and Pygame featuring spaceship movement, collectibles, and scoring system",
        "private": False
    }
    
    # Headers with token
    headers = {
        "Authorization": f"token {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Create repository
    response = requests.post(api_url, json=repo_data, headers=headers)
    
    if response.status_code == 201:
        print("Repository created successfully!")
        return response.json()["html_url"]
    else:
        print(f"Failed to create repository: {response.status_code}")
        print(response.json())
        return None

def setup_git():
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "config", "--global", "user.email", "replit@example.com"],
        ["git", "config", "--global", "user.name", "Replit User"],
        ["git", "branch", "-M", "main"],
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
            print(f"Successfully executed: {' '.join(cmd)}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {' '.join(cmd)}: {e}")
            return False
            
    # Try to commit, but don't fail if there are no changes
    try:
        subprocess.run(["git", "commit", "-m", "Initial commit: Basic game implementation"], check=False)
    except Exception as e:
        print(f"Note: Commit step skipped: {e}")
    
    return True

def push_to_github(repo_url):
    if not repo_url:
        return False
    
    remote_url = repo_url.replace("https://", f"https://{os.environ['GITHUB_TOKEN']}@")
    
    try:
        # Remove existing remote if it exists
        subprocess.run(["git", "remote", "remove", "origin"], check=False)
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Successfully pushed to GitHub!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
        return False

if __name__ == "__main__":
    if setup_git():
        repo_url = setup_github_repo()
        if repo_url:
            if push_to_github(repo_url):
                print(f"\nRepository URL: {repo_url}")

