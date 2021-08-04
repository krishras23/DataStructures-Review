# Initialize  a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weather = [60, 23, 10]
people = list(("andrew", "bob", "joe"))


# return true if one item is common
def common_member(list1, list2):
    for z in list1:
        for y in list2:
            if z == y:
                print("True")


# print(len(numbers))
# print(type(numbers))


sorted_list = sorted(numbers, reverse=True)

for x in sorted_list:
    print(x)

for x in people:
    print(x)


# return only even numbers
def get_even(given_list):
    even_numbers = []
    for x in given_list:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers


print(get_even(numbers))

# index the list
print(numbers[2])
print(numbers[-1])
print(numbers[3:])

# starts at 2 (included) and ends at 4 (not included)
print(numbers[2:4])

# print every 3rd element in a list
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 3


# multiply a list

def multiply_list(some_list):
    ans = 1
    for x in some_list:
        ans = x * ans
    return ans


print(multiply_list(numbers))

