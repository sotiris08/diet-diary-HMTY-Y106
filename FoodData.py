import json
import FoodNotFoundError
import FoodNameExistsError

class FoodData:
    foods = {}
    def __init__():
        f = open('./data/foods.json', 'r', encoding='utf-8')
        FoodData.foods = json.loads(f.read())
        f.close()

    def getFoodNames():
        result = []
        for item in FoodData.foods.keys(): result.append(item)
        return result

    def getFoodCal(foodName):
        try: return FoodData.foods[foodName]
        except KeyError: raise FoodNotFoundError()

    def createFood(name, cal):
        try:
            if(FoodData.getFoodCal(name)):
                raise FoodNameExistsError()
        except FoodNotFoundError:
            FoodData.foods[name] = cal
            f = open('./data/foods.json', 'w', encoding='utf-8')
            f.write(str(FoodData.foods))
            f.close()