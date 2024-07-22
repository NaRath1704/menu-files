from twilio.rest import Client

account_sid = 'AC9d7cf318a1c101e8cbd511ab25060c7a'
auth_token = 'd126f4896c906ac6760be5e573b4d615'

twilio_num = '+17079690945'

my_phone_no = input('ENTER THE PHONE NUMBER:  ')


msg = input("ENTER THE MESSAGE: ")

client = Client(account_sid,auth_token)

message = client.messages.create(
    body=msg,
    from_=twilio_num,
    to=my_phone_no
)

print(message.body)
