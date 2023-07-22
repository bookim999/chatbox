# by Nikki Kim

# defined function to greet user depending on whether user entered name or not
def get_greetings(name=""):
    # returned string if name is given by user
    string = "Greetings %s! I am Riley, your virtual assistant at Bank of Rabbits." % name
    # returned string if name is not given by user
    if name == "":
        string = "Hey you! I am Riley, your virtual assistant at Bank of Rabbits."

    return string


# defined function to test if word exists as a whole word in a sentence
def is_whole_word(word, sentence):
    # convert word and sentence to lower case to make function case-insensitive
    lower_word = word.lower()
    lower_sentence = sentence.lower()

    # calculate length of word and sentence
    length_word = len(lower_word)
    length_sentence = len(lower_sentence)

    # list of non-alphabets that are allowed to be right beside the word
    non_alphabet = [' ', '.', ',', '!', '?', ';', ':', '"', "'"]

    # checking whether whole word is equal to first, middle, or last word in sentence
    check_first = lower_sentence.find(lower_word, 0, length_word)
    check_last = lower_sentence.find(lower_word, length_sentence - length_word)
    check_middle = lower_sentence.find(lower_word)

    # checking if word is identical to sentence
    if lower_word == lower_sentence:
        tuple_word = True, 0
        return tuple_word
    # checking if word is in the sentence as first, middle, or last word
    if check_first != -1 or check_middle != -1 or check_last != -1:
        # check whether word is first word with a non-alphabet right behind it
        for item in non_alphabet:
            if check_first != -1 and lower_word + item in lower_sentence:
                tuple_word = True, check_first
                return tuple_word

        # check whether word is middle word with a non-alphabet right in front and behind it
        for item in non_alphabet:
            for item2 in non_alphabet:
                if check_middle != -1 and item + lower_word + item2 in lower_sentence:
                    tuple_word = True, check_middle
                    return tuple_word

        # check whether word is last word with a non-alphabet right in front of it
        for item in non_alphabet:
            if check_last != -1 and item + lower_word in lower_sentence:
                tuple_word = True, check_last
                return tuple_word

    # returned tuple if not whole word in sentence
    tuple_word = False, -1
    return tuple_word


# defined function to return correct greeting according to question
def get_basic_answers(question, name=""):
    # list of possible greetings to return
    greetings_list = ["Greetings", "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening"]
    # base index and greeting word to later reassign to return correct greeting in later code
    base_index = 10000
    greeting_word = ""

    # checking whether greeting is in user question
    # reassign base index if index of the greeting is smaller than it until you get the smallest positive index
    # reassign greeting word as the greeting with the smallest positive index
    for greeting in greetings_list:
        check = is_whole_word(greeting, question)
        greeting_index = check[1]
        if 0 <= greeting_index < base_index:
            base_index = greeting_index
            greeting_word = greeting

    # checking if greeting word is in user question
    if True in is_whole_word(greeting_word, question):
        # returned greeting if user does not give name
        if name == "":
            greetings_dict = {"Greetings": "Greetings!", "Hello": "Hello!",
                              "Hi": "Hi!", "Hey": "Hey!", "Good morning": "Good morning!",
                              "Good afternoon": "Good afternoon!",
                              "Good evening": "Good evening!", '': "Sorry, I do not understand."}
            return greetings_dict[greeting_word]

        # returned greeting if user gives name
        elif name != "":
            greetings_dict = {"Greetings": "Greetings %s!" % name, "Hello": "Hello %s!" % name,
                              "Hi": "Hi %s!" % name, "Hey": "Hey %s!" % name, "Good morning": "Good morning %s!" % name,
                              "Good afternoon": "Good afternoon %s!" % name,
                              "Good evening": "Good evening %s!" % name, '': "Sorry, I do not understand."}
            return greetings_dict[greeting_word]
    # returned string if greeting not in user input
    string = "Sorry, I do not understand."
    return string


# defined function to return specific response if q and a keyword is in user input
def get_answers(q_and_a, question):
    # check whether q and a keyword is in user question
    for key in q_and_a:
        check = is_whole_word(key, question)
        if True in check:
            string = q_and_a[key]
            return string
    # string returned if q and a keyword not in user input
    string = "Sorry, I do not understand."
    return string


# defined function to preprocess the deposit and year(s) in user input
def preprocess_earnings(question):
    # check length of question
    len_question = len(question)

    # check whether word deposit, year, years is in question
    check_deposit = is_whole_word("deposit", question)
    check_year = is_whole_word("year", question)
    check_years = is_whole_word("years", question)

    # check if the words deposit and year or deposit and years is in question
    if check_deposit and check_year or check_deposit and check_years:
        # find index of where number would be (behind deposit and in front of year or years)
        index_deposit = check_deposit[1] + 8
        index_year = check_year[1] - 2
        index_years = check_years[1] - 2

        # check whether index of number is within the length of the question and ensuring the indexes are not the same
        if len_question >= index_deposit != index_year and index_year >= 0 \
                or len_question >= index_deposit != index_years and index_years >= 0:

            # finding the character at the particular index in the question
            digit_deposit = question[index_deposit]
            digit_year = question[index_year]
            digit_years = question[index_years]

            # check whether character at index is integer
            check_digit_deposit = question[index_deposit].isdigit()
            check_digit_year = question[index_year].isdigit()
            check_digit_years = question[index_years].isdigit()

            # return string if character is a digit for both deposit and year or both deposit and years
            if check_digit_deposit and check_digit_year:
                tuple_three = True, int(digit_deposit), int(digit_year)
                return tuple_three

            elif check_digit_deposit and check_digit_years:
                tuple_three = True, int(digit_deposit), int(digit_years)
                return tuple_three

    # returned string if words not in sentence or found characters are not a digit
    tuple_three = False, 0, 0
    return tuple_three


# defined function for calculating the earnings of user
def get_earnings(question, interest_rate):
    # check whether deposit and year or deposit and years have values to process
    check = preprocess_earnings(question)

    # returned string if no deposit and year or years values to process in question
    if not check[0]:
        error = {}
        key = "Error"
        value = "Sorry, I do not understand."
        error[key] = value
        return error

    # if deposit and year or years values exist to process in question
    elif check[0] and check[1] > 0 and check[2] > 0:
        # calculate the earnings of user according to input
        initial_deposit = check[1]
        tot_year = check[2]
        year_dict = {}
        for num in range(1, tot_year + 1):
            year = num
            total_of_the_year = int(initial_deposit * (1 + interest_rate) ** year)
            key = "Year" + " " + str(num)
            value = str(total_of_the_year) + " " + "carrots."
            year_dict[key] = value

        return year_dict

    # returned string if deposit and year or years values exist to process in question, but at least one value is zero
    elif check[0] and check[1] == 0 or check[2] == 0:
        error = {}
        key = "Error"
        value = "Sorry, you must have at least 1 carrot and the deposit should be for at least 1 year."
        error[key] = value
        return error
