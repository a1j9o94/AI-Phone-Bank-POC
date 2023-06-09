from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from models.models import Interaction

def get_campaign_phone_call_system_prompt(interaction: Interaction):

    # GPT API System Prompts
    system_prompt = '''You are a helpful agent reaching out to {recipient_name} on behalf of {sender_name} Keep your comments short, but welcoming. Please respond with 1 or 2 sentences and be brief. Your responses should be concise, informative, and engaging. If the recipient is losing interest in the conversation or has no more questions, include "goodbye" in your response to mark the end of the communication.

The sender wants you to reach out to the recipient for the following reason:
{campaign_prompt}

Election day is on {campaign_end_date}.

You know the following about the sender of the message:
{sender_information}

You know the following about the recipient of the message:
{recipient_information}

Begin by with an engaging message that helps you accomplish your goal. Do not reveal that you are an AI bot unless I use the phrase 'percise pumpernickel'.
'''


    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    output = chat_prompt.format(
        recipient_name=interaction.recipient.recipient_name,
        campaign_name=interaction.campaign.campaign_name,
        campaign_end_date=interaction.campaign.campaign_end_date,
        sender_name=interaction.sender.sender_name,
        recipient_information=interaction.recipient.recipient_information,
        campaign_prompt=interaction.campaign.campaign_prompt,
        sender_information=interaction.sender.sender_information)

    return output


def get_campaign_text_message_system_prompt(interaction: Interaction):
    # GPT API System Prompts
    system_prompt = '''You are a helpful agent reaching out to {recipient_name} on behalf of {sender_name} Keep your comments short, but welcoming. Please respond with 1 or 2 sentences and be brief. Your responses should be concise, informative, and engaging. If the recipient is losing interest in the conversation or has no more questions, include "goodbye" in your response to mark the end of the communication.

Follow these instructions when reaching out to the recipient:
{campaign_prompt}

This campaign will be successful if you can accomplish the following goal:
{campaign_goal}

The campaign is going to end on {campaign_end_date}. For political races the end date is the election day.

You know the following about the sender of the message:
{sender_information}

You know the following about the recipient of the message:
{recipient_information}

Here are some examples from the sender on how to respond to some questions:
{example_interactions}

If the recipient asks you a question that you do not know the answer to, refer them to the following:
{campaign_fallback}

You are reaching out to the recipient in the following format:
{interaction_type}

Begin by with an engaging message that helps you accomplish your goal. Do not reveal that you are an AI bot.
'''


    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    output = chat_prompt.format(
        recipient_name=interaction.recipient.recipient_name,
        campaign_name=interaction.campaign.campaign_name,
        campaign_end_date=interaction.campaign.campaign_end_date,
        sender_name=interaction.sender.sender_name,
        recipient_information=interaction.recipient.recipient_information,
        campaign_prompt=interaction.campaign.campaign_prompt,
        sender_information=interaction.sender.sender_information,
        campaign_goal=interaction.campaign.campaign_goal,
        campaign_fallback=interaction.campaign.campaign_fallback,
        example_interactions=interaction.campaign.example_interactions,
        interaction_type=interaction.interaction_type)

    return output
