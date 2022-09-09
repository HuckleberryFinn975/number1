########################### Задача ###########################
'''
Написать скрипт, который, основываясь на вводных, выведет на печать предложения, содержащие текст из message.
input -> wand
result -> "The Consul watched as Kassad raised the death wand."
input -> the
result ->  """The sky the port was the color of television, tuned to a dead channel.
		   The man in black fled across the desert, and the gunslinger followed."""
Т.е result это одна строка, содержащая в себе предложение, в которое входит слово, заданное юзером (поле text в словаре message)
P.S:
Вносить изменения в исходную структуру можно. Например, если хотите создать словарь для описания уровней типа
eng_levels = {"beginner": 0,
 			  "pre-intermediate": 1,
 			  "intermediate": 2}
'''

########################### Вводные данные ###########################

def func(sentences, user, word = "take"):
	user_sentences = []
	for sentence in sentences:
		if sentence["level"] == user["level"]:
			if word in sentence.get("text"):
				user_sentences.append(sentence.get("text"))

	if user_sentences == []:
		result_message = f'Речення рівня {user["level"]}, які містять слово {word} відсутні'
	else:
		result_message = "\n-------\n".join(user_sentences)
	return result_message

sent1 = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand take.",
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]

sent2 = [
	{"text": "London is the capital of Great Britain",
	"level": 0},
	{"text": "The capital is often the largest city, though not always",
    "level": 1},
	{"text": "Classical and neoclassical economics regard capital as one of the factors of production",
    "level": 2},
	{"text": "Capital Bra is the best",
    "level": 0},
	{"text": "Kyiv is the capital and most populous city of Ukraine",
	"level": 1},
	{"text": "The number of new capitals in the world increased substantially since the Renaissance period",
    "level": 2}
]

user1 = {"username" : "Egor",
		"level" : 1}
word1 = "take"

user2 = {"username" : "Igor",
		"level" : 2}
word2 = "capital"

var1 = func(sent1, user1, word1)

var2 = func(sent2, user2, word2)

# print(var1)
# print(var2)
#
#
# В результате выполнения вот этой команды:

# В терминале должно вывестись вот это:
"""
"We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore"
"""


"""
Варианты улучшения кода:
- Предусмотрите 3 варианта развития событий
	- одно совпадение
	- несколько совпадений
	- ни одного совпадения
- Сделайте так ,чтоб в случае нескольких совпадений предложения внутри результирующей строки как-то визуально разбивались.
  Например серез три точки:
  The sky the port was the color of television, tuned to a dead channel.
  ...
  The Consul watched as Kassad raised the death wand.
  ...
- Напишите варианты кода в случаях, когда level это цифра и когда это строка. Т.е 1 или "beginner"
"""