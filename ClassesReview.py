def create_dict(CampObject):
    letters = {}
    if CampObject.name in letters:
        val = letters.get(CampObject.name)
        print(val)
        letters[CampObject.name] = val.append(CampObject)
    else:
        letters[CampObject.name] = CampObject
    return letters


class Camp:
    def __init__(self, CampID, name, min_age, max_age, price):
        self.__CampID = CampID
        self.name = name
        self.price = price
        self.min_age = min_age
        self.max_age = max_age

    def get_id(self):
        return self.__CampID

    def about(self):
        return "{} camp costs {}$ per week".format(self.name, self.price)

    def change_price(self, price):
        self.price = price

    def set_ages(self, min_age, max_age):

        if max_age > min_age:
            self.min_age = min_age
            self.max_age = max_age
        else:
            print("Minimum age must be less than maximum age")


c1 = Camp(1, "Archery", 23, 23, 9000)
c2 = Camp(1, "Art", 23, 23, 4000)

# x = (c1.make_dict(c1))
# c2.make_dict(c2)
# print(x)
# z = x.get("Archery")
# y = [z.min_age, z.price, z.max_age]
# print(y)

c3 = Camp(1, "Soccer", 23, 23, 5000)
c4 = Camp(1, "Soccer", 2344, 2344, 500055)

print(create_dict(c3))

# print(c3.make_dict_list_of_objects(c3))


# print(c1.about())
# print(c1.get_id())
# c1.set_ages(300, 2)
# print(c1.min_age, c1.max_age)
