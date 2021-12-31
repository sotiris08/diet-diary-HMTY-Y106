#ProfileData
from ProfileDataClasses import *
import json

class ProfileData:
    "weightData.json", "hydrationData.json", "bmiData.json"
    weightData = None    #WeightHistory
    hydrationData = None  #HydrationHistory
    bmiData = None    #BMIHistory
    height = None
    
    def init():
        f = open("./data/height.txt", "r", encoding="utf-8")
        ProfileData.height = f.read()
        f.close()
        ProfileData.load_profile_data()
        
    def load_profile_data():
        with open("./data/weightData.json", "r", encoding="utf-8") as f:
            weight_his = f.read()
            if weight_his != "":
                ProfileData.weightData = WeightHistory(json.loads(weight_his))
        with open("./data/hydrationData.json", "r", encoding="utf-8") as f:
            hyd_his = f.read()
            if hyd_his != "":
                ProfileData.hydrationData = HydrationHistory(json.loads(hyd_his))
        with open("./data/bmiData.json", "r", encoding="utf-8") as f:
            bmi_his = f.read()
            if bmi_his !="":
                ProfileData.bmiData = BMIHistory(json.loads(bmi_his))

    def change_height(new_height: int):
        with open("./data/height.txt", "w", encoding="utf-8") as f:
            f.write(f"{new_height}")
        ProfileData.height = new_height

    def get_height():
        return ProfileData.height

    def isFirstTime():
        if ProfileData.weightData == None and ProfileData.hydrationData == None and ProfileData.bmiData == None:
            return True
        else:
            return False