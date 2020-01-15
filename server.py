import h5py
import json
import pandas as pd
import numpy as np
from argparse import ArgumentParser
import os.path

from flask import Flask, render_template

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


parser = ArgumentParser(description="ikjMatrix multiplication")
parser.add_argument("-i", dest="filename", required=True,
                    help="input h5 file", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()

app = Flask(__name__)

@app.route("/")
def index():
    # load data
    with h5py.File(args.filename, 'r') as f:
        states = f['states']
        data = np.array(states.value)
        data = np.amax(data, axis=0)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
