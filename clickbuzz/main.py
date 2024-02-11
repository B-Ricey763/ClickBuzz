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
title3 = ""
title4 = ""
title5 = ""

best_title_text = "Need to submit"

manual_md = """
# Manual Entry 

## Titles: \n
1  <|{title1}|input|> \n 
2  <|{title2}|input|> \n
3  <|{title3}|input|> \n
4  <|{title4}|input|> \n
5  <|{title5}|input|> \n

<|Submit|button|on_action=on_submit|id=button_submit|> \n

## Best Title \n
                     
<|{best_title_text}|text|>
"""

generative_md = """
# Generative Entry

Ooh AI
"""

pages = {
    "/": "<|navbar|id=nav_bar|>",
    "manual": manual_md,
    "generative": generative_md,
}

if __name__ == "__main__":
    Core().run()
    # this is custom funciton
    scenario = tp.create_scenario(scenario_cfg)
    Gui(pages=pages).run(debug=True, port=8081)