from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACd6b2602b4f0f0ff805f4825ebcaf8713"
# Your Auth Token from twilio.com/console
auth_token  = "874c97f50f0cfe78ca1382a1fe6eb5a4"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+17542023934", 
    from_="+13522249790",
    body="Hello from Python!")

print(message.sid)
