"""
The purpose of this program is to create a word scramble document using words pulled from existing lists in the SpellingQuiz repository (https://github.com/Monkiko/SpellingQuiz).

Created by: Ian Rivera-Leandry
Last Updated: July 3, 2025
Version: 0.1.0
"""

import os
import requests
from random import sample, shuffle
from time import sleep
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import RGBColor


# Get input from the user to determine the grade level and the number of the list to pull from

def start():
    grade_level = str(input("Please indicate the grade level of the list being used (i.e. K, 1, 2, 3, etc.): "))
    list_number = int(input("Please indicate the list number of the list being used: "))

    if len(grade_level) == 1:
        readSpellingList(grade_level, list_number)

    else:
        clean()
        print("Incorrect input. Please enter either K, 1, 2, 3, etc.")
        sleep(3)
        start()


# Clear the screen dependent on the host OS system
def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def readSpellingList(grade_level, list_number):

    match grade_level.lower():
        case "k":
            grade = "Kindergarten"
        case "1":
            grade = "First_Grade"
        case "2":
            grade = "Second_Grade"
        case "3":
            grade = "Third_Grade"
        case "4":
            grade = "Fourth_Grade"
        case "5":
            grade = "Fifth_Grade"
        case "6":
            grade = "Sixth_Grade"
        case "7":
            grade = "Seventh_Grade"
        case "8":
            grade = "Eighth_Grade"
    
    with open("Tests/" + grade + "/Simplified_Lists/Spelling_List_#" + list_number + ".txt", "r") as spelling_file:
        spellingList = []
        spellingList = spelling_file.readlines()

    spelling_file.close()
    shuffle(spellingList)
