# class TopTen:
#     def __init__(self):
#         self.num = 1


#     def __iter__(self):
#         return self

#     def __next__(self):
        
#         if self.num <=10:
#             val=self.num
#             self.num +=1

#             return val
#         else:
#             raise StopIteration


# values= TopTen()


# for i in values:
#     print(i)



class TopTenn:

    n = 1

    while n <= 10:
        sq = n*n
        n +=1
       

values= TopTenn()

for i in values:
    print(i)