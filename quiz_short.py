import tkinter as tk
import random 

questions = [
    {
        'текст вопроса': 'Какой из этих типов данных изменяемый?',
        'варианты ответов': ['tuple', 'list', 'str', 'int'],
        'ответ': 'list'
    },
    {   
        'текст вопроса': 'Какой оператор перемножает числа в пайтон?',
        'варианты ответов': ['x', '//', '*', '**'],
        'ответ': '*'    
    },
    {   
        'текст вопроса': '?',
        'варианты ответов': ['stop', 'break', '', ''],
        'ответ': 'break'
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

        self.question_number = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_questions = None

        self.start()
        self.window.mainloop()

    def start(self):
        self.question_index = 0
        self.correct_index = 0
        self.incorrect_answers = 0
        if self.shuffle_questions:
            random.shuffle(questions)


App(shuffle_questions=True)
# self.question_frame['bg'] = 'coral'