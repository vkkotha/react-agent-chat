"""Simple python livereolad server to serve static files."""

import importlib.metadata
import subprocess
import sys

required = {"livereload"}
installed = {pkg.metadata["Name"] for pkg in importlib.metadata.distributions()}
missing = required - installed


def install_required_packages():
    if missing:
        print(f"Installing {missing} packages.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])


def start_server():
    from livereload import Server  # type: ignore

    server = Server()
    server.watch("*.html")
    server.serve()


install_required_packages()
start_server()
