from twilio.rest import Client

account_sid = 'AC0c958327e6b1bb721c11c8cfdd936b8c'
auth_token = '3248e9ea6fc6dda4dc5e0cba06833886'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+13206133113',
    body='Hi how are you?',
    to='+919967990831'
)

print(message.sid)
