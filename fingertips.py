# given a list make it into a dictionary (index --> key, element --> value)

def convert(fruits_list):
    i = 0
    dict_fruits = {}
    for x in fruits_list:
        dict_fruits.update({i: fruits_list[i]})
        i = i + 1
    return dict_fruits


print(convert(["apple", "banana", "cherry", "avocado"]))

