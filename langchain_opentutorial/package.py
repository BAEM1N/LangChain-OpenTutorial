# langchain_opentutorial/package.py
import subprocess
import sys

def install(packages, verbose=True, upgrade=False):
    """
    Install the given list of Python packages using pip in a single command.

    Args:
        packages (list): A list of package names to install.
        verbose (bool): Whether to print installation messages. Defaults to True.
        upgrade (bool): Whether to upgrade the packages if already installed. Defaults to False.
    """
    if not isinstance(packages, list):
        raise ValueError("Packages must be provided as a list.")
    if not packages:
        print("No packages to install.")
        return
    
    try:
        if verbose:
            print(f"Installing packages: {', '.join(packages)}...")
        
        # Build the pip command
        cmd = [sys.executable, "-m", "pip", "install"]

        # cmd = [sys.executable, "-m", "pip", "install", "--use-feature=fast-deps", "-i", "https://mirror.kakao.com/pypi/simple"]
        if upgrade:
            cmd.append("--upgrade")
        cmd.extend(packages)  # Add all packages at once
        
        # Execute the pip install command
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL if not verbose else None)
        
        if verbose:
            print(f"Successfully installed: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Failed to install packages: {', '.join(packages)}")
            print(f"Error: {e}")
