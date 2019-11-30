def checkUp(y, x, fileList):
    if fileList[y - 1][x] == ' ':
        return True
    else:
        return False

def checkRight(y, x, fileList):
    if fileList[y][x + 1] == ' ':
        return True
    else:
        return False

def checkDown(y, x, fileList):
    if fileList[y + 1][x] == ' ':
        return True
    else:
        return False

def checkLeft(y, x, fileList):
    if fileList[y][x - 1] == ' ':
        return True
    else:
        return False

#Recursive function that fills the whole 'zone'
def fillIn(y, x, fileList, symbol):
    if fileList[y][x] == " ":
        fileList[y][x] = symbol

    if checkUp(y, x, fileList) == False and checkRight(y, x, fileList) == False and checkDown(y, x, fileList) == False and checkLeft(y, x, fileList) == False:
        #^^^Base case
        return fileList
    else:
        #Returns booleans
        if checkUp(y, x, fileList) == True:
            fillIn(y - 1, x, fileList, symbol)
        if checkRight(y, x, fileList) == True:
            fillIn(y, x + 1, fileList, symbol)
        if checkDown(y, x, fileList) == True:
            fillIn(y + 1, x, fileList, symbol)
        if checkLeft(y, x, fileList) == True:
            fillIn(y, x - 1, fileList, symbol)
    return fileList

#Recursive function that fills the whole 'zone' and shows the steps
def fillInR(y, x, fileList, symbol):
    if fileList[y][x] == " ":

        fileList[y][x] = symbol
        printGrid(fileList)        
    if checkUp(y, x, fileList) == False and checkRight(y, x, fileList) == False and checkDown(y, x, fileList) == False and checkLeft(y, x, fileList) == False:
        #^^^Base case
        return fileList
    else:
        #Returns booleans
        if checkUp(y, x, fileList) == True:
            fillInR(y - 1, x, fileList, symbol)

        if checkRight(y, x, fileList) == True:
            fillInR(y, x + 1, fileList, symbol)

        if checkDown(y, x, fileList) == True:
            fillInR(y + 1, x, fileList, symbol)

        if checkLeft(y, x, fileList) == True:
            fillInR(y, x - 1, fileList, symbol)

    return fileList


def printGrid(fileList):

    for i in range(len(fileList)):
        for j in range(len(fileList[i])):
            print(fileList[i][j], end = "")
        print()
    print()

def main():
    
    #Asks for file name and prints out the contents of the file
    fileName = input("Please enter a file for input: ")
    while fileName.endswith(".dat") == False and fileName.endswith(".txt") == False : 
        
        if fileName.endswith(".dat") == False and fileName.endswith(".txt") == False :
            fileName = input("That is not a valid filename -- please enter a filename\n\tthat ends in \".dat\" or \".txt\": ")
    File = open(fileName, 'r')
    fileList = []
    for line in File:
        fileList.append(line.strip())
    for i in range(0,len(fileList)):
        fileList[i] = list(fileList[i])



#   print(fileList)
    printGrid(fileList)
    File.close()
    coords = "123"
    while coords != 'Q':
    #Asks for the starting point and puts it into rowcol[]
        
        poop = True
        while poop == True and coords != 'Q':
            coords = input("Please enter the coordinates you would like to start\nfilling at in the form \"row,col\", or Q to quit: ")
            if coords != 'Q':
                rowcol = coords.split(",")
                rowcol[0] = int(rowcol[0])
                rowcol[1] = int(rowcol[1])
                if rowcol[0] < 0 or rowcol[0] > len(fileList) - 1:
                    print("\t", rowcol[0], "is not a valid row value; please enter a number\n\tbetween 0 and", len(fileList) - 1, "inclusive.")
                if rowcol[1] < 0 or rowcol[1] > len(fileList[0]) - 1:
                    print("\t", rowcol[1], "is not a valid column value; please enter a number\n\tbetween 0 and", len(fileList[0]) - 1, "inclusive.")
                if rowcol[0] >= 0 and rowcol[0] <= len(fileList) - 1 and rowcol[1] >= 0 and rowcol[1] <= len(fileList[0]) - 1:
                    poop = False
    #Asks for the symbol to 'fill in'
        if coords != 'Q':
            symbol = "100"
            while len(symbol) > 1:
                symbol = input("Please enter a symbol to fill with: ")
                if len(symbol) > 1:
                    print("\tThe symbol\"", symbol, "\" is not a single character.")
            
            option = "nah"
            while option != "yes" and option != "no":
                option = input("Would you like to show each step of the recursion?\nEnter \"yes\" or \"no\": ")
                if option != "yes" and option != "no":
                    print("The choice \"" + option + "\" is not valid.")


            if option == "yes":
                final = fillInR(rowcol[0], rowcol[1], fileList, symbol)
            elif option == "no":
                final = fillIn(rowcol[0], rowcol[1], fileList, symbol)


            print("\n=======================================================\n")
            printGrid(final)
            
    print("Thank you for using the Autofill program!")
main()