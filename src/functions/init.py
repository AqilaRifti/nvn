import os, sys, pathlib
import out

foldername = input("Project Name: ")
try:
	p = pathlib.Path(foldername).mkdir(parents=True)
except FileExistsError:
	out.error("There is already folder with that name!")

p = pathlib.Path(foldername + "/" + ".nvnfile").mkdir(parents=True, exist_ok=True)

def create_folder(foldername):
	try:
		p = pathlib.Path(foldername).mkdir(parents=True)
	except FileExistsError:
		out.error("There is already folder with that name!")

def create_nvn_file(filename, config=None):
	nvn_files = ["config", "plugins", "cache"]
	if config == None:
		file = open(f"{foldername}/{filename}.json", "w")
	if config != None:
		if config == "nvn_files":
			for i in range(): ...
			file = open(f"{foldername}/.nvnfile/config.nvn.json", "w").write('{\n\t"name": "config"\n}')

#nvn_config = open(f"{foldername}/.nvnfile/config.nvn.json", "w").write('{\n\t"name": "config"\n}')
#nvn_plugin = open(f"{foldername}/.nvnfile/plugins.nvn.json", "w").write('{\n\t"name": "plugins"\n}')
#nvn_cache = open(f"{foldername}/.nvnfile/cache.nvn.json", "w").write('{\n\t"name": "cache"\n}')
#
#
#nvn_json = open(f"{foldername}/nvn.json", "w")
#nvn_config = open(f"{foldername}/.nvnfile/config.nvn.json", "w").write('{\n\t"name": "config"\n}')
#nvn_plugin = open(f"{foldername}/.nvnfile/plugins.nvn.json", "w").write('{\n\t"name": "plugins"\n}')
#nvn_cache = open(f"{foldername}/.nvnfile/cache.nvn.json", "w").write('{\n\t"name": "cache"\n}')
