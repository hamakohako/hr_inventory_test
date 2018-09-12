import argparse

def create_parser():
	parser = argparse.ArgumentParser(description='HR invetory software')
	parser.add_argument('path', help='Path to file to be exported')
	parser.add_argument('--export', action='store_true', help='Export current settings to json file')
	return parser


def main():
	from hr import users, inventory

	args = create_parser().parse_args()

	if args.export:
		inventory.export_users(args.path)
	else:
		user_list = inventory.read_file(args.path)
		users.match_users(user_list)

