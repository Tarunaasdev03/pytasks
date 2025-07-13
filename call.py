from twilio.rest import Client

# Your Twilio credentials
account_sid = 'ACf---------------f9ab'
auth_token = '0-------26cf83--------6b58'
client = Client(account_sid, auth_token)

call = client.calls.create(
    to='..........',  # Replace with the recipient's phone number
    from_='..........',  # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'
)

print(f"Call initiated with SID: {call.sid}")
