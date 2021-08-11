
from itertools import combinations
import ntpath

def init(dir1, db_dict) -> str:
    # Get all substrings of string
    # Using itertools.combinations()
    # for file in dir1:
    path=dir1
    file1 = open(dir1)
    lines = file1.readlines()
    dict_list = []
    num_of_line=0
    for line in lines:
        line=line[:-1]
        num_of_line+=1
        res = []
        for x, y in combinations(range(len(line) + 1), r=2):
            res.append(line[x:y])
        for pre in res:
            pre = pre.lower()
            if pre in db_dict:
                db_dict[pre].append((path, num_of_line))
                my_list = list(set(db_dict[pre]))
                db_dict[pre] = my_list
            else:
               db_dict[pre] = [(path, num_of_line)]

