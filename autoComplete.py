import ntpath
import string
from typing import List
import linecache

from AutoCompleteData import AutoCompleteData



def get_best_k_completions( prefix: str, db_dict:dict) -> List[AutoCompleteData]:
    autoCompleteDataKList = get_all_completions( prefix, db_dict)
    for item in autoCompleteDataKList:
        print(item)
def get_all_completions(prefix: str, db_dict: dict) -> List[AutoCompleteData]:
    autoCompleteDataList = []
    autoCompleteData: AutoCompleteData = None
    score = 2*(len(prefix))
    if prefix in db_dict:
        for item in db_dict[prefix]:
            cmpline=linecache.getline(item[0],item[1])
            add_to_list(autoCompleteDataList, AutoCompleteData(cmpline, ntpath.basename(item[0]), cmpline.find(prefix), score))
    #fixes
    length=len(prefix)
    for i in range(length):
        #replace
        for letter in string.ascii_lowercase:
            str = prefix[:i] + letter + prefix[i + 1:]
            if str in db_dict:
                ##### calculate score ####
                if i >= 5:
                    for item in db_dict[str]:
                        cmpline = linecache.getline(item[0], item[1])
                        add_to_list(autoCompleteDataList, AutoCompleteData(cmpline, ntpath.basename(item[0]), cmpline.find(str), score - 1))
                else:
                    for item in db_dict[str]:
                        cmpline = linecache.getline(item[0], item[1])
                        add_to_list(autoCompleteDataList, AutoCompleteData(cmpline, ntpath.basename(item[0]), cmpline.find(str), score - 5 + i))
        # add 1 letter
            str = prefix[:i + 1] + letter + prefix[i + 1:]
            if str in db_dict:
                ##### calculate score ####
                if i >= 5:
                    for item in db_dict[str]:
                        add_to_list(autoCompleteDataList, AutoCompleteData(linecache.getline(item[0],item[1]), ntpath.basename(item[0]), item[0].find(str), score - 2))
                else:
                    for item in db_dict[str]:
                        add_to_list(autoCompleteDataList, AutoCompleteData(linecache.getline(item[0],item[1]), ntpath.basename(item[0]), item[0].find(str), score-(12 - (2*i))))
        #delete 1 letter
        str = prefix[:i] + prefix[i + 1:]
        if str in db_dict:
        ##### calculate score ####
            if i >= 5:
                for item in db_dict[str]:
                    add_to_list(autoCompleteDataList, AutoCompleteData(linecache.getline(item[0],item[1]), ntpath.basename(item[0]), item[0].find(str), score - 2))
            else:
                for item in db_dict[str]:
                    add_to_list(autoCompleteDataList,AutoCompleteData(linecache.getline(item[0],item[1]), ntpath.basename(item[0]), item[0].find(str), (score - (10 - (2 * i)))))
    return autoCompleteDataList

def my_sort(autocompletedata:AutoCompleteData):
    return autocompletedata.score

def add_to_list(lst:List[AutoCompleteData], instance:AutoCompleteData):
    if len(lst) == 5 and lst[4].score < instance.score:
        lst[4] = instance

    elif len(lst) < 5:
        lst.append(instance)
    lst.sort(key=my_sort, reverse=True)
    return