'''
	Мур Мяу кодировка v2.0
	Графическое окружение
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from mmc import Convert

Window.clearcolor = (59/255, 58/255, 59/255, 1)
Window.title = "Мур Мяу Кодировка"

class Main(App):
	def __init__(self, path):
		super(Main,self).__init__()
		self.engine = Convert() # Подключение Конвертера
		self.key_path = self.engine.read_key(path) # Подключение ключа шифрования

		self.mmc_text_textbox = Label(
			text='Текст',
			font_size=20,
			size_hint=(1, .1)
			)

		self.mmc_text_inputbox = TextInput(
			hint_text='Введите кодируемый текст', 
			multiline=True, text_language="ru-RU",
			padding_x=20,
			padding_y=20
			)

		self.btn = Button(
			text="Применить", 
			background_color=(0,1,0,1),
			color=(1,1,1,1),
			size_hint=(1, .1)
			)

		self.btn.bind(on_press = self.OnClick)
	
	def OnClick(self, instance): # При нажатии на кнопку
		data = self.mmc_text_inputbox.text

		if data != "":
			
			if self.engine.check_content(data): # Если код
				self.mmc_text_inputbox.text = self.engine.decode(data)

			else: # Если текст
				self.mmc_text_inputbox.text = self.engine.encode(data)

	def build(self):
		box = BoxLayout(orientation='vertical', 
			padding=[10,0,10,10])

		box.add_widget(self.mmc_text_textbox)
		box.add_widget(self.mmc_text_inputbox)
		box.add_widget(self.btn)

		return box

#	RUN
if __name__ == '__main__':
    app = Main(path="config.json")
    app.run()