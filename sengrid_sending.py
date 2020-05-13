from sendgrid.helpers.mail import CustomArg, From, To, Subject, MimeType, Content, Mail
from sendgrid import SendGridAPIClient
import pdb
def sending_email(data):
    email = data['email']
    uid = "1" 
    message = Mail()
    message.to = To(email)
    message.template_id = "d-5141e682aa76"
    message.dynamic_template_data = {'subject': 'sign up verification','email':data['email'],'HOSTING_URL':'http://ec2-34-226-191-16.compute-1.amazonaws.com',
        'first_name':"prathap"}
    message.subject = Subject('sign up verification email')
    message.from_email = From('abhijit.kulkarni@cognitiveclouds.com')
    sg = SendGridAPIClient("SGYAta2_q")
    response = sg.send(message)
    print(sg)
    print(response)

sending_email({"email": "pmohansaikrishna@gmail.com"})

'''
  References:
  https://app.sendgrid.com/guide/integrate/langs/python
'''