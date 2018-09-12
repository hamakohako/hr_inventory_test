import sys
import pwd
import subprocess


def match_user(user_dict):
	existing_users = [i.pw_name for i in pwd.getpwall()]
	usernames = [user['name'] for user in user_dict]
	for user in user_dict:
		name, password, groups = (user['name'], user['password'], ','.join(grp for grp in user['groups']))
		if name in existing_users:
			update_user(name, password, groups)
		elif name not in existing_users:
			create_user(name, password, groups)
	for user in existing_users:
		if user in usernames:
			remove_user(user)



def create_user(name, password, groups):
	try:
		print(f"Creating a username for {name}")
		subprocess.run(['useradd', '-p', password, '-G', groups, name])
		print(f"user {name} was successfully created")
	except:
		print(f"Failed to create user {name} ")
		sys.exit(1)


def update_user(name, password, groups):
	try:
		print(f"Updating username - {name}")
		subprocess.run(['usermod', '-p', password, '-G', groups, name])
		print(f"user {name} was successfully updated")
	except:
		print(f"Failed to update user {name}")
		sys.exit(1)


def remove_user(name):
	try:
		print(f"Removing username - {name}")
		#subprocess.run(['userdel', '-r', name])
		print(f"['userdel', '-r', {name}]")
		print(f"user {name} was successfully removed")
	except:
		print(f"Failed to remove user {name}")
		sys.exit(1)

