import sys
# def Integer_Division(a,b):
    # divide = a % b
    # count = 0
    # if divide != 0:
    #     count +=1
    #     return Integer_Division(a,b), 
    # elif divide == 0:
    #     return count
def Integer_Division(a,b,count = 0):
    
    if a < b:
        return count
    else:
        count += 1
        return Integer_Division(a - b,b,count)
    
    return count
       

if __name__ == "__main__":
    number = int(input('Enter a number:'))
    number2 = int(input('Enter another number:'))
    print(Integer_Division(number,number2))

       

