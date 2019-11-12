
def zip_lists(list_one,list_two,final_list = []):
    
    if list_one:
        # print(list_one)
        final_list.append(list_one[0])
        list_one.pop(0)
        print(list_one)
        return zip_lists(list_two,list_one,final_list)
    if list_two:
        # print(list_two)
        final_list.append(list_two[0])
        list_two.pop(0)
        print(list_two)
        return zip_lists(list_one,list_two,final_list)
    return final_list
    


if __name__ == "__main__":
    
    first_list = []
    second_list = []
    while True:
        first_list_input = input("Enter words, STOP to stop:")
        first_list.append(first_list_input) 
        if first_list_input == "STOP":
            for word in range(len(first_list)):
                second_list_input = input('Word:')
                second_list.append(second_list_input)
            break
    print(first_list)
    print(second_list)        
    print(zip_lists(first_list,second_list))
          
