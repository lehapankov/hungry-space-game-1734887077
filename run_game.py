import subprocess
import json
import sys

def run_game():
    try:
        # Run the game as a subprocess
        result = subprocess.run(['python', 'main.py'], 
                              capture_output=True, 
                              text=True)
        
        # Check if the game exited successfully (won)
        if result.returncode == 0:
            try:
                # Parse the JSON output
                game_result = json.loads(result.stdout.strip())
                print("Game completed successfully!")
                print("Result:", game_result)
                return True
            except json.JSONDecodeError:
                print("Error parsing game output")
                return False
        else:
            print("Game ended without winning")
            return False
            
    except Exception as e:
        print(f"Error running game: {e}")
        return False

if __name__ == "__main__":
    run_game()
