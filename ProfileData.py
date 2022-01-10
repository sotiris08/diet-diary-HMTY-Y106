#ProfileData
from ProfileDataClasses import *
import json

class ProfileData:
    "weightData.json", "hydrationData.json", "bmiData.json"
    weightData = None    #WeightHistory
    hydrationData = None  #HydrationHistory
    bmiData = None    #BMIHistory
    calpDay = None
    height = None
    gender=None
    
    def init():
        f = open("./data/height.txt", "r", encoding="utf-8")
        ProfileData.height = f.read()
        f.close()
        f = open("./data/calpday.txt", "r", encoding="utf-8")
        ProfileData.calpDay = f.read()
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

    def change_calpDay(new_calpDay: int):
        with open("./data/calpday.txt", "w", encoding="utf-8") as f:
            f.write(f"{new_calpDay}")
        ProfileData.calpDay = new_calpDay

    def change_gender(new_gender):
        with open("./data/gender.txt","w",encoding="utf-8") as f:
            f.write(f"{new_gender}")
        ProfileData.gender=new_gender
       
    def get_height():
        return ProfileData.height

    def get_calpDay():
        return ProfileData.calpDay

    def get_gender():
        return ProfileData.gender

    def isFirstTime():
        if (not ProfileData.weightData.hasData()) and (not ProfileData.bmiData.hasData()):
            return True
        else:
            return False
