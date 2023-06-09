import logging

logging.basicConfig(level=logging.DEBUG, filename="log_ques_3.txt", filemode="w",
                    format= "%(asctime)s - %(levelname)s - %(message)s")



def overlap(a, b): 
    if a in b:
        return len(a)
    logging.info("a trong b")
    if b in a:
        return len(b)
    logging.info("b trong a")
    min_len = min(len(a), len(b))
    for i in range(3, min_len + 1):
        if a[:i] == "".join(reversed(b[:i:-1])):
            return i
        logging.info("dau a gan voi duoi b")
    for i in range(3, min_len + 1):
        if b[:i] == "".join(reversed(a[:i:-1])):
            return i
        logging.info("dau b gan voi duoi a")
         

a = "ATGCCT"
b = "AAATTGAAGATG"
print(overlap(a,b))