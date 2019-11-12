import sys
def flight(height,steps = 0):
    """
    flight() recursively calculates the path of a hailstone
    :param height: the height of the hailstone
    :return: a recursive call, which at the end returns
        the number of "steps" taken for the
        hailstone to reach a height of 1
    """

    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    if height <= 0:
        print('invalid')
        return sys.exit(0)
    # stops when it reachs height of 1 (the ground)
    elif height == 1:
        print(height)
        print('hail reaches ground')
        return steps
    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2
    if height % 2 == 0:
        steps += 1
        print(height)
        return flight(height // 2, steps)

    # if the current height is odd, multiply it by 3, then add 1
    if height % 2 != 0:
        steps += 1
        print(height)
        return flight((height * 3) + 1,steps )
    


if __name__ == '__main__':
    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    start_height = int(input(msg))

    # recursive call goes here
    # flight(start_height)
    print()
    print("It took" + " " + str(flight(start_height)) + " steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!")


# if __name__ == '__main__':
#     height = int(input("Please enter the starting height of the Hailstone? "))
#     if height==0:
#         print("Hailstone stopped at height 0")
#         exit()

#     while height >= 1:  
#         if height % 2 == 0:
#             height=int(height)//2
#             print("HailStone is currently at height ", height)
#         elif height==1:
#             print("Hailstone stopped at height 1")
#             exit()
#         else:
#             height =int(height)*3+1
#             print("HailStone is currently at height:",height)