# sum_list_to_value
Looks through a list for all possible combinations that sum to a specified value or to within a specified window

#Example
list1 = [1,2,3,4,5]
//list1 to check and the value you're looking for.
//list,value or [values,between],bounds(exact,window),print(true or false)
find_lists(list1,[6,7],'window',1)

output:
match found 6:  [1, 2, 3]
match found 7:  [1, 2, 4]
match found 6:  [1, 5]
match found 6:  [2, 4]
match found 7:  [2, 5]
match found 7:  [3, 4]

These are all the possible sublists of list [1,2,3,4,5] that sum to 6 or 7

Other use if you want to specify a specific value you can do that as follows.
list1 = [1,2,3,4,5]
//list1 to check and the value you're looking for.
//list,value or [values,between],bounds(exact,window),print(true or false)
find_lists(list1,6,'exact',1)

Output:
match found 6:  [1, 2, 3]
match found 6:  [1, 5]
match found 6:  [2, 4]
