#!/usr/bin/python3

import os
import re
import sys
import time

path = sys.argv[1]


def locate_and_clean(path):
	for item in os.listdir(path):
		if os.path.isdir(os.path.join(path, item)) and not_hidden_file(item) and not item == 'lost+found':
			os.chdir(os.path.join(path, item))
			dir_path = os.getcwd()
			clean_dir(dir_path)
			os.chdir(path)
			os.rmdir(dir_path)
		else:
			continue


def clean_dir(dir_path):
	for file in os.listdir(dir_path):
		query = re.search(r'\.mp4', file)
		query2 = re.search(r'\.mkv', file)
		if query != None or query2 != None:
			os.rename(os.path.join(dir_path, file), os.path.join(path, file))
		else:
			os.remove(file)


def not_hidden_file(item):
	query = re.search(r'^\..*', item)
	if query != None:
		return False
	return True


time.sleep(10)
locate_and_clean(path)
