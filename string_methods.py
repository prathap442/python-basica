a = "prathap"
print(a.count('p'))# the statement basically returns the count of p's in the string in the variable a 
# count is the method for the string to count the number of the characters
'''
  Hey guys this is the way that we do multi line commenting in python
'''
user_email = input("can you enter your email please")
user_name = user_email[:(user_email.index('@'))]
print(user_name)
#user_domain = user_email[user_name(user_name.index('.'))+1:]
user_domain = user_email[(user_email.index('@')+1)::1]
print(user_domain)
#print("the username extracted is {0} the email is{1} the user domain is {2}",(user_name,user_email,user_domain))
