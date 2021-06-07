import ssl
import os, sys, time
ssl_context = ssl.create_default_context()

from tqdm import tqdm
for i in tqdm(range(100), desc="Fetching"):
	time.sleep(0.5)
	pass