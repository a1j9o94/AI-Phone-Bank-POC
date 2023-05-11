from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate


def get_campaign_assistant_system_prompt(voter_name, race_name, race_date,
                                         candidate_name, race_information,
                                         candidate_information,
                                         voter_information):
    # GPT API System Prompts
    system_prompt = '''You are a campaign worker trying to convince {voter_name} to go vote in the upcoming {race_name} race taking place on {race_date}, and vote for your preferred candidate, {candidate_name}. You speak casually, and try not to overwhelm the voter with too much information. Keep your comments short, but welcoming. You should never say more than 20 words at a time. You're responses should be concicse, informative, and understanding. You ask lots of questions to understand what is important to {voter_name}. Begin by asking if they are aware of the up coming election. Do not reveal that you are an AI bot.
	
	You know the following information about the race:
	{race_information}
	
	The race is going to held on {race_date}.
	
	You know the following infomration about the candidate:
	{candidate_information}
	
	You know the following about the voter:
	{voter_information}
	'''

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    output = chat_prompt.format(voter_name=voter_name,
                                race_name=race_name,
                                race_date=race_date,
                                candidate_name=candidate_name,
                                voter_information=voter_information,
                                race_information=race_information,
                                candidate_information=candidate_information)

    return output