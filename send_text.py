from twilio.rest import TwilioRestClient

account_sid = "AC63a11cb18f39b2fa0f324a23fa7dac25" # Your Account SID from www.twilio.com/console
auth_token  = "2227a1b24d42c310dfe395e50997979d"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hey, it's me! Testing my program!",
    to="+17246813724",    # Replace with your phone number
    from_="+14127443250") # Replace with your Twilio number

print(message.sid)
