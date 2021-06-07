import pathlib, out, os, sys

def create_folder(foldername):
	try:
		folder = pathlib.Path(foldername).mkdir(parents=True)
	except FileExistsError:
		out.error("There is already folder with that name!")
		quit()
