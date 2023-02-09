from twilio.rest import Client

def sms():
    # Your Account 
    account_sid = "Your Account"
    # Your Auth 
    auth_token  = "Your Auth"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+918210410103", 
        from_="+19402919532",
        body="Help me ! i'm in danger")
    print(message.sid)