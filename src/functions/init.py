import os, sys, pathlib
import out

foldername = input("Project Name: ")
nvn_files = ["config", "plugins", "cache", "map", "script"]
nvn_folder = f"{foldername}/.nvnfile/"

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
print("ter")

def create_nvn_config():

def create_nvn_file():
	for i in range(len(nvn_files)):
		nvn_files_content = '{\n\t"name": ' + '"' + nvn_files[i] + '"' + '\n}'
		f = open(f"{nvn_folder}{nvn_files[i]}{nvn_extension}", "w")
		f.write(nvn_files_content)
		f.close()

create_nvn_file()