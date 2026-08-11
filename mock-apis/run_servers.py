"""
Start both mock APIs in separate processes.

Usage:  python mock-apis/run_servers.py

Source (monitoring):   http://127.0.0.1:5001
Destination (ticketing): http://127.0.0.1:5002
"""

import subprocess
import sys
import time
from pathlib import Path

MOCK_DIR = Path(__file__).parent


def main():
    print("Starting mock APIs...")
    print("  Source (monitoring):   http://127.0.0.1:5001")
    print("  Destination (ticketing): http://127.0.0.1:5002")
    print("  Press Ctrl+C to stop both.\n")

    source = subprocess.Popen(
        [sys.executable, str(MOCK_DIR / "source_api.py")],
        cwd=MOCK_DIR.parent,
    )
    dest = subprocess.Popen(
        [sys.executable, str(MOCK_DIR / "destination_api.py")],
        cwd=MOCK_DIR.parent,
    )

    try:
        while True:
            time.sleep(1)
            if source.poll() is not None or dest.poll() is not None:
                print("A server exited unexpectedly.")
                break
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        source.terminate()
        dest.terminate()
        source.wait()
        dest.wait()


if __name__ == "__main__":
    main()
