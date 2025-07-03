"""
The purpose of this program is to create a word scramble document using words pulled from existing lists in the SpellingQuiz repository (https://github.com/Monkiko/SpellingQuiz).

Created by: Ian Rivera-Leandry
Last Updated: July 3, 2025
Version: 0.1.0
"""

import os
import requests
from random import sample
from time import sleep
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import RGBColor
