# meals = [
#         {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#         {"title": "Italian salad with fusilli and ham", "kcal": 320},
#         {"title": "Bulgur with vegetables", "kcal": 350},
#         {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#         {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
print(sum([meals[x]['kcal'] for x in range(len(meals))]))
