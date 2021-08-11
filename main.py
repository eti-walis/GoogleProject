import init
import autoComplete

if __name__ == '__main__':
    db_dict = {}
    prefix2 = ""
    prefix = ""
    print("working, please wait...")
    # the init function should be called only one time, in the beginning.
    init.init("C:/Users/User/Desktop/Google/2021-archive/RFC/2.7.txt", db_dict)
    while str(prefix2) != str(-1) and str(prefix) != str(-1): #enter a new word
        prefix2 = ""
        prefix = input("************** start to type sentence:\n")
        while prefix2 != "#" and str(prefix2) != str(-1) and str(prefix) != str(-1): #continue typing
            prefix = prefix.lower()+prefix2.lower()
            autoComplete.get_best_k_completions(prefix, db_dict)
            prefix2 = input("************** continue typing. to restart press #. to exit press -1.\n"+prefix)
