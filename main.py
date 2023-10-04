def convert_to_number(st):
    """Function to convert a string in a number form to its corresponding integer form"""
    result = []
    word_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "double": 2,
        "triple": 3
    }
    
    words = st.split()
    
    i = 0
    while i < len(words):
        word = words[i]
        if word in word_dict:
            if word == "double" or word == "triple":
                i += 1  # Move to the next word
                if i < len(words):
                    result.extend([word_dict.get(words[i], 1)] * word_dict[word])
            else:
                result.append(word_dict[word])
        i += 1

    # Use the join() method to concatenate the numeric values as strings
    number = "".join(map(str, result))
    return number
    
inp = input("Enter the number in words: \n")    
print(convert_to_number(inp))