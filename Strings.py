def reverse_word(given_word):
    return given_word[::-1]


print(reverse_word("hello"))


def break_sentence(given_sentence):
    blank1 = given_sentence.find(" ")
    lastblank = given_sentence.rfind(" ")
    print(lastblank)
    word1 = given_sentence[0:blank1]
    print(word1)


break_sentence("This is a sentence ")


def is_palindrome(given_string):
    left = 0
    right = len(given_string) - 1

    while left < right:
        if given_string[left] != given_string[right]:
            return False
        left = left + 1
        right = right - 1
    return True


print(is_palindrome("racecar"))
print(is_palindrome("racecaxxr"))


def even_lenhgth_words(given_string):
    even_list = []
    beg = 0

    while True:
        end = given_string.find(" ", beg)
        if end == - 1:
            break
        word = given_string[beg:end]
        if len(word) % 2 == 0:
            even_list.append(word)
        beg = end + 1

    return even_list


# print(even_length_words("I am a case casa hjh lluuu "))


def even_length_words(sentence):
    word_list = sentence.split(" ")
    number_of_blanks = len(word_list) - 1
    beginning = 0
    list_of_words = []
    for i in range(3):
        first_blank = sentence.find(" ", beginning + 1)
        word = sentence[beginning:first_blank]
        list_of_words.append(word)
    beginning = beginning + first_blank
    return list_of_words


print(even_length_words("Integer well we are legends "))
