import os
import sys

from exceptions import NoArguments, WrongPathName


PATH_FILE = r'G:\\программирование new\\pathbinder\\paths.txt'

def arg_parser(args: list) -> None:
	command = args[1] if len(args) > 1 else None
	# path or name of path in txt
	first_additional_arg = args[2] if len(args) > 2 else None
	# path or name of path in txt              
	second_additional_arg = args[3] if len(args) > 3 else None

	args_group = lambda count_args: [command, first_additional_arg] if count_args == 3 \
																	else [command, first_additional_arg, second_additional_arg]
	return args_group(len(args))

def function_router(command):
	try:
		commands = {'set': set_new_path,
					'open': open_path
		}

		return commands[command]
	except KeyError:
		raise NoArguments

def set_new_path(path: str, name: str) -> None:
	with open(PATH_FILE, 'a') as file:
		file.write(f'{name} {path}\n')

def open_path(name: str) -> None:
	try:
		with open(PATH_FILE, 'r') as file:
			all_lines = {line.strip().split(' ')[0]:line[len(line.strip().split(' ')[0]) + 1:-1].replace(r'\\\\','') for line in file}
			
			directorys = all_lines[name].split('\\')
			disk = directorys[0]
			file_to_open = directorys[-1]

			directorys = directorys[1:-1]

			os.chdir(disk)
			os.chdir('../' * (all_lines[name].count('\\') + 1))

			for directory in directorys:
				os.chdir(directory)

			print(os.system(f'py {file_to_open}'))
	except KeyError:
		raise WrongPathName

def main():
	cli_args: list = sys.argv

	try:
		args = arg_parser(cli_args)
		function_router(args[0])(*args[1:])

	except TypeError as e:
		print(e)
		print('No additional arguments!')
	except WrongPathName:
		print('Wrong Path name!')
	except NoArguments:
		print('No arguments!')


if __name__ == '__main__':
	main()