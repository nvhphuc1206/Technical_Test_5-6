import argparse
import logging 
from Bio import SeqIO

parser = argparse.ArgumentParser(description="Assembly DNA sequences")
parser.add_argument("file",type=str, help="File trinh tu")
args = parser.parse_args()

file_path = str(args.file).replace('\\','/')

logging.basicConfig(level=logging.DEBUG, filename="log_ques_3.txt", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Start")

# Tạo 1 list chứa tất cả các trình tự từ file gốc dưới dạng string
list_of_reads = list(str(sequence.seq) for sequence in SeqIO.parse(f"{file_path}","fasta"))

# Tạo 1 hàm lắp rắp 2 trình tự:
def assembly(a, b):
    assembled_seq = ""
    # Điều kiện 1 nếu trình tự a tìm thấy trong trình tự b thì trình tự ghép sẽ là trình tự b
    if a in b:
        assembled_seq = b
    # Điều kiện 2 nếu trình tự b tìm thấy trong trình tự b thì trình tự ghép sẽ là trình tự a
    elif b in a:
        assembled_seq = a
    # Trường hợp 2 trình tự không nằm trong nhau thì:
    else:
        min_len = min(len(a), len(b))
        # Tạo vòng lặp, đối với độ dài tối thiểu là 3 nu tìm đoạn overlap giữa 2 trình tự, nếu có overlap thì trình tự ghép là trình tự nối của 2 trình tự a và b
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
# Tạo vòng lặp so sánh và ghép từng cặp trình tự trong file:
for i in range(len(list_of_reads)):
    # Cách so sánh đó là so sánh từng trình tự với trình tự ghép từ vòng lặp trước
    target_dna = assembly(list_of_reads[i],allign_list[-1])
    allign_list.append(target_dna)
    logging.info(f"Trinh tu consensus sau khi allign 2 trinh tu thu {i+1,i+2} la : {target_dna}")

print(allign_list[-1])
logging.debug("End")