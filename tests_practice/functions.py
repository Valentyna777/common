import math
import string


def task_1(list_1, list_2):
    """
    returns a list that contains only
    the elements that are common between
    the lists (without duplicates)
    """
    result_list = list(set(i for i in list_1 if i in list_2))
    return result_list


def task_2(string_1):
    """
    returns the number of times that
    the letter “a” appears anywhere
    in the given string
    """
    return string_1.count('a')


def task_3(num):
    """
    checks if a given positive
    integer is a power of three
    """
    x = math.log(num, 3)
    return int(x) == x


def task_4(num):
    """
    adds the digits of a positive
    integer repeatedly until the
    result has a single digit
    """
    while True:
        digit_count = sum(int(i) for i in str(num))
        if len(str(digit_count)) == 1:
            return digit_count
        num = digit_count


def task_5(list_1):
    """
    pushes all zeros to the end of a list.
    """
    count = 0
    while 0 in list_1:
        list_1.remove(0)
        count += 1
    for j in range(count):
        list_1.append(j)
    return list_1


def task_6(list_1):
    """
    checks a sequence of numbers is
    an arithmetic progression or not
    """
    if len(list_1) <= 2:
        return False
    dif = list_1[1] - list_1[0]
    ind = 1
    while ind < len(list_1) - 1:
        if list_1[ind + 1] - list_1[ind] != dif:
            return False
        ind += 1
    return True


def task_7(list_1):
    """
    finds the number in a list
    that doesn't occur twice.
    """
    new_list = []
    for i in list_1:
        if list_1.count(i) == 1:
            new_list.append(i)
    return new_list


def task_8(list_1):
    """
    finds a missing number from a list
    """
    for i in range(list_1[0], list_1[-1]):
        if i not in list_1:
            return i


def task_9(list_1):
    """
    counts the elements in a list
    until an element is a tuple.
    """
    count = 0
    for i in list_1:
        if isinstance(i, tuple):
            break
        count += 1
    return count


def task_10(my_string):
    """
    Write a program that will take the str parameter 
    being passed and return the string in reversed order.
    """
    return my_string[::-1]


def task_11(num):
    """
    takes the num parameter being passed
    and returns the number of hours and minutes
    the parameter converts to (ie. if num = 63
    then the output should be 1:3)
    """
    hours = num // 60
    minutes = num % 60
    time = f"{hours}:{minutes}"
    return time


def task_12(my_string):
    """
    takes the parameter being passed and returns
    the largest word in the string. If there are
    two or more words that are the same length,
    returns the first word from the string with
    that length. It ignores punctuation.
    """
    my_list = [i.strip(string.punctuation) for i in my_string.split()]
    largest = my_list[0]
    for i in my_list:
        if len(i) > len(largest):
            largest = i
        else:
            continue
        return largest


def task_13():
    """
    asks the user for a long string containing multiple words and
    prints back to the user the same string, except with the words
    in backwards order.
    """
    input_string = input('Write a sentence: ')
    list_1 = input_string.split()
    list_1.reverse()
    new_string = ' '.join(list_1)
    return new_string


def task_14():
    """asks the user how many Fibonnaci numbers
    to generate and then generates them"""
    input_num = input('How many numbers of Fibonacci sequence would you like to generate?')
    l = []
    a = 0
    b = 1
    for i in range(int(input_num)):
        a, b = b, a + b
        l.append(a)
    return l


def task_15(input_list):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write
    one line of Python that takes this list a and makes
    a new list that has only the even elements of this
    list in it.
    """
    return [i for i in input_list if i % 2 == 0]


def task_16(input_number):
    """
    adds up all the numbers from 1 to input number.
    For example: if the input is 4 then your program
    should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    return sum([i for i in range(int(input_number)+1)])


def task_17(num):
    """
    takes the parameter being passed
    and returns the factorial of it
    """
    if num == 0:
        return 1
    else:
        return num * task_17(num - 1)


def task_18(str_1):
    """
    take the str parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the alphabet
    (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
    (a, e, i, o, u) and finally return this modified string.
    """
    l1 = [chr(ord(i) + 1) for i in str_1]
    l2 = []
    for i in l1:
        if i in 'aeiou':
            l2.append(i.upper())
        else:
            l2.append(i)
    return ''.join(l2)


def task_19(str_1):
    """
    Write a program that will take the str string parameter being passed and return
    the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    """
    return ''.join(sorted(str_1))


def task_20(num_1, num_2):
    """
    Write a program that will take both parameters being passed and return the true if num2
    is greater than num1, otherwise return the false. If the parameter values are equal to
    each other then return the string -1
    """
    if num_2 > num_1:
        return True
    elif num_2 < num_1:
        return False
    else:
        return '-1'


