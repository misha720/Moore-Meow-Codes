'''
	Moore Meow Codes v2.0
	Framework
'''
import os
import json

class Convert():

	def __init__(self):
		super(Convert,self).__init__()
		self.security_keys = {}
		self.bit = 6

	def check_content(self, content):
		'''
			Проверяет какого типа строка Текст / ММС-Код

			Возвращает True, если переданная строка является ммс-кодом 
		'''
		crop = content[0]

		if crop == "r" or crop == "y":
			print("Передан код")
			return True
		else:
			print("Передан текст")
			return False
			
	def encode(self, content):
		'''
			Зашифровывает сообщение

			content - Текст сообщения который нужно зашифровать

			Возвращает необработанный код
		'''
		result = ""
		if self.security_keys != "":
			# Если ключ безопасности настроен
			
			for letter in content:
				# Перебераем каждый символ текста

				if letter != " ":
					for key_letter in self.security_keys.items():
						# Перебераем весь ключ
						
						if letter == key_letter[0]:
							result += key_letter[1]

				else: 
					# Если в слове есть пробел, то просто перенести пробел в результат
					result += letter

			return result

		else:
			return " | Ошибка | Ключ безопасности не установлен!"

	def decode(self, content):
		'''
			Расшифровывает сообщение
			
			content - Код сообщения который нужно расшифровать

			Возвращает текстовое сообщение
		'''
		result = ""
		letter_array = [] # Промежуточный результат
		list_words = content.split()

		if self.security_keys != "":
			# Если ключ безопасности настроен
			
			for word in list_words:
				# Перебираем каждое слово из текста

				begin = 0 # Начальная точка среза
				end = self.bit # Конечная точка среза

				for _ in range(int(len(word) // self.bit)):
					cut = word[begin:end]
					# Прибавляем шаг в соответствии с bit
					begin += self.bit 
					end += self.bit

					letter_array.append(cut)
				letter_array.append(" ")

			for letter in letter_array:
				if letter == " ":
					result += letter
				else:
					#print(letter)
					for key_letter in self.security_keys.items():
						# Перебераем весь ключ
						
						if letter == key_letter[1]:
							result += key_letter[0]

			return result
		else:
			return " | Ошибка | Ключ безопасности не установлен!"

	def read_key(self, key_path):
		'''
			Читает ключ

			key_path - Обсолютный путь до ключа

			Возвращает json объект с образом ключа
		'''

		if os.path.isfile(key_path):

			with open(key_path, "r") as file_security_key:
				self.security_keys = json.load(file_security_key)

			return "Ключ, по адресу " + key_path + ", установлен!"

		else:
			return " | Ошибка | Такого файла не существует! " + key_path		

	# def creat_key(self, bit_size=8):
	# 	'''
	# 		Создаёт ключ

	# 		bit_size - Количество символов кода на 1 символ текста 

	# 		Возвращает True если ключ был успешно создан
	# 	'''

	def shrink(self, content):
		'''
			Сжимает код 

			ryrrrrryrrryrryrryrrrryrrrryryryrryy

			Возвращает сжатый код
		'''
		list_words = content.split()
		result = ""
		for word in list_words:
			
			old_letter = word[0] # Придыдущий символ
			count = 0
			new_code = "" # Промежуточный результат

			for index_letter in range(len(word)):
				
				if word[index_letter] == old_letter:
					count += 1
				else:
					new_code += str(count) + str(old_letter)
					old_letter = word[index_letter]
					count = 1

			new_code += str(count) + str(old_letter) + " "
			result += new_code 
		return result

	# def increase(self, content):
	# 	'''
	# 		Расжимает код

	# 		Возвращает код
	# 	'''

