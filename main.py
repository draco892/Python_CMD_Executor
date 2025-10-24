import subprocess

def run_commands_from_file(filename="command.txt"):
    """
    Reads commands from a text file and executes them in the system shell.
    Each non-empty line in the file is treated as a separate command.
    """
    try:
        # Read all commands from the file
        with open(filename, "r", encoding="utf-8") as file:
            commands = [line.strip() for line in file if line.strip()]
        
        # Execute each command in order
        for cmd in commands:
            print(f"\nExecuting: {cmd}")
            try:
                result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
                if result.stdout:
                    print("Output:\n", result.stdout)
                if result.stderr:
                    print("Errors:\n", result.stderr)
            except Exception as e:
                print(f"Error while executing '{cmd}': {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"General error: {e}")

if __name__ == "__main__":
    run_commands_from_file()
