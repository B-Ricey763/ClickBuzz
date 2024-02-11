from taipy.gui import Gui
from taipy.core import Core
from taipy.config import Config
import taipy as tp

scenario = None

def on_submit(state):
    state.scenario.input_titles.write([state.title1, state.title2, state.title3, state.title4, state.title5])
    state.scenario.submit()
    state.best_title_text = scenario.message.read()

def get_best_title(titles):
    # TODO: Change to actual algorithm
    return f"The best one: {titles[0]}"

titles_cfg = Config.configure_data_node(id="input_titles")
message_data_node_cfg = Config.configure_data_node(id="message")
get_best_cfg = Config.configure_task("build_msg", get_best_title, titles_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[get_best_cfg])

title1 = ""
title2 = ""


best_title_text = "Need to submit"

manual_md = """
# Manual Entry 

## Titles: \n
A  <|{title1}|input|> \n 
B  <|{title2}|input|> \n


<|Submit|button|on_action=on_submit|id=button_submit|> \n

## Best Title \n
                     
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