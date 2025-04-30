import gradio as gr
import pandas as pd
import numpy as np
import random

getHomeState("./data.yml")
time, tem, hum = LoadHomeState(r"./data.yml")


df = pd.DataFrame({
    'height': np.random.randint(50, 70, 25),
    'weight': np.random.randint(120, 320, 25),
    'age': np.random.randint(18, 65, 25),
    'ethnicity': [random.choice(["white", "black", "asian"]) for _ in range(25)]
})

with gr.Blocks() as demo:
    gr.LinePlot(df, x="weight", y="height")
    gr.ScatterPlot(df, x="height", y="age")
    gr.BarPlot(df, x="age", y="ethnicity")
demo.launch()
