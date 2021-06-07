import os, sys, pathlib

foldername = input("Project Name: ")
p = pathlib.Path(foldername).mkdir(parents=True, exist_ok=True)
f = open(f"{foldername}/config.py", "w")
f.write('{"name": "nvn","version": 1.0,"command": {}}')
f.close()
