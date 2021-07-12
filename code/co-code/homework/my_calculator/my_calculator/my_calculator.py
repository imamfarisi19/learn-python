import ui
import console

def on_textfield(sender):
		text_label = sender.superview['text_label']
		text_field = sender.superview['text_field']
		a = eval(text_field.text)
		text_label.text = str(a)

def on_button(sender):
		value = console.alert('guide/使用方法', '', 'English', '日本語', '中文', hide_cancel_button = False)
		if value == 1:
				console.alert('GUIDE', '+ : addition\n- : subtraction\n* : multiplication\n/ : division\n% : remainder\nYou can also use parentheses/brackets to indicate the part you want to culculate first.', hide_cancel_button = True)
		elif value == 2:
				console.alert('使用方法', '+ : 足し算\n- : 引き算\n* : 掛け算\n/ : 割り算\n% : 余りを求める\n小括弧を用いて先に計算したい部分を示すこともできます。', hide_cancel_button = True)
		elif value == 3:
				console.alert('使用方法', '+ : 加\n- : 減\n* : 乘\n/ : 除\n% : 剩余\n您可使用小括號並表示先計算的部分。', hide_cancel_button = True)
		


v = ui.load_view()
v.present('sheet')
