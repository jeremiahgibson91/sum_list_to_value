__author__ = 'Jeremiah'
import itertools

def remove_dup(dups):
    k = sorted(dups)
    dedup = list(k for k, _ in itertools.groupby(k))
    return dedup

def remove_empty(list):
    return [x for x in list if x != []]

def gen_sublists(thelist, k):
    n = len(thelist)
    if k == 0:
        yield list(), 0
    elif k == n:
        yield list(thelist), n
    elif k < n:
        for sublist, idx in gen_sublists(thelist[:-1], k - 1):
            for i, item in enumerate(thelist[idx:], idx):
                yield sublist + [item], i + 1

def choose_sets1(thelist, k):
    if not 0 <= k <= len(thelist):
        raise ValueError((k, len(thelist)))
    return [ L for L, i in gen_sublists(thelist, k) ]

def within_threshold(list,threshold,bounds,prints):
    s = sum(list)
    if bounds=="exact":
        if s == threshold:
            if prints:
                print('match found '+str(threshold)+": ",list)
    elif bounds=='window':
        if s >= int(threshold[0]) and s <= int(threshold[1]):
            if prints:
                print('match found '+str(s)+": ",list)

def find_lists(list,threshold,bounds,prints):
    final_list=[]
    for n in range(len(list)):
        final_list+=choose_sets1(list,n)
    final_list = remove_empty(remove_dup(final_list))
    for l in final_list:
        within_threshold(l,threshold,bounds,prints)

list1 = [1,2,3,4,5]
# list1 to check and the value you're looking for.
#list,value or [values,between],bounds(exact,window),print(true or false)
find_lists(list1,6,'exact',1)