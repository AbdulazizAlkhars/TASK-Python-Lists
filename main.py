# check_length_is_odd(numbers):
# - receives a list of `numbers`
# - returns true if the list has an odd number of elements
# - returns false otherwise
#
# e.g.
# check_length_is_odd([1, 2, 3]) -> true
# check_length_is_odd([1, 2, 3, 4]) -> false

numbersList = [1, 2, 3, 4, 5, 6, 7]


def check_length_is_odd(numbers):
    # Your code here
    if len(numbers) % 2 != 0:
        checkingOdd = True
        return checkingOdd
    else:
        checkingOdd = False
        return checkingOdd

    ...


print(check_length_is_odd(numbersList))

# check_length_is_even(numbers):
# - receives a list of `numbers`
# - returns true if the list has an even number of elements
# - returns false otherwise
# e.g.
# check_length_is_even([1, 2, 3]) -> false
# check_length_is_even([1, 2, 3, 4]) -> true


def check_length_is_even(numbers):
    # Your code here
    if len(numbers) % 2 == 0:
        checkingEven = True
        return checkingEven
    else:
        checkingEven = False
        return checkingEven
    ...


print(check_length_is_even(numbersList))

# add_mohammad_to_list(instructors):
# - receives a list of `instructors`
# - returns a new list that's a copy of list `instructors` with additional string "Mohammad"
# e.g.
# add_mohammad_to_list(["Mshary", "Hasan"]) -> ["Mshary", "Hasan", "Mohammad"]

instructors = ["Aziz", "Mansour"]


def add_mohammad_to_list(instructors):
    # Your code here
    instructors.append("Mohammad")
    return instructors
    ...


print(add_mohammad_to_list(instructors))

# eliminate_team(teams):
# - receives a list of `teams`
# - removes the last element from the list and returns it
# e.g.
# eliminate_team(["Brazil", "Germany", "Italy"]) -> "Italy"

teams = ["Brazil", "Germany", "Italy"]


def eliminate_team(teams):
    # Your code here
    lastItem = teams.pop()

    return lastItem
    ...


print(eliminate_team(teams))

# second_half_of_list_if_even(fruits):
# - receives a list of `fruits`
# - returns a new list that's the second half of the original list if it has an even number of elements
# - returns an empty list if it has an odd number of elements
# e.g.
# second_half_of_list_if_even(["apple", "orange", "banana", "kiwi"]) -> ["banana", "kiwi"]
# second_half_of_list_if_even(["apple", "orange", "banana", "kiwi", "blueberry"]) -> []

fruits = ["apple", "orange", "banana", "kiwi", "blueberry"]


def second_half_of_list_if_even(fruits):
    # Your code here
    newFruit = []
    if len(fruits) % 2 == 0:
        newFruit = list(fruits[int(len(fruits)/2):])
        return newFruit
    else:
        return newFruit
    ...


print(second_half_of_list_if_even(fruits))
