from kivy.app import *
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.boxlayout import *
from kivy.uix.screenmanager import *
from instructions import *
from ruffier import *
from kivy.core.window import Window
from kivy.clock import Clock
from seconds import *
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.animation import Animation

age = 0
name = ''
p1,p2,p3 = 0,0,0
back = (1, 0.8, 0.1, 0.28)

Window.clearcolor = back
w_width = Window.width

w_width = w_width / 1920
font = str(20 * w_width)
font = font + 'px'
font = '20px'

btn_color = (0.99, 0.6, 0.01, 0.28)

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class FirstScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        
        
        vl = BoxLayout(orientation = 'vertical')
        hl1 = BoxLayout(size_hint_y = (1,None), height = '50px')
        hl2 = BoxLayout(size_hint_y = (1,None), height = '50px')
        
        txt = Label(text = txt_instruction,font_size=font)
        txt_name = Label(text = "Enter a name:",font_size=font)
        txt_age = Label(text = "Enter a age:",font_size=font)
        
        self.input_name = TextInput(hint_text = "Enter a name", multiline = False,font_size=font)
        self.input_age = TextInput(hint_text = "Enter a age", multiline = False,font_size=font)
        
        btn = Button(text = 'Next',size_hint_y = (1,None), height = '50px',font_size=font)
        btn.on_press = self.next
        btn.background_color = btn_color

        vl.add_widget(txt)

        hl1.add_widget(txt_name)
        hl1.add_widget(self.input_name)

        hl2.add_widget(txt_age)
        hl2.add_widget(self.input_age)

        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(btn)

        self.add_widget(vl)

    def next(self):
        global name
        global age
        name = self.input_name.text
        age = check_int(self.input_age.text)
        if age == False or age < 7:
            age = 0
            self.input_age.text = str(age)
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = "second"

class SecondScr(Screen):
    def __init__(self,**kwargs):

        self.next_screen = False

        self.lbl_sec = Seconds(1)
        self.lbl_sec.bind(done = self.sec_finished)
    
        super().__init__(**kwargs)

        vl = BoxLayout(orientation = 'vertical')
        hl = BoxLayout(size_hint_y = (1,None), height = '50px')

        txt = Label(text = txt_test1,font_size=font)
        txt_pulse = Label(text = "Count a pulse:",font_size=font)

        self.input_pulse = TextInput(hint_text= "Enter a pulse", multiline = False,font_size=font)
        self.input_pulse.set_disabled(True)

        self.btn = Button(text = 'Next',size_hint_y = (1,None), height = '50px',font_size=font)
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        vl.add_widget(txt)

        hl.add_widget(txt_pulse)
        hl.add_widget(self.input_pulse)

        vl.add_widget(hl)

        vl.add_widget(self.lbl_sec)

        vl.add_widget(self.btn)

        self.add_widget(vl)

    
    def sec_finished(self, *args):
        self.next_screen  = True
        self.input_pulse.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'
    
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.input_pulse.text)
            if p1 == False:
                p1 = 0
                self.input_pulse.text = str(p1)
            else:
                self.manager.current = "third"
        

class ThirdScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        vl = BoxLayout(orientation = 'vertical')

        txt = Label(text = txt_test2,font_size=font)

        self.anim = Animation(pos_hint={'center_x': 1.1}, background_color=(0.7,0.5,0.1,0.9), duration =2.0) + Animation(pos_hint={'center_x': 0.1},background_color = (0.35,0.7,0.2,0.7)) 

        self.btn = Button(text = 'Почати',size_hint = (None,None), pos_hint={'center_x': 0.5}, background_color=btn_color, height = '50px',width= '500px',font_size=font)
        self.btn.on_press = self.next

        vl.add_widget(txt)
        vl.add_widget(self.btn)

        self.add_widget(vl)
    
    def next(self):
        self.anim.start(self.btn)
        #self.btn.animation.on_complete = self.nextscreen

    def nextscreen(self):    
        self.manager.current = "fourth"

class FourthScr(Screen):
    def __init__(self,**kwargs):

        self.next_screen = False

        self.lbl_sec = Seconds(1)
        self.lbl_sec.bind(done = self.sec_finished)
        self.lbl1 = Label(text = 'Рахуйте пульс')
        self.stage = 0

        super().__init__(**kwargs)

        vl = BoxLayout(orientation = 'vertical')

        hl1 = BoxLayout(size_hint_y = (1,None), height = '50px')
        hl2 = BoxLayout(size_hint_y = (1,None), height = '50px')

        txt = Label(text = txt_test2)

        txt_first = Label(text = "First:",font_size=font)
        txt_second = Label(text = "Second:",font_size=font)

        self.input_first = TextInput(font_size=font)
        self.input_first.set_disabled(True)
        self.input_second = TextInput(font_size=font)
        self.input_second.set_disabled(True)

        self.btn = Button(text = 'Next',size_hint_y = (1,None), height = '50px',font_size=font)
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        vl.add_widget(txt)

        hl1.add_widget(txt_first)
        hl1.add_widget(self.input_first)

        hl2.add_widget(txt_second)
        hl2.add_widget(self.input_second)

        vl.add_widget(hl1)
        vl.add_widget(hl2)

        vl.add_widget(self.lbl_sec)
        vl.add_widget(self.lbl1)

        vl.add_widget(self.btn)

        self.add_widget(vl)

    def sec_finished(self,*args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = 'Відпочивайте'
                self.lbl_sec.restart(2)
                self.input_first.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text='Рахуйте пульс'
                self.lbl_sec.restart(1)
            elif self.stage == 2:
                self.input_second.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершити'
                self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        
        else:
            global p2
            global p3
            p2 = check_int(self.input_first.text)
            p3 = check_int(self.input_second.text)
            if p2 == False:
                p2 = 0
                self.input_first.text = str(p2)
            if p3 == False:
                p3 = 0
                self.input_second.text = str(p3) 
            else:
                self.manager.current = "fifth"

class FifthScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        vl = BoxLayout(orientation = 'vertical')

        self.txt = Label(text = '',font_size=font)

        vl.add_widget(self.txt)

        self.add_widget(vl)

        self.on_enter = self.before
    
    def before(self):
        self.txt.text = name+'\n'+txt_index+ str(ruffier_index(p1, p2, p3)) + '\n'+ txt_workheart + txt_res[ruffier_result(ruffier_index(p1, p2, p3),neud_level(age))]

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(FourthScr(name='fourth'))
        sm.add_widget(FifthScr(name='fifth'))
        return sm

MyApp().run()
