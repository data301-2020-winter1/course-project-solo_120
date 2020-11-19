import pandas as pd

def load_and_process(red):
    red = (
        red.dropna()
        .assign(slope_quality_alchohol=red['quality']/red['alcohol'])
        .groupby('quality').mean())
    return red

