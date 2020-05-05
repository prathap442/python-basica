print("Hey i'm travis waiting for your service")
known_users = ['Alice','Doe','Mae']
while True:
  search_user = raw_input("please enter your name you are searching for")
  if search_user in known_users:
    user_found_input = raw_input('the user already exist do you wish to remove(y/n)').strip().lower()
    if(user_found_input == 'y'):
      known_users.remove(search_user)
      print('After removing the users are {0}'.format(known_users))  
  else:
    add_user = raw_input("the user does not exist do you wish to add(y/n)?").strip().lower()
    if(add_user == 'y'):
      known_users.append(search_user)
      print("After adding the rest of the users are {0}",known_users)

