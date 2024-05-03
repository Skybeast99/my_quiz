import tkinter as tk
import random
from datetime import datetime

questions = [
    {
        'вопрос': 'Какой из этих типов данных изменяемый?',
        'ответы': ['tuple', ' list', ' str ', ' int '],
        'ответ': 'list'
    },
    {   
        'вопрос': 'Какой оператор перемножает числа в пайтон?',
        'ответы': [' x ', ' //', ' * ', ' **'],
        'ответ': '*'
        
    },
    {   
        'вопрос': 'какой символ пишется в конце заголовка любого цикла',
        'ответы': [' []', ' * ', ' ()', ' : '],
        'ответ': ':'
    }
]


class App:
    '''Приложение'''
    def __init__(self, shuffle_questions=False) -> None:
        self.window = tk.Tk()
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        self.window.option_add('*Font', ('Consolas', 30))
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')

        self.main_frame = tk.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.question_index = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_questions = shuffle_questions

        self.start()
        self.window.mainloop()

    def clear_main_frame(self):
        '''удвляет виджеты из мэйн фрэйм'''
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def start(self) -> None:
        '''Начинает викторину'''
        self.time_1 = datetime.now()
        self.question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
            self.clear_main_frame()
        self.show_question()

    def show_question(self) -> None:
        '''Создает виджеты и наполняет их контентом вопроса'''
        question = questions[self.question_index]
        tk.Label(self.main_frame, text=question['вопрос']).pack(pady=(0, 30))
        buttons_frame = tk.Frame(self.main_frame)
        buttons_frame.pack()
        for answer in question['ответы']:
            tk.Button(
                buttons_frame,
                text=answer,
                command=lambda arg=answer: self.on_button(arg)
            ).pack(side='left', padx=20)

    def on_button(self, button_text: str) -> None:
        question = questions[self.question_index]
        if button_text == question['ответ']:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        self.clear_main_frame()

        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self) -> None:
        self.time_2 = datetime.now()
        self.delta_t = self.time_2 - self.time_1
        a = str(self.delta_t)
        s=a.split(':')
        sp=s[-1].split('.')
        s[-1]=sp[0]
        s.append(sp[-1])
        s=list(map(int,s))
        if s[-1]>=500:
            s[-1]=0
            if s[-2]<59:
                s[-2]+=1
            else:
                s[-2]=0
                if s[-3]<59:
                    s[-3]+=1
                else:
                    s[-3]=0
                    if s[-4]<22:
                        s[-4]+=1
                    else:
                        s[-4]=0
        else:
            s[-1]=0
        print(f'{s[0]}:{s[1]}:{s[2]}.{s[3]}')
        tk.Label(
            self.main_frame, text=f'время: {s[0]}:{s[1]}:{s[2]}.{s[3]}'
        ).pack()
        tk.Label(
            self.main_frame, text=f'верно: {self.correct_answers}'
        ).pack()
        tk.Label(
            self.main_frame, text=f'ошибок: {self.incorrect_answers}'
        ).pack()
        tk.Button(
            self.main_frame, text='заново', command=self.start
        ).pack(pady=(30, 0))
        # очистить main_frame


App(shuffle_questions=True)
