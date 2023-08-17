from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import random

class ui(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.root = Builder.load_file('design.kv')
        return ui()
    
    def fun_stone(self):
        self.player = 1
        self.funRamdom()
    def fun_paper(self):
        self.player = 2
        self.funRamdom()
    def fun_scissors(self):
        self.player = 3
        self.funRamdom()

    def funRamdom(self): 
        result = ''
        machine = 0
        player = self.player
        answer_machine = self.root.ids.answer_machine
        scoreMachine = self.root.ids.score
        scorePlayer = self.root.ids
        ScoreMachine = 0
        ScorePlayer = 0

        ramdom = random.randint(1, 3)
        if ramdom == 1:
            machine = 1
            resultMachine = 'Piedra'
        elif ramdom == 2:
            machine = 2
            resultMachine = 'Papel'
        elif ramdom == 3:
            machine = 3
            resultMachine = 'Tijera'
        print("numero ramdom " + str(ramdom))

        if machine == player: 
            result = 'Empate'       
        elif machine == 1 and player == 2: 
            result = 'Gana Jugador'
            scorePlayer += 2
        elif machine == 2 and player == 3:
            result = 'Gana Jugador'
            scorePlayer += 2
        elif machine == 3 and player == 1:
            result = 'Gana Jugador'
            scorePlayer += 2     
        elif player == 1 and machine == 2: 
            result = 'Gana Maquina'
            scoreMachine += 2
        elif player == 2 and machine == 3:
            result = 'Gana Maquina'
            scoreMachine += 2
        elif player == 3 and machine == 1:
            result = 'Gana Maquina'
            scoreMachine += 2
        if scoreMachine >= 10 or scorePlayer >=10:
            result = 'Fin del Juego'

        answer_machine.text = "La Maquina Saco: " + str(resultMachine) + "\n" +  str(result)
        
        
if __name__ == "__main__":
    MainApp().run()