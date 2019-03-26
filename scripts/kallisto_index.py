"""
    __author__: Kevin Chau
    __description: Construct Kallisto transcriptome index
    TODO: check how to import snakemake parameters
"""

import os
import subprocess

def construct_index(kallisto, transcriptome, idx_out):
    """Construct Kallisto index

        @param kallisto Path to kallisto executable
        @param transcriptome Transcriptome to process
        @param idx_out Output filename
    """

    try:
        subprocess.check_call(
            [
                kallisto,
                "index",
                "-i", idx_out,
                transcriptome
            ]
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return(1)
    return(0)

if __name__ == '__main__':
    pass