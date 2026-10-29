# FASTA Sequence Analyzer

This script reads a FASTA file and reports the length, GC percent and protein translation of each sequence. It uses only the Python standard library.

## Features

- Reads sequences from a FASTA file
- Calculates the length and GC percent of each sequence
- Translates each sequence to a protein (reading frame 1)
- Prints a table and saves results to results.csv

## Requirements

Python 3. No external libraries are needed.

## Usage

Put your FASTA file in the same folder as the script, then run:

    python analyze_fasta.py

## Files

- analyze_fasta.py: the script
- sequences.fasta: input file with 5 short sequences
- results.csv: output file

## Example output

    id       length     GC%  AA sequence
    seq1         24   54.17  MRTLADRC
    seq2         30   50.00  DYRPS*DP*R
    seq3         36   52.78  LTDAS*ANVSRC
    seq4         42   52.38  TYVALRPSIVTIVA
    seq5         48   52.08  GLIDASLTGSVTIVA*

## Notes

In the translation, * marks a stop codon. If the sequence length is not a multiple of 3,