#!/usr/bin/env python3

import os
import re
import sys
import time
import subprocess
import shutil

path = sys.argv[1]


def clean_dir(dir_path):
	for file in os.listdir(dir_path):
		query = re.search(r'\.mp4', file)
		query2 = re.search(r'\.mkv', file)
		query3 = re.search(r'\.avi', file)
		if query != None or query2 != None or query3 != None:
			os.rename(os.path.join(dir_path, file), os.path.join(path, file))
		elif os.path.isdir(os.path.join(dir_path, file)):
			shutil.rmtree(file)
		else:
			os.remove(file)


def not_hidden_file(item):
	print(item)
	query = re.search(r'^\..*', item)
	if query != None:
		return False
	return True


def format_check(path):
	"""function to check if the title is already in the correct format i.e. movie title (2020)"""
	incorrect_formats = []
	pattern = r'[\w ]*\([\d]*\).mp4'
	for movie in os.listdir(path):
		result = re.search(pattern, movie)
		if result == None:
			incorrect_formats.append(movie)
	return incorrect_formats


def rename(path):
	for item in format_check(path):
		print(item)
		movie_title = input('Movie Title: ')
		movie_year = input('Movie Year: ')
		substitute = f'{movie_title} ({movie_year}).mp4'
		subprocess.run(['mv', item, substitute])


def main(path):
	for item in os.listdir(path):
		if os.path.isdir(os.path.join(path, item)) and not_hidden_file(item):
			os.chdir(os.path.join(path, item))
			dir_path = os.getcwd()
			clean_dir(dir_path)
			os.chdir(path)
			os.rmdir(dir_path)
		else:
			continue
	os.chdir(path)
	rename(path)


time.sleep(2)
main(path)
