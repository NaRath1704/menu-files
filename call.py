from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# Your Twilio Account SID and Auth Token from https://www.twilio.com/console
account_sid = 'AC9d7cf318a1c101e8cbd511ab25060c7a'
auth_token = 'd126f4896c906ac6760be5e573b4d615'

twilio_num = '+17079690945'

# The recipient's phone number in international format
to_number = input("ENTER THE NUMBER:  ")
print("Entered Number:", to_number)

# The message to be spoken during the call
msg = input("ENTER THE MESSAGE: ")
print("Entered Message:", msg)

try:
    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Create the TwiML response with the message
    response = VoiceResponse()
    response.say(msg)

    # Convert the TwiML response to a string
    twiml_str = str(response)

    # Make the call
    call = client.calls.create(
        twiml=twiml_str,
        to=to_number,
        from_=twilio_num
    )

    # Print call SID for reference
    print(f'Call SID: {call.sid}')
    print('Calling...')

except Exception as e:
    print(f'Error: {e}')
