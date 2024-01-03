import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True)
        print(f"Command '{' '.join(command)}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{' '.join(command)}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <target_domain>")
        sys.exit(1)

    target_domain = sys.argv[1]

    # Run commands for each tool
    run_command(["sublist3r", "-d", target_domain, "-o", "sublister_result.txt"])
    run_command(["python3", "securitytrails.py", target_domain])
    run_command(["subfinder", "-d", target_domain, "-o", "subfinder_result.txt"])
    run_command(["python3", "crtsh.py", target_domain])
