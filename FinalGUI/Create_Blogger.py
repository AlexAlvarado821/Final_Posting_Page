"""
Author: Alex Alvarado
Date:  12-11-20
Program: Create_Blogger.py
Description: Checks if a blogger's name meets the right conditions
"""
from FinalGUI import Error_Handling as exc


def check_new_blogger(l_name, f_name):
        """
        :param l_name: last name of the user from main page
        :param f_name: first name of the user from the main page
        :return: exception if there is any
        """

        if has_Numbers(f_name.replace(" ", "")) or has_Numbers(l_name.replace(" ", "")):
            raise exc.InvalidName
        elif has_spaces(f_name.replace(" ", "")) or has_spaces(l_name.replace(" ", "")):
            raise exc.NoName
        elif f_name == "" or l_name == "":
            raise exc.NoName

def check_new_post(post):
    """
    :param post:
    :return:
    """

    if not post:
        raise exc.InvalidPost


def has_Numbers(input_string):
    return any(char.isdigit() for char in input_string)


def has_spaces(input_string):
    return any(char.isspace() for char in input_string)
