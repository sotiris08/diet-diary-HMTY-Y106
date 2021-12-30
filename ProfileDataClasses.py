#ProfileData Classes
import DateNotFoundError
        
class WeightHistory:

    def __init__(self, data):   #data => το λεξικό από το αρχείο json
        self.history = data

    def getWeightForDays(self, dates):
        '''Δίνεις τις ημέρες που θες σε μορφή λίστας και σου επιστρέφει ένα λεξικό με κλειδιά της ημέρες και για τιμές το βάρος'''
        result = {}
        for item in dates:
            try:
                result[item] = self.history[item]
            except KeyError: 
                result[item] = None
        return result

    def updateWeightForDay(self, date, weight):
        self.history[date] = weight
        WeightHistory.saveWeightHistory(self.history)

    def deleteWeightForDay(self, date):
        '''Διαγράφει το βάρος της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            WeightHistory.saveWeightHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveWeightHistory(data):
        f = open('./data/weightData.json', "w", encoding='utf-8')
        f.write(data)
        f.close()
    #def __str__(self):
    #    return f"{self.date},{self.weight}"


class HydrationHistory:

    def __init__(self, data):  #data => το λεξικό από το αρχείο json
        self.history = data

    def getHydrationForDays(self, dates):
        '''Δίνεις τις ημέρες που θες σε μορφή λίστας και σου επιστρέφει ένα λεξικό με κλειδιά της ημέρες και για τιμές το hydration'''
        result = {}
        for item in dates:
            try:
                result[item] = self.history[item]
            except KeyError: 
                result[item] = None
        return result

    def updateHydrationForDay(self, date, hydration):
        self.history[date] = hydration
        HydrationHistory.saveHydrationHistory(self.history)

    def deleteHydrationForDay(self, date):
        '''Διαγράφει το hydration της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            HydrationHistory.saveHydrationHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveHydrationHistory(data):
        f = open('./data/hydrationData.json', 'w', encoding='utf-8')
        f.write(data)
        f.close()

    #def __str__(self):
    #    return f"{self.date},{self.hydration}"


class BMIHistory:

    def __init__(self, data):  #data => το λεξικό από το αρχείο json
        self.history = data

    def getBMIForDays(self, dates):
        '''Δίνεις τις ημέρες που θες σε μορφή λίστας και σου επιστρέφει ένα λεξικό με κλειδιά της ημέρες και για τιμές το BMI'''
        result = {}
        for item in dates:
            try:
                result[item] = self.history[item]
            except KeyError: 
                result[item] = None
        return result

    def updateBMIForDay(self, date, BMI):
        self.history[date] = BMI
        BMIHistory.saveBMIHistory(self.history)

    def deleteBMIForDay(self, date):
        '''Διαγράφει το BMI της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            BMIHistory.saveBMIHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveBMIHistory(data):
        f = open('./data/bmiData.json', 'w', encoding='utf-8')
        f.write(data)
        f.close()

    #def __str__(self):
    #    return f"{self.date},{self.bmi}"
