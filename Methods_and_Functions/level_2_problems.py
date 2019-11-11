def has_33(nums):
    prev = None
    for a in nums:
        print(f"a={a}, prev={prev}")
        if a == 3 and prev == 3:
            return True
        prev = a
    return False


# print(has_33([1,2,3,3,6,7,4,3,6]))


def paper_doll(text):
    result = ""
    for a in text:
        result = result + a * 3
        print(result)
    return result


# print(paper_doll("NapIS"))

def blackjack(a, b, c):
    mysum = a + b + c
    if mysum <= 21:
        return mysum
    elif mysum - 10 <= 21:
        return mysum - 10
    else:
        return "BUST"


# print(blackjack(19,6,7))

def summer_69(arr):
    should_add = True
    myres = 0
    for a in arr:
        if a == 6:
            should_add = False
        if should_add:
            myres = myres + a
        if a == 9:
            should_add = True
    return (myres)


# print(summer_69([1, 2, 4, 6, 7, 5, 9, 4, 11, 6, 9]))


def spy_game(nums):
    zero_counter = 0
    for a in nums:
        if a == 0:
            zero_counter = zero_counter + 1
        if a == 7 and zero_counter >= 2:
            return True
    return False


print(spy_game([1, 9, 0, 8, 7]))
