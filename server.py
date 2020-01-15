import h5py
import json
import pandas as pd
import numpy as np

from flask import Flask, render_template

filename = 'crispr.h5'

app = Flask(__name__)

@app.route("/")
def index():
    # load data
    with h5py.File(filename, 'r') as f:
        states = f['states']
        data = np.array(states.value)
        data = np.amax(data, axis=0)#[1:200]

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
