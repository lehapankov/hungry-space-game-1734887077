import subprocess
import json
import sys

def run_game():
    try:
        print("Starting game as subprocess...", flush=True)
        # Run the game as a subprocess
        print("\nWaiting for game to complete (play until you reach size 100)...", flush=True)
        result = subprocess.run(['python', 'main.py'], 
                              capture_output=True, 
                              text=True)
        
        print("\n=== Game Process Output ===", flush=True)
        print(f"Return code: {result.returncode}", flush=True)
        print("\nStandard output:", flush=True)
        print(result.stdout, flush=True)
        print("\nStandard error:", flush=True)
        print(result.stderr, flush=True)
        print("========================", flush=True)
        
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
