import logging 
from Bio import SeqIO

logging.basicConfig(level=logging.DEBUG, filename="log_ques_3.txt", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

list_of_reads = list(str(sequence.seq) for sequence in SeqIO.parse("C:/Users/Admin/Documents/Study/KTest Training/Tài liệu/Technical_test_06June/Seq03.fasta","fasta"))

def assembly(a, b):
    assembled_seq = ""
    if a in b:
        assembled_seq = b
    elif b in a:
        assembled_seq = a
    else:
        min_len = min(len(a), len(b))
        for i in range(3, min_len + 1):
            if a[:i] == "".join(reversed(b[:-i-1:-1])):
                assembled_seq = b + a[i:]
                break
        for i in range(3, min_len + 1):
            if b[:i] == "".join(reversed(a[:-i-1:-1])):
                assembled_seq = a + b[i:]
                break
    return assembled_seq


allign_list = [list_of_reads[0]]
for i in range(len(list_of_reads)):
    target_dna = assembly(list_of_reads[i],allign_list[-1])
    allign_list.append(target_dna)
    logging.info(f"Trinh tu consensus sau khi allign {i+1,i+2,target_dna}")

print(allign_list[-1])