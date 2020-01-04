import keyboard as kb
import pyperclip as pc

value = ''
value1 = ''
value2 = ''
value3 = ''
value4 = ''


def copy(number='0'):

	global value
	global value1
	global value2
	global value3
	global value4

	if pc.paste() != '':
		if number == '0':
			value = pc.paste()
		elif number == '1':
			value1 = pc.paste()
		elif number == '2':
			value2 = pc.paste()
		elif number == '3':
			value3 = pc.paste()
		elif number == '4':
			value4 = pc.paste()


def paste(number='0'):
	global value
	global value1
	global value2
	global value3
	global value4

	if number == '0':
		pc.copy(value)
	elif number == '1':
		pc.copy(value1)
	elif number == '2':
		pc.copy(value2)
	elif number == '3':
		pc.copy(value3)
	elif number == '4':
		pc.copy(value4)


kb.add_hotkey('ctrl+c+0', copy)
kb.add_hotkey('ctrl+alt+0', paste)
kb.add_hotkey('ctrl+c+1', copy, args=('1'))
kb.add_hotkey('ctrl+alt+1', paste, args=('1'))
kb.add_hotkey('ctrl+c+2', copy, args=('2'))
kb.add_hotkey('ctrl+alt+2', paste, args=('2'))
kb.add_hotkey('ctrl+c+3', copy, args=('3'))
kb.add_hotkey('ctrl+alt+3', paste, args=('3'))
kb.add_hotkey('ctrl+c+4', copy, args=('4'))
kb.add_hotkey('ctrl+alt+4', paste, args=('4'))

kb.wait()

