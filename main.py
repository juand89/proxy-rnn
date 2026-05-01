import os
import subprocess
import urllib.request
import sys

def start_terminal():
    ttyd_path = "/tmp/ttyd"
    
    # 1. Download ttyd binary
    print("Downloading ttyd (Web Terminal)...")
    try:
        urllib.request.urlretrieve("https://github.com/tsl0922/ttyd/releases/download/1.7.4/ttyd.x86_64", ttyd_path)
        os.chmod(ttyd_path, 0o755)
    except Exception as e:
        print(f"Error downloading ttyd: {e}")
        sys.exit(1)

    # 2. Get credentials from environment variables
    user = os.environ.get("TERMINAL_USER", "admin")
    password = os.environ.get("TERMINAL_PASSWORD", "password")

    # 3. Start the terminal
    print("Starting secure terminal on port 8080...")
    
    # -W: writable (allow typing commands)
    # -p 8080: port
    # -c user:password: basic auth
    # tmux new -A -s flux: Reattaches to the "flux" session, or creates it if it doesn't exist
    subprocess.run([ttyd_path, "-W", "-p", "8080", "-c", f"{user}:{password}", "tmux", "new", "-A", "-s", "flux"])

if __name__ == "__main__":
    start_terminal()
