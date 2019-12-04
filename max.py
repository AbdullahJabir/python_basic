# number=[7,2,9]
# print(max(number))
# print(min(number))

# def greatest(l):
#     return max(l)-min(l)

# print(greatest(number))

#sub list count in a list

def sub_list_counter(l):
    count=0
    for i in l:
        if type(i) == list:

            count += 1
    return count

mixed=[1,2,3,[4,6,7]]

print(sub_list_counter(mixed))