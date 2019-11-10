

def replace_hidden_message(encrypted_message, hidden_message, new_hidden_message,replaced_message = []):
    """
    Replaces the hidden_message hidden in input_string
    with new_hidden_message
    :param encrypted_message: a message with something
    hidden in it
    :param hidden_message: the old hidden message
    :param new_hidden_message: the new hidden message
    that will replace it
    :return: The input_string where the first occurrence
    of hidden_message is replaced with new_hidden_message
    """
    
    encrypted_list = list(encrypted_message)
    print(encrypted_list)
    hidden_list = list(hidden_message)
    print(hidden_list)
    new_hidden_list = list(new_hidden_message)
    print(new_hidden_list)

    if len(encrypted_message) >= 1 or len(hidden_message) >= 1 or len(new_hidden_message) >= 1:
        
        if len(hidden_message) == 0 and len(new_hidden_message) == 0:
            replaced_message.append(encrypted_list[0])
            return replace_hidden_message(encrypted_message[1:],hidden_message,new_hidden_message,replaced_message)

        if encrypted_message[0] != hidden_message[0]:
            replaced_message.append(encrypted_list[0])
            return replace_hidden_message(encrypted_message[1:],hidden_message,new_hidden_message, replaced_message)

        elif encrypted_message[0] == hidden_message[0]:
            replaced_message.append(new_hidden_message[0])
            print(replaced_message)
            return replace_hidden_message(encrypted_message[1:],hidden_message[1:], new_hidden_message[1:], replaced_message)
    else:
        # print(''.join(replaced_message))
        return ''.join(replaced_message)
    


    # if len(hidden_message) == len(new_hidden_message):
    #     # print('sucess')

    #     if len(hidden_message) >= 1:
    #         new_message = encrypted_message.replace(hidden_message[0], new_hidden_message[0])
    #         # print(new_message)
    #         new_hidden = hidden_message[1:]
    #         new_new = new_hidden_message[1:]
    #         return replace_hidden_message(new_message,new_hidden,new_new)
    #     else:
    #         sys.exit(1)



if __name__ == "__main__":
    encrypted_message = input(
        'Give me a string with a message hidden in it:'
        )
    hidden_message = input(
        'Give me the hidden message:'
        )
    new_hidden_message = input(
        "what do you want the new hidden message to be?:"
    )

    assert len(hidden_message) == len(new_hidden_message), 'The new message must be the same length. Good day.'
    assert all(elem in encrypted_message for elem in hidden_message), 'what if the hidden message isn\'t present. what about case?'

    print(replace_hidden_message(encrypted_message,hidden_message,new_hidden_message))