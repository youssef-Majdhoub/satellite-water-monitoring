import subprocess
import sys
import os

VENV_DIR = ".venv"


def run_setup():
    print("🚀 Starting First-Time Project Setup...\n")

    # 1. Check Python Version
    if sys.version_info < (3, 10):
        print(
            f"❌ ERROR: You are using Python {sys.version_info.major}.{sys.version_info.minor}."
        )
        print("👉 This project requires Python 3.10 or higher. Please update Python.")
        return

    # 2. Create Venv if missing
    if not os.path.exists(VENV_DIR):
        print(
            f"📁 Creating virtual environment '{VENV_DIR}'... (This takes a few seconds)"
        )
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    else:
        print(f"✅ Virtual environment '{VENV_DIR}' already exists.")

    # 3. Find the new venv's Python
    if os.name == "nt":
        venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(VENV_DIR, "bin", "python")

    # 4. Call the installer script using the new venv
    print("\n🔄 Handing over to install_requirements.py to install packages...\n")
    try:
        subprocess.run([venv_python, "install_requirements.py"], check=True)
    except Exception as e:
        print(f"❌ Failed to run install_requirements.py: {e}")
        return

    print(
        "\n🎉 SETUP COMPLETE! 👉 IMPORTANT: In VS Code, look at the bottom-right corner."
    )
    print(
        "Click the Python version and select '.venv' so VS Code uses the new environment!"
    )


if __name__ == "__main__":
    run_setup()
