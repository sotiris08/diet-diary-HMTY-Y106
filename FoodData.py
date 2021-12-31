import json
from FoodNotFoundError import FoodNotFoundError
from FoodNameExistsError import FoodNameExistsError

class FoodData:
    foods = {}
    
    def init():
        f = open('./data/foods.json', 'r', encoding='utf-8')
        FoodData.foods = json.loads(f.read())
        f.close()

    def getFoodNames():
        result = []
        for item in FoodData.foods.keys(): result.append(item)
        return result

    def getFoodCal(foodName):
        try: 
            cal = FoodData.foods[foodName]
            return cal
        except KeyError: raise FoodNotFoundError('Wrong Food Name')

    def createFood(name, cal):
        try:
            if(FoodData.getFoodCal(name)):
                raise FoodNameExistsError('Food already exists')
        except FoodNotFoundError:
            FoodData.foods[name] = cal
            f = open('./data/foods.json', 'w', encoding='utf-8')
            newfoods = str(FoodData.foods)
            i = 0
            while i <= len(newfoods):
                newfoods = newfoods.replace("'",'"')
                i += 1
            f.write(newfoods)
            f.close()