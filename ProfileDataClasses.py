#ProfileData Classes
from DateNotFoundError import DateNotFoundError
        
class WeightHistory:

    def __init__(self, data):   #data => το λεξικό από το αρχείο json
        self.history = data

    def hasData(self):
        '''Επιστρέφει True αν υπάρχουν αποθηκευμένα δεδομένα'''
        if len(self.history) == 0: return False
        else: return True

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
        '''Αλλαγή αποθηκευμένων δεδομένων για μια συγκεκριμένη ημέρα'''
        self.history[date] = weight
        WeightHistory.saveWeightHistory(self.history)

    def deleteWeightForDay(self, date):
        '''Διαγράφει το βάρος της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            WeightHistory.saveWeightHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveWeightHistory(data):
        '''Αποθήκευση'''
        data = getValidJSON(data)
        f = open('./data/weightData.json', "w", encoding='utf-8')
        f.write(data)
        f.close()
    #def __str__(self):
    #    return f"{self.date},{self.weight}"


class HydrationHistory:

    def __init__(self, data):  #data => το λεξικό από το αρχείο json
        self.history = data

    def hasData(self):
        '''Επιστρέφει True αν υπάρχουν αποθηκευμένα δεδομένα'''
        if len(self.history) == 0: return False
        else: return True

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
        '''Αλλαγή αποθηκευμένων δεδομένων για μια συγκεκριμένη ημέρα'''
        self.history[date] = hydration
        HydrationHistory.saveHydrationHistory(self.history)

    def deleteHydrationForDay(self, date):
        '''Διαγράφει το hydration της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            HydrationHistory.saveHydrationHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveHydrationHistory(data):
        '''Αποθήκευση'''
        data = getValidJSON(data)
        f = open('./data/hydrationData.json', 'w', encoding='utf-8')
        f.write(data)
        f.close()

    #def __str__(self):
    #    return f"{self.date},{self.hydration}"


class BMIHistory:

    def __init__(self, data):  #data => το λεξικό από το αρχείο json
        self.history = data

    def hasData(self):
        '''Επιστρέφει True αν υπάρχουν αποθηκευμένα δεδομένα'''
        if len(self.history) == 0: return False
        else: return True

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
        '''Αλλαγή αποθηκευμένων δεδομένων για μια συγκεκριμένη ημέρα'''
        self.history[date] = BMI
        BMIHistory.saveBMIHistory(self.history)

    def deleteBMIForDay(self, date):
        '''Διαγράφει το BMI της date. Μπορεί να δόσει DateNotFoundError αν η ημέρα δεν υπάρχει στο λεξικό'''
        try:
            del self.history[date]
            BMIHistory.saveBMIHistory(self.history)
        except KeyError: raise DateNotFoundError('Invalid Date')

    def saveBMIHistory(data):
        '''Αποθήκευση'''
        data = getValidJSON(data)
        f = open('./data/bmiData.json', 'w', encoding='utf-8')
        f.write(data)
        f.close()

    #def __str__(self):
    #    return f"{self.date},{self.bmi}"

def getValidJSON(data):
    data = str(data)
    i = 0
    while i <= len(data):
        data = data.replace("'",'"')
        i += 1
    return data