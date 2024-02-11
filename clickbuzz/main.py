from taipy.gui import Gui
from taipy.core import Core
from taipy.config import Config
import taipy as tp

import joblib
import xgboost
import numpy as np

scenario = None

def on_submit(state):
    state.scenario.input_titles.write([state.title1, state.title2])
    state.scenario.submit()
    titles = [state.title1, state.title2]

    state.grade1 = get_grade(get_score(state.title1))
    state.grade2 = get_grade(get_score(state.title2))
    
    bestTitle = get_best_title(titles[0], titles[1])
    
    state.best_title_text = bestTitle
    

def get_score(title):
    loaded_model= joblib.load('model.joblib')
    raw_score = loaded_model.predict([title])[0]
    score = min((raw_score/2 + np.log1p(raw_score)), 1.0)
    return score

def get_grade(outScore):
    outScore =int(outScore * 100)
    outGrade = ""
    if outScore >= 90:
        outGrade = "A"
    elif outScore >= 80:
        outGrade = "B"
    elif outScore >= 70:
        outGrade = "C"
    elif outScore >= 60:
        outGrade = "D"
    else:
        outGrade = "F"
    
    # Determine if it's a + or -
    if (outScore % 10 >= 7 and outGrade != "F") or outScore > 97:
        outGrade += "+"
    elif outScore % 10 <= 3 and outGrade != "F" and outScore != 100:
        outGrade += "-"

    return outGrade

def compare_grades(grades):
    grade_values = {
        "A+": 13, "A": 12, "A-": 11, 
        "B+": 10, "B": 9, "B-": 8, 
        "C+": 7, "C": 6, "C-": 5, 
        "D+": 4, "D": 3, "D-": 2,
        "F": 1
    }   
    highest_index = 0
    
    if grade_values[grades[0]] > grade_values[grades[1]]:
        highest_index = 0
    elif grade_values[grades[0]] < grade_values[grades[1]]:
        highest_index = 1
    else:
        return -1
    return highest_index


def get_best_title(title0, title1):
    loaded_model= joblib.load('model.joblib')
    score0 = get_score(title0)
    score1 = get_score(title1)

    # Assign Letter Grade
    grade1 = get_grade(score0)
    grade2 = get_grade(score1)
    grades = [grade1, grade2]

    betterTits = compare_grades(grades)

    outTitle = ''
    if betterTits == 0:
        outTitle = title0
    elif betterTits == 1: 
        outTitle = title1
    else:
        outTitle = "You choose! Both titles scored equally well. "

    return f"The best one: {outTitle}"

titles_cfg = Config.configure_data_node(id="input_titles")
message_data_node_cfg = Config.configure_data_node(id="message")
get_best_cfg = Config.configure_task("build_msg", get_best_title, titles_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[get_best_cfg])

title1 = ""
title2 = ""

grade1 = ''
grade2 = ''

best_title_text = "Need to submit"

manual_md = """
# Welcome to ClickBUZZ!

## Input Your A|B Titles \n
A  <|{title1}|input|> Grade: <|{grade1}|text|> \n 
B  <|{title2}|input|> Grade: <|{grade2}|text|> \n


<|Submit|button|on_action=on_submit|id=button_submit|> \n

## Winning Title \n
                     
<|{best_title_text}|text|>
"""

about_md = """
# About

####Say goodbye to guesswork and hello to precision with ClickBuzz!

Introducing our cutting-edge AI machine learning model designed to revolutionize content optimization: harness the power of data-driven decision-making with our innovative platform. \n
Our AI model analyzes user engagement metrics and provides insights into the effectiveness of your content. \n\n\n
For the perfectly tailored video title that ensures every piece of content resonates with your audience, our AI empowers you to change the way you A|B test, leaving more time to create exciting content and connect with your audience.\n



"""

pages = {
    "/": "<|navbar|id=nav_bar|>",
    "manual": manual_md,
    "About": about_md ,
}

if __name__ == "__main__":
    Core().run()
    # this is custom funciton
    scenario = tp.create_scenario(scenario_cfg)
    Gui(pages=pages).run(debug=True, port=8081)