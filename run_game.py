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
        
        # Check if the game exited successfully (won)
        if result.returncode == 0:
            try:
                # Parse the JSON output - search for the line containing JSON
                json_line = None
                for line in result.stdout.strip().split('\n'):
                    if '{"result":' in line:
                        json_line = line.strip()
                        break
                
                if json_line:
                    game_result = json.loads(json_line)
                    print("\n=== SUBPROCESS OUTPUT ===")
                    print("Game completed successfully!")
                    print(f"Final Result: {game_result}")
                    print("=======================")
                    return True
                else:
                    print("No JSON result found in output")
                    return False
            except json.JSONDecodeError as e:
                print(f"Error parsing game output: {e}")
                if json_line:
                    print(f"Raw output was: {json_line}")
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
