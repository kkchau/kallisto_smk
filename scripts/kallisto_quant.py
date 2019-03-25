"""
    __author__: Kevin Chau
    __description: Quantify RNA-seq samples with Kallisto
"""

import os
import subprocess

def quantify(kallisto, fq_dir, transcriptome):
    """Quantify the passed FASTQ files using a subprocess call to Kallisto

        @param kallisto Path to kallisto executable
        @param fq_dir Directory of the FASTQ input files
        @param transcriptome Path to reference transcriptome
    """
    try:
        out = subprocess.check_output(
            [
                kallisto,
                "OTHER STUFF"
            ]
        )
    except subprocess.CalledProcessError as e:
        print(e)
        return(1)

    return(out)

if __name__ == '__main__':
    pass
