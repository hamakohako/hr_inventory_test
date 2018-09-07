import argparse

def create_parser():
	parser = argparse.ArgumentParser(description='HR invetory software')
	parser.add_argument('path', help='Path to file to be exported')
	parser.add_argument('--export', action='store_true', help='Export current settings to json file')
	return parser
