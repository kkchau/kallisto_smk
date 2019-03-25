"""
__author__: Kevin Chau
__description__: Quantifcation of RNA-Seq data using Kallisto
"""

import os
import sys
from shutil import which

configfile: "config.yaml"

# Check if Kallisto is installed
# Check executable path
if config['kallisto']['path']:
    kallisto = config['kallisto']['path']
elif which("kallisto"):
    kallisto = "kallisto"
else:
    sys.exit("Kallisto not installed. Please install Kallisto or enter an executable path for Kallisto in config.yaml")

# Pipeline directories
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("log"):
    os.makedirs("log")

rule all:
    input: expand("", samples = config['samples'].keys())

"""Quantify RNA-Seq data with Kallisto"""
rule quantify:
    input:
        config["samples_dir"]
    output:
        "data/{samples}".format(samples = os.listdir(config["samples_dir"]))
    params:
        config["transcriptome"]
    script:
        "scripts/kallisto_quant.py"