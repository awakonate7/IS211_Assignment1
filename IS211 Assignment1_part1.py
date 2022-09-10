def list_divide(numbers, divide):

    """
    The function return the number of elements in the numbers list that are divisibleby divide
    """
class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):

def test_list_divide():
    counter = 0

    """
    Test listDivide
    """

    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5

if __name__ == "__main__":
		    testListDivide()

testListDivide()
    if isinstance(numbers, list) == False:
        raise ListDivideException("This is not a list of numbers")
    elif isinstance(numbers, str) == True:
        raise ListDivideException("This is not a list of numbers")

    try:
        for i in numbers:
            if i % divide == 0:
                counter += 1
    except ListDivideException:
        pass

    print(counter)

if __name__ == "__main__":
    listDivide([1, 2, 3, 4, 5])
    listDivide([2, 4, 6, 8, 10])
    listDivide([30, 54, 63, 98, 100], divide=10)
    listDivide([])
    listDivide([1, 2, 3, 4, 5], 1)
