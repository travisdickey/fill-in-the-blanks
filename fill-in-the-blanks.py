# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# A list of blanks to be passed in to the start quiz function.
blanks  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___"]


# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

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


# The answer for ___1___ is 'function'. Can you figure out the others?

# prints quiz_string for user

''' print sample '''

# Checks if a word in answers is a substring of the word passed in.
def is_blank(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

# Checks if user_input is in answers; returns boolean
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

# prompts user to supply an answer then runs is_correct to check answer. Returns
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

# Runs a fill-in-the-blanks quiz. A quiz taker is prompted to replace blanks in quiz_string,
# which appear in blanks with with correct answers.
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

''' play_game(sample, answers) '''

difficulty()


# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
