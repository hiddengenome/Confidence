#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
import numpy as np
from os import path

from argparse import ArgumentParser
from flask import Flask, render_template, request, jsonify, make_response
app = Flask(__name__)


def is_valid_file(parser, arg):
    if not path.exists(arg):
        parser.error("The file {} does not exist!".format(arg))
    else:
        return arg  # return an open file handle


@app.route("/")
def index():
    seq_names = []
    for i, name in enumerate(states):
        short_name = name.split()[0]
        confidences = np.amax(states[name][()], axis=0)
        seq_names.append(
            [str(i + 1), str(i + 1), short_name, str(len(confidences))])
    return render_template("index.html", data=seq_names)


@app.route("/view", methods=["POST"])
def visualize():
    req = request.get_json()
    selections = map(int, req['selections'])

    if req['from'] != '':
        start, end = int(req['from']), int(req['to'])
        splice = lambda x: x[start - 1:end]
    else:
        splice = lambda x: x
    state_array = []
    for seqid in selections:
        name = names[seqid - 1]
        short_name = name.split()[0]
        confidences = np.amax(states[name][()], axis=0)
        state_array.append({'name': short_name, 'value': splice(
            confidences).tolist()})

    res = make_response(jsonify(state_array), 200)

    return res


if __name__ == "__main__":
    parser = ArgumentParser(description="Confidence visualization")
    parser.add_argument("-i", dest="filename", required=True,
                        help="input h5 file", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-p", dest="port", default=5000,
                        help="The port of APP")
    args = parser.parse_args()

    f = h5py.File(args.filename, 'r')
    states = f['states']
    names = list(states.keys())
    app.run(host='0.0.0.0', port=args.port, debug=True)
    f.close()
