import random
import PySimpleGUI as vt
import os


class PassGen:
    def __init__(self):
        vt.theme('Dark Blue')
        layout = [
            [vt.Text('Gerador de código de acesso ao RBOT!')],
            [vt.Text('Quantidade de caracteres:'), vt.Combo(values=list(range(11)), key= 'total_chars', default_value=1)],
            [vt.Output(size=(29, 2))],
            [vt.Button('GERAR', button_color="green")]
        ]
        self.janela = vt.Window('CÓD GENERATOR', element_justification='center', layout=layout)
    def Iniciar (self):
        while True:
            evento, valores = self.janela.read()
            if evento == vt.WIN_CLOSED:
               break
            if evento == 'GERAR':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)

    def gerar_senha(self,valores):
        char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

gen = PassGen ()
gen.Iniciar()