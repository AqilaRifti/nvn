import sys
args_config = {"name": None, "args": None, "opts": None}

def ask():
	try:
		command_name = sys.argv[1]
		args_config["name"] = command_name
	except Exception:
		pass

	try:
		command_args = sys.argv[2]
		args_config["args"] = command_args
	except Exception:
		pass

	try:
		command_opts = sys.argv[3]
		args_config["opts"] = command_opts
	except Exception:
		pass