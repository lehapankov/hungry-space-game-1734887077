import subprocess
import json
import sys

def run_game():
    try:
        print("Starting game as subprocess...")
        # Run the game as a subprocess
        result = subprocess.run(['python', 'main.py'], 
                              capture_output=True, 
                              text=True)
        
        print(f"Game process completed with return code: {result.returncode}")
        print(f"Game stdout: {result.stdout}")
        print(f"Game stderr: {result.stderr}")
        
        # Check if the game exited successfully (won)
        if result.returncode == 0:
            try:
                # Parse the JSON output
                stdout_lines = result.stdout.strip().split('\n')
                # Get the last line which should be our JSON
                json_line = stdout_lines[-1].strip()
                game_result = json.loads(json_line)
                print("\n=== SUBPROCESS OUTPUT ===")
                print("Game completed successfully!")
                print(f"Final Result: {game_result}")
                print("=======================")
                return True
            except json.JSONDecodeError as e:
                print(f"Error parsing game output: {e}")
                print(f"Raw output was: {json_line}")
                return False
            except IndexError as e:
                print(f"No output found: {e}")
                return False
        else:
            print("Game ended without winning")
            return False
            
    except Exception as e:
        print(f"Error running game: {e}")
        return False

if __name__ == "__main__":
    success = run_game()
    # Exit with appropriate code
    sys.exit(0 if success else 1)
