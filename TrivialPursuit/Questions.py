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

import pymsgbox

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
        pass

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

        # Ask a dummy question for now
        answer = pymsgbox.confirm("Is this a Question?", question_type, ["Yes", "No"])
        if answer == "Yes":
            return True
        else:
            return False

################################################################################
# Functions
################################################################################


################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
