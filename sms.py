def txtmsg(contact):
    from twilio.rest import Client

    account_sid = 'AC-----cb43------2a4f67519de7760'
    auth_token = '6-------274cc8-----a23c212e'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello! This is a test message from Python.",
        from_='+1........85',   
        to=contact     
        )
    print("Message sent! SID:", message.sid)


txtmsg (+91.........)

