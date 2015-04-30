"""
Module:
Questions.py

Author:
Mark Nauman

Description:
This contains the classes for the question cards

Improvements/Todo:
None at this time
"""

################################################################################
# Dependencies
################################################################################

import csv
import pymsgbox
import random

################################################################################
# Variables
################################################################################

# None

################################################################################
# Classes
################################################################################


class Questions:
    """
    Class Name:
    Questions

    Base Class:
    None

    Description:
    Define the base class for the question card
    """

    def __init__(self):
        """
        Method Name:
        __init__

        Description:
        Initialize the class objects

        Inputs:
        None

        Outputs:
        None
        """

        # Probably need to read/initialize the questions here
        self.questions = {}
        input_questions = csv.reader(open("questions.csv", "rb"))

        # Loop through all of the questions
        first = True
        for (category, question, correct, incorrect_1,
             incorrect_2, incorrect_3) in input_questions:

            # This is not the header row
            if first is False:

                # Add this category, if necessary
                if category not in self.questions:
                    self.questions[category] = []

                # Add this question
                self.questions[category].append([question,
                                                 [[correct, True],
                                                  [incorrect_1, False],
                                                  [incorrect_2, False],
                                                  [incorrect_3, False]]])

            # Mark the header row processed
            else:
                first = False

        # Shuffle the deck
        self.location = {}
        for category in self.questions.keys():
            self.location[category] = 0
            random.shuffle(self.questions[category])

    def ask(self, question_type):
        """
        Method Name:
        initialize

        Description:
        Ask a question based on the input type

        Inputs:
        question_type - question type

        Outputs:
        True/False based on if the question is answered correctly
        """

        # Get the next question
        index = self.location[question_type]
        self.location[question_type] += 1
        if self.location[question_type] >= len(self.questions[question_type]):
            self.location[question_type] = 0

        # Shuffle the answers
        random.shuffle(self.questions[question_type][index][1])

        # Generate the question text
        question = "%s\n\n" % (self.questions[question_type][index][0])

        # Generate the answer text
        number = 1
        correct = 1
        for answer in self.questions[question_type][index][1]:

            # Add this answer option
            question += "(%d) %s\n" % (number, answer[0])

            # If this is the correct answer, store
            if answer[1]:
                correct = number

            # Move next answer option
            number += 1

        # Ask the question
        answer = pymsgbox.confirm(question, question_type,
                                  ["1", "2", "3", "4"])

        # If answered correctly, assert true
        if int(answer) == correct:
            pymsgbox.alert("Correct", "Congratulations")
            return True

        # If answered incorrectly, assert false
        else:
            correct_text = self.questions[question_type][index][1][correct-1][0]
            pymsgbox.alert("Incorrect: %s" % correct_text, "Sorry")
            return False

################################################################################
# Functions
################################################################################


################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
