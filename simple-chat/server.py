"""Simple python livereload server to serve static files."""

import importlib.metadata
import shutil
import subprocess
import sys

required = {"livereload"}
installed = {pkg.metadata["Name"] for pkg in importlib.metadata.distributions()}
missing = required - installed


def install_required_packages():
    if missing:
        print(f"Installing {missing} packages.")
        # Check if uv is available
        uv_path = shutil.which("uv")
        if uv_path:
            # Use uv to install packages
            subprocess.check_call(["uv", "pip", "install", "-r", "requirements.txt"])
        else:
            # Fallback to pip if uv is not available
            print("uv not found, falling back to pip")
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])


def start_server():
    from livereload import Server  # type: ignore

    server = Server()
    server.watch("*.html")
    server.serve()


install_required_packages()
start_server()
