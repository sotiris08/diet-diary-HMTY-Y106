#ProfileData Classes Dimitris Sgourakis
        
class WeightHistory:

    def __init__(self, date: str, weight: float):   #ημερομηνία, βάρος(σε kg)
        self.date = date
        self.weight = weight

    def __str__(self):
        return f"{self.date},{self.weight}"


class HydrationHistory:

    def __init__(self, date: str, hydration: int):  #ημερομηνία, βαθμός ενυδάτωσης
        self.date = date
        self.hydration = hydration

    def __str__(self):
        return f"{self.date},{self.hydration}"


class BMIHistory:

    def __init__(self, date: str, bmi: float):  #ημερομηνία, BMI
        self.date = date
        self.bmi = bmi

    def __str__(self):
        return f"{self.date},{self.bmi}"


class FoodWeekHistory:

    def __init__(self, date: str, week_day: str, foodtypes: list):   #ημερομηνία, μέρα της εβδομάδας, είδος φαγητού
        self.date = date
        self.week_day = week_day
        self.foodtypes = foodtypes      #self.foodtypes: list object with FoodData elements
        self.food_number = len(self.foodtypes)      #αριθμός ειδών φαγητού(ο αριθμός αυξάνεται ακόμη και αν έχει καταναλωθεί το ίδιο είδος φαγητού)

    def __str__(self):
        return f"{self.date},{self.week_day},{self.food_number},{self.foodtypes}"
