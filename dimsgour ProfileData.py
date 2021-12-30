#ProfileData
from dimsgourProfileDataClasses import *

class ProfileData:
    "weightData.txt", "hydrationData.txt", "bmiData.txt", "foodweekData.txt"
    weightData = {}    #{date : WeightHistory_obj}
    hydrationData = {}  #{date : HydrationHistory_obj}
    bmiData = {}    #{date : BMIHistory_obj}
    foodweekData = {}   #{date : FoodWeekHisotry_obj}
    
    def __init__(self):
        f = open("height.txt", "r", encoding="utf-8")
        self.height = f.read()
        f.close()

    def load_profile_data(self):
        with open("weightData.txt", "r", encoding="utf-8") as f:
            weight_his = f.read()
            if weight_his != "":
                for line in weight_his.split("\n"):
                    date, weight = line.split(",")
                    weight_obj = WeightHistory(date, weight)
                    ProfileData.weightData[date] = weight_obj
            else: pass
        with open("hydrationData.txt", "r", encoding="utf-8") as f:
            hyd_his = f.read()
            if hyd_his != "":
                for line in hyd_his.split("\n"):
                    date, hydration = line.split(",")
                    hydration_obj = HydrationHistory(date, hydration)
                    ProfileData.hydrationData[date] = hydration_obj
            else: pass
        with open("bmiData.txt", "r", encoding="utf-8") as f:
            bmi_his = f.read()
            if bmi_his !="":
                for line in bmi_his.split("\n"):
                    date, bmi = line.split(",")
                    bmi_obj = BMIHistory(date, bmi)
                    ProfileData.bmiData[date] = bmi_obj
            else: pass
        with open("foodweekData.txt", "r", encoding="utf-8") as f:
            foodweek_his = f.read()
            if foodweek_his !="":
                for line in foodweek_his.split("\n"):
                    date, week_day, food_number, foodtypes = line.split(",", maxsplit=3)
                    food_number = int(food_number)
                    foodtypes = foodtypes.replace("[", "").replace("]", "").replace('"', '').replace("'", "")
                    foodtypes = list(foodtypes.split(", "))
                    foodweek_obj = FoodWeekHistory(date, week_day, foodtypes)
                    ProfileData.foodweekData[date] = foodweek_obj
            else: pass

    def change_height(self, new_height: int):
        with open("height.txt", "w", encoding="utf-8") as f:
            f.write(f"{new_height}")
        self.height = new_height

    def show_height(self):
        return self.height

    def del_weight_data(self, date: str):    #Διαγράφεται το βάρος μιας συγκεκριμένης ημερομηνίας
        try:
            del ProfileData.weightData[date]
            return True     #Επιστρέφει True και διαγράφει αν υπάρχει η ημερομηνία
        except KeyError: return False   #Επιστρέφει False αν δεν υπάρχει η ημερομηνία

    def del_hydration_data(self, date: str):     #Διαγράφεται η ενυδάτωση μιας συγκεκριμένης ημερομηνίας
        try:
            del ProfileData.hydrationData[date]
            return True
        except KeyError: return False

    def del_bmi_data(self, date: str):   #Διαγράφεται το bmi μιας συγκεκριμένης ημερομηνίας
        try:
            del ProfileData.bmiData[date]
            return True
        except KeyError: return False

    def del_foodweek_data(self, date: str):      ##Διαγράφεται το διατροφικό ιστορικό μιας συγκεκριμένης ημερομηνίας
        try:
            del ProfileData.foodweekData[date]
            return True
        except KeyError: return False

    def add_weight_data(self, date: str, weight: float):    #Δημιουργία δεδομένων βάρους για μια συγκεκριμένη ημερομηνία
        if date in ProfileData.weightData:
            return False    #Επιστρέφει False αν υπάρχει η ημερομηνία
        elif date not in ProfileData.weightData:
            weight_obj = WeightHistory(date, weight)
            ProfileData.weightData[date] = weight_obj
            return True     #Επιστρέφει True και δημιουργεί αν δεν υπάρχει η ημερομηνία

    def add_hydration_data(self, date: str, hydration: int):    #Δημιουργία δεδομένων ενυδάτωσης για μια συγκεκριμένη ημερομηνία
        if date in ProfileData.hydrationData:
            return False
        elif date not in ProfileData.hydrationData:
            hydration_obj = HydrationHistory(date, hydration)
            ProfileData.hydrationData[date] = hydration_obj
            return True

    def add_bmi_data(self, date: str, bmi: float):      #Δημιουργία δεδομένων BMI για μια συγκεκριμένη ημερομηνία
        if date in ProfileData.bmiData:
            return False
        elif date not in ProfileData.bmiData:
            bmi_obj = BMIHistory(date, bmi)
            ProfileData.bmiData[date] = bmi_obj
            return True

    def add_foodweek_data(self, date: str, week_day: str, foodtypes: list):      #Δημιουργία δεδομένων foodweek για μια συγκεκριμένη ημερομηνία
        if date in ProfileData.foodweekData:
            return False
        elif date not in ProfileData.foodweekData:
            foodweek_obj = FoodWeekHistory(date, week_day, foodtypes)
            ProfileData.foodweekData[date] = foodweek_obj
            return True

    def show_weight_data(self, date: str):      #Επιστρέφει το βάρος μιας συγκεκριμένης ημερομηνίας
        try:
            d, weight = ProfileData.weightData[date].split(",")
            return weight
        except KeyError: return False       #Αν η ημερομηνία δεν υπάρχει επιστρέφει False

    def show_hydration_data(self, date: str):       ##Επιστρέφει την ενυδάτωση μιας συγκεκριμένης ημερομηνίας
        try:
            d, hydration = ProfileData.hydrationData[date].split(",")
            return hydration
        except KeyError: return False

    def show_bmi_data(self, date: str):     #Επιστρέφει το BMI μιας συγκεκριμένης ημερομηνίας
        try:
            d, bmi = ProfileData.bmiData[date].split(",")
            return bmi
        except KeyError: return False

    def show_fooodweek_data(self, date: str):       #Επιστρέφει το foodweek μιας συγκεκριμένης ημερομηνίας
        try:
            d, foodweek = ProfileData.foodweekData[date].split(",", maxsplit=1)
            return foodweek
        except KeyError: return False

    def store_profile_data(self):
        with open("weightData.txt", "w", encoding="utf-8") as f:
            for weight_obj in ProfileData.weightData:
                f.write(f"{ProfileData.weightData[weight_obj]}\n")
        with open("hydrationData.txt", "w", encoding="utf-8") as f:
            for hydration_obj in ProfileData.hydrationData:
                f.write(f"{ProfileData.hydrationData[hydration_obj]}\n")
        with open("bmiData.txt", "w", encoding="utf-8") as f:
            for bmi_obj in ProfileData.bmiData:
                f.write(f"{ProfileData.bmiData[bmi_obj]}\n")
        with open("foodweekData.txt", "w", encoding="utf-8") as f:
            for foodweek_obj in ProfileData.foodweekData:
                f.write(f"{ProfileData.foodweekData[foodweek_obj]}\n")
