from twilio.rest import Client
import os
import openai
from dotenv import load_dotenv

load_dotenv()
# Your Twilio account credentials
account_sid = os.environ['twilio_account_sid']
auth_token = os.environ['twilio_auth_token']
twilio_number = os.environ['twilio_number']
second_twilio_number = os.environ['second_twilio_number']
third_twilio_number = os.environ['third_twilio_number']
segment_write_key = os.environ['WRITE_KEY']

twilio_numbers = [twilio_number, second_twilio_number, third_twilio_number]

base_url = os.environ['BASE_URL']

# The webhook URL for handling the call events
call_webhook_url = base_url+"/twilio_call"

# Create a Twilio client object
client = Client(account_sid, auth_token)

# set OpenAi Key for GPT4
openai.api_key = os.environ['OPENAI_APIKEY']