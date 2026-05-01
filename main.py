import os
import subprocess
import sys

def run_trojan_horse():
    # 1. Grab the GitHub Personal Access Token from FluxCloud's environment variables
    token = os.environ.get('GITHUB_PAT')
    if not token:
        print("Error: GITHUB_PAT environment variable is missing!")
        sys.exit(1)

    # Replace with your actual username and private repository name
    repo_url = f"https://{token}@github.com/juand89/RNN.git"
    clone_dir = "/app/strategy"

    # 2. Silently clone the private repository
    print("Downloading private strategy...")
    subprocess.run(["git", "clone", repo_url, clone_dir], check=True)

    # 3. Install the private strategy's dependencies
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", f"{clone_dir}/requirements.txt"], check=True)

    # 4. Change directory and run your bots
    print("Starting strategies...")
    os.chdir(clone_dir)
    
    # Run the main strategy in the background
    subprocess.Popen([sys.executable, "polymarket_arbitrage_trading/polymarket_eth_5m_open_strategy.py"])
    
    # You can add more scripts here if needed:
    # subprocess.Popen([sys.executable, "dashboard_btc_5m_open.py"])
    # subprocess.Popen([sys.executable, "polymarket_sum_arbitrage.py"])

    # Keep the main process alive so the container doesn't exit
    print("Trojan horse running successfully. Waiting...")
    os.wait()

if __name__ == "__main__":
    run_trojan_horse()
