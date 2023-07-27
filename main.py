import os
import subprocess
import re
import time
import yaml

def is_music(entry):
	return '.mp3' in entry
	
def is_image(entry):
	return re.search(".jpg|.jpeg|.png", entry) is not None
	
def move_file(filename, origin_dir, destination_dir):
	os.system('mv "{}"/"{}" "{}"'.format(origin_dir, filename, destination_dir))

	
def main():
	with open('config.yml', 'r') as file:
		config_file = yaml.safe_load(file)
	download_dir = config_file['downloads']
	music_dir = config_file['music']
	image_dir = config_file['images']
	
	print('Files will be redirected from:')
	print('Downloads (mp3) -> Music')
	print('Downloads (jpg, jpeg, png) -> Pictures')
	
	while True:
		entries = os.listdir(download_dir)
		
		for entry in entries:
			if(is_music(entry)):
				move_file(entry, download_dir, music_dir)
				print('Music moved {}'.format(entry))
			elif(is_image(entry)):
				move_file(entry, download_dir, image_dir)
				print('Image moved {}'.format(entry))
		time.sleep(10*60)
			
if __name__ == "__main__":
	main()
