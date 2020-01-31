#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py
import click
import numpy as np

# states = h5py.File('examples/h5Test.h5', 'r')
# fasta_path = states['fasta_path']


# # def print_attrs(name, obj):
# #     print(name)
# #     for key, val in obj.attrs.iteritems():
# #         print("    %s: %s" % (key, val))


# state_dict = {}


# # def iter_h5(name, obj):
# #     """ Find first object with 'foo' anywhere in the name """
# #     state_dict[name.split()[0]] = obj[name]


# # states['states'].visititems(iter_h5)
# # print(states['states'].values())

# for name in states['states']:
#     state_dict[name.split()[0]] = states['states'][name][()]


# print(state_dict)

# states.visititems(print_attrs)
@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('-r', '--region', type=str, help='Region start-end of visualization, e.g. 10-20', default=None)
def index(input, region):
    if region is not None:
        start, end = map(int, region.split('-'))
        splice = lambda x: x[start - 1:end]
    else:
        splice = lambda x: x
    with h5py.File(input, 'r') as f:
        # fasta_path = f['fasta_path']
        state_dict = {}
        states = f['states']
        for name in states:
            state_dict[name.split()[0]] = splice(
                np.amax(states[name][()], axis=0))
    print(state_dict)


if __name__ == "__main__":
    index()
