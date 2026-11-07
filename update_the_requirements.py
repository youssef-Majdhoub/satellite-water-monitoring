import subprocess
import sys
import os
import re


def update_requirements():
    print("🚀 Starting fully automated dependency scan...\n")

    # 1. Safety Check: Are we in the Virtual Environment?
    if sys.prefix == sys.base_prefix:
        print("❌ ERROR: You are NOT using the virtual environment.")
        print(
            "👉 Fix: Click the Python version in the bottom-right corner of VS Code and select '.venv'."
        )
        return

    print("✅ Virtual environment detected safely.")

    # 2. Use pipreqs to scan code and find imports
    print("🔍 Scanning .py files for imports...")
    try:
        # Run pipreqs on the current directory, overwrite if it exists
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pipreqs",
                ".",
                "--force",
                "--savepath",
                "requirements.in",
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("❌ Failed to scan files. Do you have any .py files with imports?")
        return

    if not os.path.exists("requirements.in"):
        print(
            "⚠️ No external imports found in your code yet. Try adding 'import asf_search' to a file first."
        )
        return

    # 3. Show the user what was found
    with open("requirements.in", "r") as f:
        found_packages = f.read().strip()

    print("\n📦 Found the following high-level dependencies in your code:")
    print("--------------------------------------------------")
    print(found_packages)
    print("--------------------------------------------------")

    # 4. Install packages
    print("\n⚙️ Installing/Updating these packages...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.in"],
            check=True,
        )
    except subprocess.CalledProcessError:
        print(
            "❌ Failed to install packages. Check your internet or the library names."
        )
        return

    # 5. Generate requirements.txt with EXACT versions
    print("\n📝 Locking exact versions into requirements.txt...")
    with open("requirements.txt", "w") as outfile:
        subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=outfile)

    print("\n🎉 SUCCESS! requirements.txt has been automatically generated and locked.")
    print(
        "👉 Commit BOTH requirements.in and requirements.txt to GitHub for your team."
    )


if __name__ == "__main__":
    update_requirements()
