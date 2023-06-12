# BT1: OK
# BT2:
Absolute path: C:/Users/Admin/Documents/Study/KTest Training/Tài liệu/Technical_test_06June/Seq02.fasta !!!
Nên có argparse để input cho bước này
Việc check các trình tự có cùng chiều dài là tốt những nên ghi rõ ra khi log là trình tự nào
Trước khi output nên print `Trinh tu consensus`
Ta có thể nâng cấp thêm làm sao để có thể ứng dụng cả ngưỡng cutoff consensus. VD 1 vị trí 60% là A, 40% là C thì sẽ là A. Tuy nhiên 70% là A, 30% C thì là thoái biến Y. 20% A, 10%T, 70% G thì đó là G. 20% A, 20%T, 60%G thì đó là N. Đó là ví dụ của tạo consensus mức đồng thuận là 70% !. Code hiện tại đang tạo consensus theo nu có tần suất lớn nhất.
# BT3:
2 file BT3.py là sao ?
Với lại ko dùng đường dẫn tuyệt đối nhé, đồng thời không để dấu cách trong đường dẫn
Anh thấy code Question3_ref.py dev theo hướng tốt hơn cái kia ?