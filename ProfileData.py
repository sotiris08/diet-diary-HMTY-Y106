#ProfileData
from ProfileDataClasses import *
import json

class ProfileData:
    "weightData.json", "hydrationData.json", "bmiData.json", "foodweekData.txt"
    weightData = None    #WeightHistory
    hydrationData = None  #HydrationHistory
    bmiData = None    #BMIHistory
    foodweekData = None   #{date : FoodWeekHisotry_obj}
    height = None
    
    def __init__(self):
        f = open("./data/height.txt", "r", encoding="utf-8")
        ProfileData.height = f.read()
        f.close()

    def load_profile_data(self):
        with open("./data/weightData.json", "r", encoding="utf-8") as f:
            weight_his = f.read()
            if weight_his != "":
                ProfileData.weightData = WeightHistory(json.loads(weight_his))
            else: pass
        with open("./data/hydrationData.json", "r", encoding="utf-8") as f:
            hyd_his = f.read()
            if hyd_his != "":
                ProfileData.hydrationData = HydrationHistory(json.loads(hyd_his))
            else: pass
        with open("./data/bmiData.json", "r", encoding="utf-8") as f:
            bmi_his = f.read()
            if bmi_his !="":
                ProfileData.bmiData = BMIHistory(json.loads(bmi_his))
            else: pass
        with open("./data/foodweekData.txt", "r", encoding="utf-8") as f:
            foodweek_his = f.read()
            if foodweek_his !="":
                for line in foodweek_his.split("\n"):
                    date, week_day, food_number, foodtypes = line.split(",", maxsplit=3)
                    food_number = int(food_number)
                    foodtypes = foodtypes.replace("[", "").replace("]", "").replace('"', '').replace("'", "")
                    foodtypes = list(foodtypes.split(", "))
                    foodweek_obj = FoodDayHistory(date, week_day, foodtypes)
                    ProfileData.foodweekData[date] = foodweek_obj
            else: pass

    def change_height(self, new_height: int):
        with open("./data/height.txt", "w", encoding="utf-8") as f:
            f.write(f"{new_height}")
        self.height = new_height

    def get_height(self):
        return ProfileData.height

    def del_foodweek_data(self, date: str):      ##Διαγράφεται το διατροφικό ιστορικό μιας συγκεκριμένης ημερομηνίας
        try:
            del ProfileData.foodweekData[date]
            return True
        except KeyError: return False

    def add_foodweek_data(self, date: str, week_day: str, foodtypes: list):      #Δημιουργία δεδομένων foodweek για μια συγκεκριμένη ημερομηνία
        if date in ProfileData.foodweekData:
            return False
        elif date not in ProfileData.foodweekData:
            foodweek_obj = FoodDayHistory(date, week_day, foodtypes)
            ProfileData.foodweekData[date] = foodweek_obj
            return True

    def show_fooodweek_data(self, date: str):       #Επιστρέφει το foodweek μιας συγκεκριμένης ημερομηνίας
        try:
            d, foodweek = ProfileData.foodweekData[date].split(",", maxsplit=1)
            return foodweek
        except KeyError: return False

    def store_profile_data(self):
        with open("./data/foodweekData.txt", "w", encoding="utf-8") as f:
            for foodweek_obj in ProfileData.foodweekData:
                f.write(f"{ProfileData.foodweekData[foodweek_obj]}\n")
