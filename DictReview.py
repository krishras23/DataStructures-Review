# dictionaries

test = {"key1": "value1", "key2": "value2", "key3": "value3"}

person = {"name": "john", "age": 23}

# prints all keys one by one
for x in test:
    print(x)

for x in test.values():
    print(x)

for y in test:
    print(test[y])

print(len(test))

# update function changes the dictionary
test.update({"key4": "value4"})

print(test)

# assign a new key to a specific value
test["key5"] = "value5"

print(test)

person["favorite_food"] = "pizza"
person.update({"gender": "male"})

print(person)

person["favorite_food"] = "pasta"
person.update({"age": "24"})

print(person.get("age"))

# get values

y = person.get("favorite_food")
z = person["gender"]

print(y)
print(z)

person.pop("gender")
print(person)

camp_dict = {}


def camp(name, price):
    camp_dict.update({name: price})


camp("Skateboarding Camp", "400")
camp("Kids Camp", "200")
camp("Krish's Camp", "100")

print(camp_dict)

krish_grades = {"name": "Krish Rastogi",
                "assignment": [80, 50, 40, 20],
                "test": [75, 90, 85, 23, 21],
                "lab": [78.20, 77.20]
                }

tests_list = krish_grades.get("test")


def add_list(given_list):
    counter = 0
    for x in given_list:
        counter = counter + x
    return counter


print(add_list(tests_list))


def finding_average(given_list):
    total_sum = 0
    for items in given_list:
        total_sum = total_sum + items
    average = total_sum/len(given_list)
    return average


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(finding_average(my_list))