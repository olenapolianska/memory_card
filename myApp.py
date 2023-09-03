from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
import json

player = {}

def write():
    global player
    with open("playerData.json", "w", encoding="utf-8") as file:
        json.dump(player, file)

def read():
    global player
    with open("playerData.json", "r", encoding="utf-8") as file:
        player = json.load(file)
read()
class MainScreen(Screen):
    def __init__(self, name):
        super().__init__(name=name)  # ім'я екрана має передаватися конструктору класу Screen
        self.ids.clickScore.text = str(player["score"])

    def clickBtn(self):
        read()
        player["score"] += player["clickPower"]
        self.ids.clickScore.text = str(player["score"])
        write()
        self.ids.ball.size_hint = (0.7, 0.7)


    def clickend(self):
        write()
        self.ids.ball.size_hint = (0.4, 0.4)
    def on_enter(self):
        read()
        self.ids.clickScore.text = str(player["score"])
        write()


    def clickShopBtn(self):
        self.manager.current = 'shop'



class Shop(Screen):
    def __init__(self, name):
        super().__init__(name=name)

    def buyItem(self, price, power):
        read()
        #якщо хватає грошей
        player["score"] -= price
        player["clickPower"] += power
        write()

    def backToGame(self):
        self.manager.current = 'name'



class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(MainScreen("name"))
        sm.add_widget(Shop("shop"))
        return sm

app = MyApp()
app.run()