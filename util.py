from collections import Counter
    
def count_list(i_ls):
    """returns a dict with count of each element
       in the input list as key value pairs
    """
    return  dict(Counter(i_ls))

def count_item(i_ls,i_item):
    """returns a count of item in the input list
       returns -1 if item not found
    """
    return dict(Counter(i_ls)).get(i_item,-1)
	

def unique_items_inorder(in_ls):
    """
    returns the unique/distinct items from input list
    in order of occurance
    """
    unique = dict(Counter(in_ls))
    ls =[]
    for key,value in unique.items():
        if value ==1:
            ls.append(key)
    return ls
	

def filter_over(i_ls,i_key):
    """returns a list filtered down to all the
       item over the key specified
    """
    ls = [i for i in i_ls if i > i_key]
    return ls

def filter_under(i_ls,i_key):
    """returns a list filtered down to all the
       item under the key specified
    """
    ls = [i for i in i_ls if i < i_key]
    return ls

def filter_even(i_ls):
    """returns a list filtered down to all the
       even items
    """
    K_DIV = 2
    ls = [i for i in i_ls if i%K_DIV ==0]
    return ls

def filter_odd(i_ls):
    """returns a list filtered down to all the
       odd items
    """
    K_DIV = 2
    ls = [i for i in i_ls if i%K_DIV ==1]
    return ls 
        
    
def filter_NaN(i_ls):
    """returns a list filtered down by removing
       nulls
    """
    return list(filter(None,i_ls))


def get_commons(i_lsa,i_lsb):
    """returns a list of common items between two lists.
    """
    return list(set(i_lsa) & set(i_lsb))
	

def get_distinct(i_lsa,i_lsb):
    """returns a list of distinct items between two lists.
    """
    return list(set(i_lsa) ^ set(i_lsb))
	
	
def sort_dict_bykey(i_dict,i_reverse = False):
    """sorts dict by key, asc order default
    """
    KEY =0
    return dict(sorted(i_dict.items(),key = lambda x:x[KEY],reverse = i_reverse))


def sort_dict_byValue(i_dict,i_reverse = False):
    """sorts dictionary by value, asc order default
    """
    VALUE =1
    return dict(sorted(i_dict.items(),key = lambda x:x[VALUE],reverse = i_reverse))


def sort_list(i_ls,i_reverse):
    """sorts list by value, asc order default
    """
    return sorted(i_ls,reverse = i_reverse)

def item_index(i_ls,i_item):
    """returns the index of first occurance item in the list
       -1 if not found
    """
    try:
        return i_ls.index(i_item)
    except ValueError:
        return -1

def item_nth_index(i_ls,item,n):
    """returns the index of the n'th occurance of
       item in list. Return -1 when not found
    """
    idx = [index for index,value in \
           enumerate(i_ls) if value ==item]
    try:
      return idx[n-1]
    except IndexError:
        return -1


def flatten_nested(i_ls):
    """flattens a list of lists
       works for any level of nesting
       usage - flat_ls = [i for i in flatten_nested(ls1)]
    """
    try:
        iter_ls = iter(i_ls)
    except TypeError:
        yield i_ls

    else:
        for i in iter_ls:
            for j in flatten_nested(i):
                yield j
				
				
def reverse_order(i_ls):
    """returns the reverse of a list, without
       changing the original list
       note: ls.reverse() changes ls.
    """
    return i_ls[-1::-1]

def read_file(i_inp):
    """read file and return words as list
    """
    K_SEPERATOR = ' '
    with open(i_inp) as fp:
        txt = fp.readlines()

    ls = [words.strip() for lines in txt for words in lines.split(K_SEPERATOR)]
    return ls
	
	
def print_dict(i_dict):
    """
    prints elements of a dict
    """
    for key,value in i_dict.items():
        print(key,value)	
		

def get_choice():
    """
    return an integer input from the user
    """
    try:
       choice = int(input('enter a number: '))
    except ValueError:
       return get_choice()
    return choice

def reverse_string(in_val):
    """
	reverses the user input (word by word)
    """
    for i in in_val[::-1]:
        print(i,end = ' ')
		
if __name__  == '__main__':
    pass