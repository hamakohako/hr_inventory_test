import pytest

from hr import cli

@pytest.fixture
def parser():
	return cli.create_parser()

def test_no_arguments_passed(parser):
	'''
	An error is raised if no arguments are passed to the parser.
	'''
	with pytest.raises(SystemExit):
		parser.parse_args()


def test_argument_passed(parser):
	'''
	No error is raised if a path is given as an argument.
	'''
	path = '/some/path/test.json'
	args = parser.parse_args([path])
	
	assert args.path == '/some/path/test.json'


def test_export_flag_passed(parser):
	'''
	The export value is set to True if the --export flag is given.
	'''
	path = '/some/path/test.json'

	args = parser.parse_args([path])
	assert args.export == False

	args = parser.parse_args(['--export', path])
	assert args.export == True

