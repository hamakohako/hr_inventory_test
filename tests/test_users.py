import pytest
from hr import users

user_dict = {
  'name': 'kevin',
  'groups': ['wheel', 'dev'],
  'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
}




#def test_match_user_should_print():
#	match, no_match = users.match_users('/home/user/code/hr/sample2.json')
#
#	assert no_match == ['connection1', 'connection2']
#	assert match == ['username']
