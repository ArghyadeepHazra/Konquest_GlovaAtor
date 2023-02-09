
from twilio.rest import Client
def make_call():
    account_sid = "Your Account"
    auth_token = "Your Auth"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+918210410103',
                            from_='+19402919532')
    print(call.sid)
    

 
