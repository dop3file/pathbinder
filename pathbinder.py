import os
import sys


cli_args: list = sys.argv
path_file = 'paths.txt'

def arg_parser(args: list) -> None:
	try:
		command = args[1] if len(args) > 1 else None
		# path with way to file example G:\программирование new\pathbinder\pathbinder.py
		path = args[2] if len(args) > 2 else None                
		parameter = args[3] if len(args) > 3 else None

		all_additional_args = [path, parameter]

		commands = {'set': set_new_path,
					'open': open_path
		}
		commands[command](*all_additional_args)
	except KeyError:
		print('no arguments')

def set_new_path(path, name):
	with open(path_file, 'a') as file:
		file.write(f'{name} {path}\n')

def open_path(path, name):
	with open(path_file, 'r') as file:
		all_lines = {line.strip().split(' ')[0]:line[len(line.strip().split(' ')[0]) + 1:-1].replace(r'\\\\','') for line in file}
		os.chdir('../' * all_lines[name].count('\\'))
		os.chdir(f'cd {all_lines[name]}')


arg_parser(cli_args)
















#print(Fore.GREEN + strings.start_message)
#pwd = "G:\\фриланс\\shop_btc\\greed\\shop_btc" 
#os.chdir(pwd) 
 
#print(os.system('py core.py')) 