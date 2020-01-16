# Confidence
Visualization of model confidence on genomic sequences

![Image of CRISPR region](src/example.png)

# installation
```bash
git clone https://github.com/hiddengenome/Confidence.git
cd Confidence
virtualenv env
source env/bin/activate
pip install argparse
```

# Usage

Run the Server with python 2 and point your browser to http://127.0.0.1:5000/

```bash
python visualize.py -i examples/crispr.h5
```

To visualize a subset of a larger genome, you can use `-from` and `-to` parameters

```bash
python visualize.py -i example/full.h5 -from 1000 -to 2500
```
