import json
import grp
import pwd
import spwd

def read_file(path):
	with open(path, 'r') as f:
		user_dict = json.load(f)
		return [user['name'] for user in user_dict]

def export_users(path, userlist=None):
	existing_users = [user.pw_name for user in pwd.getpwall()]
	if userlist == None:
		userlist = existing_users		

	export = []
	for i in userlist:
		name = pwd.getpwnam(i)
		export.append({'name': name.pw_name, 'groups': name.pw_gid, 'password': name.pw_passwd})
	with open(path, 'w') as f:
		json.dump(export, f)
		
	
