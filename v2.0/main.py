from mmc import Convert # Импорт класса

path = "config.json" # Путь до ключа шифрования
engine = Convert() # Инициализация класса
engine.read_key(path) # Установка ключа

def main():
	print("""
    .`````-.  ,---.    ,---.,---.    ,---.,---.    ,---.    _______    
   /   ,-.  \\ |    \\  /    ||    \\  /    ||    \\  /    |   /   __  \\   
  (___/  |   ||  ,  \\/  ,  ||  ,  \\/  ,  ||  ,  \\/  ,  |  | ,_/  \\__)  
        .'  / |  |\\_   /|  ||  |\\_   /|  ||  |\\_   /|  |,-./  )        
    _.-'_.-'  |  _( )_/ |  ||  _( )_/ |  ||  _( )_/ |  |\\  '_ '`)      
  _/_  .'     | (_ o _) |  || (_ o _) |  || (_ o _) |  | > (_)  )  __  
 ( ' )(__..--.|  (_,_)  |  ||  (_,_)  |  ||  (_,_)  |  |(  .  .-'_/  ) 
(_{;}_)      ||  |      |  ||  |      |  ||  |      |  | `-'`-'     /  
 (_,_)-------''--'      '--''--'      '--''--'      '--'   `._____.'   
                                                                       
""")
	print("Welcome Moore-Meow-Codes v2.0\n")
	
	while True:
		content = input("Введите ТЕКСТ либо ММС-КОД: ")
		
		if engine.check_content(content): # Если сообщение является кодом
			print("Code")
			result = engine.decode(engine.increase( engine.filter(content, type_filter="text") ))
			print(result)
			print("---------------------------")

		else: # Если сообщение является текстом
			print("Text")
			result = engine.filter(engine.shrink( engine.encode(content) ), type_filter="mmc") 
			print(result)
			print("---------------------------")

if __name__ == '__main__':
	main()
