import keyboard as kb
import pyperclip as pc

value = ''
value1 = ''
value2 = ''
value3 = ''
value4 = ''
value5 = ''
value6 = ''
value7 = ''
value8 = ''
value9 = ''


def copy(number='0'):

	global value
	global value1
	global value2
	global value3
	global value4
	global value5
	global value6
	global value7
	global value8
	global value9

	if pc.paste() != '':
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
			elif number == '5':
				value5 = pc.paste()
			elif number == '6':
				value6 = pc.paste()
			elif number == '7':
				value7 = pc.paste()
			elif number == '8':
				value8 = pc.paste()
			elif number == '9':
				value9 = pc.paste()


def paste(number='0'):
	global value
	global value1
	global value2
	global value3
	global value4
	global value5
	global value6
	global value7
	global value8
	global value9

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
	elif number == '5':
		pc.copy(value5)
	elif number == '6':
		pc.copy(value6)
	elif number == '7':
		pc.copy(value7)
	elif number == '8':
		pc.copy(value8)
	elif number == '9':
		pc.copy(value9)


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
kb.add_hotkey('ctrl+c+5', copy, args=('5'))
kb.add_hotkey('ctrl+alt+5', paste, args=('5'))
kb.add_hotkey('ctrl+c+6', copy, args=('6'))
kb.add_hotkey('ctrl+alt+6', paste, args=('6'))
kb.add_hotkey('ctrl+c+7', copy, args=('7'))
kb.add_hotkey('ctrl+alt+7', paste, args=('7'))
kb.add_hotkey('ctrl+c+8', copy, args=('8'))
kb.add_hotkey('ctrl+alt+8', paste, args=('8'))
kb.add_hotkey('ctrl+c+9', copy, args=('9'))
kb.add_hotkey('ctrl+alt+9', paste, args=('9'))

kb.wait()

