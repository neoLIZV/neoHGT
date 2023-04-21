"""
////////////////////////////////////////////////////////////
│	
│	Filename:	server.py
│	Comment:	Server download and setup
│	
│	=======================================================
│	Authorship:	neoLIZV
│	Copyright:	Distributed under the terms of the Modified BSD License.
│	Made with love by @neoLIZV https://github.com/neoLIZV
│	
////////////////////////////////////////////////////////////
"""

import subprocess
import sys
import os
from serverutil import importParser

welcome = """
					 __  ______________
   ____  ___  ____  / / / / ____/_  __/
  / __ \/ _ \/ __ \/ /_/ / / __  / /   
 / / / /  __/ /_/ / __  / /_/ / / /    
/_/ /_/\___/\____/_/ /_/\____/ /_/     

"""

def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])
	
try:
	import requests

	print('\033[96m' + welcome)
	print('\033[36m\033[1m' + 'Welcome to neoHGT 🧬')
	print('\033[0m' + 'neoHGT Server Automation Script helps you to setup neoHGT without Graphical User Interface.\n')
	database_path = input('\033[1m' + 'Please enter the absolute path you want to store the database (drag-and-drop): \033[0m').replace("'",'')
	while not (os.path.isdir(database_path)):
		database_path = input('\033[1m' + 'Please enter the absolute path you want to store the database (drag-and-drop): \033[0m').replace("'",'')
	
	#/*====================*/
	# Step1: HGTector.zip
	importParser('https://www.dropbox.com/sh/tevabydz6palfih/AAB-TitXKNfQl5dmnZM1VfRca?dl=0&preview=hgtdb_20230102.tar.xz', None, database_path, True, True)

	#/*====================*/
	# Step2: run command
	
	
except ImportError as e:
	install('requests')