from Gui import Gui as Gui
from ProfileData import ProfileData as ProfileData

class Client:
    Gui = Gui
    ProfileData = ProfileData

    def init():
        Client.ProfileData.init()
        Client.Gui.beginView(Client.Gui.StartView)