from Gui import Gui as Gui
from ProfileData import ProfileData as ProfileData
from FoodData import FoodData as FoodData

class Client:
    Gui = Gui
    FoodData = FoodData
    ProfileData = ProfileData

    def init():
        Client.FoodData.init()
        Client.ProfileData.init()
        #Client.Gui.beginView(Client.Gui.StartView)