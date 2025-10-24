🐍 Command Runner

A simple Python script that reads and executes shell commands from a text file (command.txt).

=== Description ===
This script allows you to automate the execution of multiple terminal commands listed in a file.
Each line in command.txt is treated as an individual command and executed in sequence.

=== How It Works ===
1. The script opens command.txt and reads all non-empty lines.
2. Each command is executed using Python’s subprocess module.
3. The standard output (stdout) and error messages (stderr) for each command are printed in the console.

=== Example ===
command.txt
-----------------
echo "Hello from the terminal!"
ls -la
pwd

Output
-----------------
Executing: echo "Hello from the terminal!"
Output:
Hello from the terminal!

Executing: ls -la
Output:
(total file list...)

Executing: pwd
Output:
/Users/yourname

=== Notes ===
- The script uses shell=True, so make sure the commands in command.txt are safe before running.
- You can change the filename or add additional error handling inside the code if needed.
- Works on macOS, Linux, and Windows (with compatible commands).

=== Usage ===
Run the script with:
python3 run_commands.py

Make sure your command.txt is in the same directory as the script.

=== Info ===
Author: Andrea
Repository: github.com/draco892
License: MIT
Python Version: 3.10+
