import os, sys, pathlib
import out

foldername = input("Project Name: ")
try:
	p = pathlib.Path(foldername).mkdir(parents=True)
except FileExistsError:
	out.error("There is already folder with that name!")

p = pathlib.Path(foldername + "/" + ".nvnfile").mkdir(parents=True, exist_ok=True)

def create_folder(foldername):
	p = pathlib.Path(foldername).mkdir(parents=True, exist_ok=True)

nvn_json = open(f"{foldername}/nvn.json", "w")
nvn_config = open(f"{foldername}/.nvnfile/config.nvn.json", "w").write('{\n\t"name": "config"\n}')
nvn_plugin = open(f"{foldername}/.nvnfile/plugins.nvn.json", "w").write('{\n\t"name": "plugins"\n}')
nvn_cache = open(f"{foldername}/.nvnfile/cache.nvn.json", "w").write('{\n\t"name": "cache"\n}')

nvn_json.write('')
nvn_json.close()