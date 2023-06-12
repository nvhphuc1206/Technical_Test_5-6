import logging
from Bio import SeqIO

logging.basicConfig(level=logging.DEBUG, filename="log_ques_3_ref.txt", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

list_of_reads = list(str(sequence.seq) for sequence in SeqIO.parse("C:/Users/Admin/Documents/Study/KTest Training/Tài liệu/Technical_test_06June/Seq03.fasta","fasta"))


def generate_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers.append(kmer)
    return kmers

def generate_kmers_from_sequences(sequences, k):
    kmers = []
    for sequence in sequences:
        kmers.extend(generate_kmers(sequence, k))
    return kmers

def build_debruijn_graph(kmers):
    graph = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
        logging.info(f"Cac edge tuong ung voi k-mers la : {graph}")
    return graph

def assemble_sequence(graph):
    start_node = next(iter(graph))  # Get an arbitrary starting node
    assembled_sequence = start_node

    while True:
        if start_node in graph:
            next_node = graph[start_node].pop(0)
            assembled_sequence += next_node[-1]
            if len(graph[start_node]) == 0:
                del graph[start_node]
            start_node = next_node
        else:
            break

    return assembled_sequence

def assemble_sequences(sequences, k):
    kmers = generate_kmers_from_sequences(sequences, k)
    debruijn_graph = build_debruijn_graph(kmers)
    assembled_sequence = assemble_sequence(debruijn_graph)
    return assembled_sequence

assembled_sequence = assemble_sequences(list_of_reads, 15)
print(assembled_sequence)