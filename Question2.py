import logging
from Bio import SeqIO
from collections import Counter

logging.basicConfig(level=logging.DEBUG, filename="log_ques_2.txt", filemode="w",
                    format= "%(asctime)s - %(levelname)s - %(message)s")

sequences = list(str(sequence.seq) for sequence in SeqIO.parse("C:/Users/Admin/Documents/Study/KTest Training/Tài liệu/Technical_test_06June/Seq02.fasta", "fasta"))


# Xác định xem các trình tự có cùng kích thước hay không:
for seq in sequences[1:]:
    if len(seq) != len(sequences[0]):
        print("Cac trinh tu co khong co cung kich thuoc")     
        break
    else:
        print("Cac trinh tu co cung kich thuoc")

# Khi xác định được các trình tự đã cùng kích thước thì đi xét độ dài của các trình tự:
length = len(sequences[0])


consensus = ""
for i in range(length):
    # Tạo 1 list chứa tất cả các nu ở cùng vị trí trên tất cả các sequences
    nu_at_each_pos = [seq[i] for seq in sequences]
    
    # Sử dụng hàm Counter để đếm số nu từng loại khi sắp gióng cột cho tất cả các sequences
    counts = Counter(nu_at_each_pos)
    
    # Sử dụng method most_common để sắp xếp các nu theo thứ tự tần số xuất hiện giảm dần
    most_common = counts.most_common()

    # Phần tử thứ 2 trong phần tử đầu tiên của most_common là số lần xuất hiện của nu có tần số suất hiện nhiều nhất
    max_count = most_common[0][1]
    
    # Để xác định được số lần xuất hiện của 2 nu nhiều nhất có bằng nhau hay không thì ta phải tạo điều kiện:
    # Nếu tần số xuất hiện của 2 nu phổ biến nhất mà bằng nhau thì chưa xác định được vị trí nu đó trên consensus
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        consensus += "N" 
    else:
        consensus += most_common[0][0]  

print(consensus)