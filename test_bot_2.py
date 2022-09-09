
import requests
import HomeWork5

token = "5536685745:AAHwOShygUFxr23_KxrbVF9YrzXVoIlycfs"
root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204

def get_bot_info(token):
	url = f"{root_url}{token}/getMe"
	response = requests.get(url)
	bot_info = response.json()
	return bot_info

def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	response = requests.get(url)
	updates = response.json()
	if response.status_code in ok_codes:
		result = {"error": None, "data": updates}
		return result
	else:
		result = {"error": "Bad code", "data": None}
		# print(f"Request failed with status: {response.status_code}")

def send_message(chat_id, message):
	url = f"{root_url}{token}/sendMessage"

	response = requests.post(url, json={'chat_id':chat_id, 'text': message})
	status = response.status_code
	
	if status != 200:
		print("Error message")

last_message_id = 0

tekst1 = HomeWork5.func(HomeWork5.sent1, HomeWork5.user1, HomeWork5.word1)


while True:
	updates = get_updates(token)
	last_message = updates.get('data').get('result')[-1]
	chat_id = last_message.get('message').get('chat').get('id')
	message_text = last_message.get('message').get('text')
	tekst2 = HomeWork5.func(HomeWork5.sent1, HomeWork5.user1, message_text)
	#print(updates["data"]["result"])
	message_id =  last_message.get('message').get('message_id')

	if message_id > last_message_id:
		last_message_id = message_id
		send_message(chat_id, tekst2)

#

# send_message(866012534, tekst1)
# updates = get_updates(token)
#
# if len(updates["result"]) > 0:
# 	last_message = updates["result"][-1]
# 	last_message_text = last_message["message"]["text"]
# 	print(last_message_text)
# else:
# 	print("No messages")
#




# print(get_bot_info(token))
# print(get_updates(token))
#
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json())