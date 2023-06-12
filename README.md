# Technical_Test_5-6
This repository summarizes 3 exercises:
1. Find a repeated sequence in an original sequence
2. Find consensus sequence from short reads
3. Assembly a DNA string based on sequences

## Table of Contents:
 - [Table of Contents](#table-of-contents)
 - [Questions](#questions)
 - [Input](#input-file)
 - [Solution](#solution)

## Questions

Question 1: : Given a DNA string (Seq01.fasta), report the sequence:numberofrepeat of the Kmers that has equal or greater than 10 base-pair. Using argparser library  (hEps://docs.python.org/3/library/argparse.html) for user inpuIng.

Question 2: : Building a consensus by taking 10 strings in Seq02.fasta in consideraIon. Use logging library to report the log file (hEps://docs.python.org/3/library/logging.html).

Question 3:  Assembly a DNA string based on 7 sequences in Seq03.fasta. Use both argparser and logging library.

## Input file

1. Seq01.fasta.
2. Seq02.fasta.
3. Seq03.fasta.

## Solution

Solutions for each question are in each file below, respectively:
1. Question01.py
2. Question02.py
3. Question03.py

In addition, because the method in Question3.py is not optimal, I have consulted some other sources and redone in the file.

By using argparse, it is necessary to add the set arguments to each file in order to run code files 1 and 3 using argparse:

1. Open terminal.
2. Copy the corresponding code

```bash
python Question01.py -l (minimum length of repeated sequence) -f (file name)
```

```bash
python Question03.py Seq03.fasta
```

3. Enter or Return.
