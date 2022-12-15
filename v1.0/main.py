'''
	Mr-Myau Codding
'''

import os
import json

bit = 6 # Колличество символов для кодировки

with open('config.json', 'r') as file:
	codes = json.load(file)

def filter(content, type_filter): 
	'''
		Нужен для преобразования в читабельный вид
		(типо не "rryrrr", а "МрМрМяуМрМрМр")
	'''
	if type_filter == 'encode': # Если нужно раскодировать скрипт
		res = ""

		for item in content:
			if item == 'r':
				res = res + " Мрр "

			elif item == 'y':
				res = res + " Мяу "

			elif item == ';':
				res = res + ";"

		return res

	elif type_filter == 'decode': # Если нужно закодировать в скрипт
		res = ""

		for item in content:
			if item == "Мрр":
				res = res + "r"

			elif item == "Мяу":
				res = res + "y"
			elif item == ";":
				res = res + ";"


		return res

def encode(text): # "word" => "ryrry"
	content = ""

	list_words = text.split()

	for item in list_words:
		for word in item:
			content = content + codes[word] + " "
		content = content + ";"
	print("---------------------")
	print(filter(content, "encode"))
	print("---------------------")

def decode(code): # "ryrry" => "word"
	content = ""
	msg = []
	global bit
	list_words = code.split()

	content = filter(list_words, "decode")
	content = content.replace(";", ' ')
	content = content.split()

	for word in content:

		len_word = len(word) 

		count = len_word / bit

		end = 0
		for _ in range(int(count)):
			res = word[end:bit]
			bit += 6
			end += 6

			msg.append(res)

		bit = 6
		end = 0
		len_word = 0
		count = 0
		msg.append(" ")

	cont = ""
	# Переводим обратно в живой текст
	for item in msg:
		#print(item)
		for key in codes:
			#print(key)
			if item == " ":
				cont = cont + " "
			elif item == codes[key]:
				cont = cont + key

	cont = cont.split()

	result = ""
	for i in cont:
		result += i + " "

	print("---------------------")
	print(result)
	print("---------------------")

def main():
	print("Вас приветствует Мур-Мяу КОТировка!!")
	print("    [1] Закодировать сообщение(encode) ")
	print("    [2] Декодировать сообщение(decode) ")
	
	while True:
		command = input("Что будем делать? - ")

		if command == "1" or command == "encode" or command == "закодировать":
			text = input("Введите сообщение - ")
			encode(text)
		elif command == "2" or command == "decode" or command == "декодировать":
			code = input("Введите код - ")
			decode(code)

# RUN
if __name__ == "__main__":
	main()
