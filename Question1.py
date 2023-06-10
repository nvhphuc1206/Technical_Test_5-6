import logging
from Bio import SeqIO

logging.basicConfig(level=logging.DEBUG, filename="log_ques_1.txt", filemode="w",
                    format= "%(asctime)s - %(levelname)s - %(message)s")

dna = SeqIO.read("C:/Users/Admin/Documents/Study/KTest Training/Tài liệu/Technical_test_06June/Seq01.fasta","fasta").seq

# Tạo 1 hàm để tìm trình tự lặp lại và số lần lặp lại từ 1 trình tự gốc có 2 đối số gồm trình tự gốc và độ dài ngắn nhất của trình tự lặp lại: 
def find_repreat_subseq(dna, length):   
    result_list = []
    n = len(dna)
    # Tạo vòng lặp bao gồm những độ dài của trình tự lặp lại:
    for specific_length in range(length,n-length):
        repreat_subseq = []
        repeated_counts = {}
        # Đối với mỗi độ dài nhất định, tạo subsequence tương ứng với độ dài đó tuy nhiên sau mỗi vòng lặp vị trí bắt đầu của subsequence sẽ tiến tới 1 nu cho đến hết trình tự gốc:
        for pos in range(n - specific_length + 1):
            subseq = dna[pos:pos+specific_length]
            # Sử dụng Dictionary để thêm từng cặp subseq : count tương ứng, nếu supseq đã xuất hiện trong dict thì count + 1 còn nếu subseq chưa xuất hiện thì tạo 1 cặp subseq : count mới với count = 1
            if subseq in repeated_counts:
                repeated_counts[subseq] += 1
            else:
                repeated_counts[subseq] = 1

        # Đối với mỗi cặp subseq : count trong dict, chỉ chọn những subseq có số lần lặp lại cao hơn 1:
        for subseq, count in repeated_counts.items():
            if count > 1:
                repreat_subseq.append([subseq, count])
        # Thêm list chứa các cặp subseq : count vào list kết quả tuy nhiên đối với từng length thì có thể subseq đó không có trình tự lặp lại vì vậy sẽ có list rỗng nên cần thêm điều kiện loại bỏ các rỗng đó:
        if repreat_subseq != []:
            result_list.append(repreat_subseq)
            logging.info(f"Cac trinh tu lap lai co kich thuoc {specific_length,repreat_subseq}")
    return result_list



repeat_subsequences = find_repreat_subseq(dna,10)
for i in repeat_subsequences:
    for subseq, count in i:
        print(subseq, count)





