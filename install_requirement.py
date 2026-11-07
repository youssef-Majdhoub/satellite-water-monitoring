import subprocess
import sys
import os

# Define the minimum Python version required (e.g., 3.10)
MIN_PYTHON_VERSION = (3, 10)


def install_requirements():
    print("🚀 Starting environment setup...\n")

    # 1. Check Python Version
    current_version = sys.version_info
    if current_version < MIN_PYTHON_VERSION:
        print(
            f"❌ ERROR: You are using Python {current_version.major}.{current_version.minor}."
        )
        print(
            f"👉 This project requires Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or higher."
        )
        print(
            "   Please download the latest version from python.org and recreate your .venv."
        )
        return

    print(
        f"✅ Python version {current_version.major}.{current_version.minor} is compatible."
    )

    # 2. Safety Check: Are we in the Virtual Environment?
    if sys.prefix == sys.base_prefix:
        print("❌ ERROR: You are NOT using the virtual environment.")
        print(
            "👉 Fix: Click the Python version in the bottom-right corner of VS Code and select '.venv'."
        )
        return

    print("✅ Virtual environment detected safely.")

    # 3. Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ ERROR: 'requirements.txt' not found.")
        print("👉 Make sure you are in the root folder of the project (PFA2027).")
        return

    # 4. Install exact packages
    print("\n📦 Installing exact versions from requirements.txt...")
    try:
        # Run pip install -r requirements.txt
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Check your internet connection.")
        return

    print("\n🎉 SUCCESS! Your environment is perfectly synced with the repository.")
    print("You can now run any of the project scripts (e.g., download_sentil1.py).")


if __name__ == "__main__":
    install_requirements()
