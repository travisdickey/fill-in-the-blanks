# IPND Stage 2 Final Project

# List of blanks to be passed in to the start quiz function.
blanks  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___"]


# quiz_strings: 3 levels of difficulty along with answers for each

easy = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answers_easy = [["function", "functions", "Function", "Functions"], ["parameter", "parameters", "Parameters", "parameters"],"None",  "boolean"]

medium = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answers_medium = [["function", "functions", "Function", "Functions"], ["parameter", "parameters", "Parameters", "parameters"],"None",  "boolean"]


hard = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answers_hard = [["function", "functions", "Function", "Functions"], ["parameter", "parameters", "Parameters", "parameters"],"None",  "boolean"]


# Checks if a word in answers is a substring of the word passed in.
def is_blank(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

# Checks if user_answer is in answers; returns boolean
def is_correct(user_answer, replacement, answers):
    if replacement == blanks[0]:
        return user_answer in answers[0]
    elif replacement == blanks[1]:
        return user_answer in answers[1]
    elif replacement == blanks[2]:
        return user_answer in answers[2]
    elif replacement == blanks[3]:
        return user_answer in answers[3]
    elif replacement == blanks[4]:
        return user_answer in answers[4]
    elif replacement == blanks[5]:
        return user_answer in answers[5]
    elif replacement == blanks[6]:
        return user_answer in answers[6]
    elif replacement == blanks[7]:
        return user_answer in answers[7]
    return None

# Starts game, prompts user to decide difficulty level; calls play_game at appropriate level
def difficulty():
    print "\nWelcome to my fill-in-the-blanks quiz.\n"
    level = raw_input("Please choose difficulty level. Type easy, medium, or hard.\n")
    if level == "easy":
        print "You've chosen easy.\n\n You get 5 guesses per problem."
        return play_game(easy, answers_easy)
    if level == "medium":
        print "You've chosen medium.\n\n You get 5 guesses per problem."
        return play_game(medium, answers_medium)
    if level == "hard":
        print "You've chosen hard.\n\n You get 5 guesses per problem."
        return play_game(hard, answers_hard)
    return difficulty()

# prompts user to supply an answer then runs is_correct to check answer. Returns
''' def prompt_user(user_answer, replacement, answers):
    user_answer = raw_input("What should be substitued for " + replacement + "?" + " ")
    if is_correct(user_answer, replacement, answers):
        word = word.replace(replacement, user_answer)
        return word '''

# Takes current blank, user_answer, and quiz_string and returns revised quiz_string.
def corrected_string(word, user_answer, quiz_string):
    revised = quiz_string
    revised = revised.replace(word, user_answer, 1)
    return revised

# Runs a fill-in-the-blanks quiz; takes quiz_string and answers; prompts user
#to replace blanks in quiz_string; displays corrected quiz_string
def play_game(quiz_string, answers):
    replaced = []
    attempts = 1
    max_attempts = 5
    revised = quiz_string
    print "\n" + quiz_string + "\n"
    quiz_string = quiz_string.split()
    for word in quiz_string:
        replacement = is_blank(word, blanks)
        if replacement != None:
            user_answer = raw_input("What should be substitued for " + replacement + "?" + " ")
            if is_correct(user_answer, replacement, answers):
                word = word.replace(replacement, user_answer)
                revised = corrected_string(replacement, user_answer, revised)
                print "\nThat is correct! The paragraph now reads as follows:\n" + revised + "\n"
                print "Well done! Try the next one."
            else:
                while attempts < max_attempts:
                    if (max_attempts - attempts) > 1:
                        print "\nI'm sorry. That is not correct. Try again. You have " + str(max_attempts - attempts) + " tries left."
                        user_answer = raw_input("What should be substitued for " + replacement + "?" + " ")
                        if is_correct(user_answer, replacement, answers):
                            word = word.replace(replacement, user_answer)
                            revised = corrected_string(replacement, user_answer, revised)
                            print "\nThat is correct! The paragraph now reads as follows:\n" + revised + "\n"
                            print "Well done! Try the next one."
                            break
                    elif (max_attempts - attempts) == 1:
                        print "\nI'm sorry. That is not correct. You have only " + str(max_attempts - attempts) + " try left."
                        user_answer = raw_input("What should be substitued for " + replacement + "?" + " ")
                        if is_correct(user_answer, replacement, answers):
                            word = word.replace(replacement, user_answer)
                            revised = corrected_string(replacement, user_answer, revised)
                            print "\nThat is correct! The paragraph now reads as follows:\n" + revised + "\n"
                            print "Well done! Try the next one."
                            break
                        else:
                            print "I'm sorry. You have reached the maximum number of incorrect responses. Please try again later."
                            quit()
                    attempts += 1
        replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

difficulty()
