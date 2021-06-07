from .utils.file import *

projectname = input("Project Name: ")
nvn_files = ["config", "plugins", "cache", "map", "script"]
nvn_folder = f"{projectname}/.nvnfile/"

def create_nvn_config():
	f = open(f"{projectname}/nvn.json", "w")
	nvn_config_content = '{\n\t"name": ' + '"' + projectname + '"' + '\n}'
	f.write(nvn_config_content)
	f.close()

def create_nvn_files():
	nvn_extension = ".nvn.json"
	for i in range(len(nvn_files)):
		nvn_files_content = '{\n\t"name": ' + '"' + nvn_files[i] + '"' + '\n}'
		f = open(f"{nvn_folder}{nvn_files[i]}{nvn_extension}", "w")
		f.write(nvn_files_content)
		f.close()

def create_nvn_project():
	create_folder(f"{projectname}/.nvnfile")
	create_nvn_config()
	create_nvn_files()

create_nvn_project()