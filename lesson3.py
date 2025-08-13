# LIFO - Last In First Out

# lst = []
# lst.append(1)
# lst.append(2)
# print(lst.pop())

# from collections import deque
# # deque - double ended queue
# stack = deque([1, 2, 3], maxlen=4)
# stack.append(4)
# stack.append(5)
# stack.append(6)
# print(stack)
# stack.pop()
# print(stack)


# FIFO - First In First Out

# queue = deque()
# queue.appendleft(1)
# queue.appendleft(2)
# queue.appendleft(3)
# queue.appendleft(4)
# print(queue)

# sum = 0 
# lst = [{'user1': 'user1', 'account': '20$'}, {'user2': 'user2', 'account': '30$'}, {'user3':'user3', 'account':'40$'}]
# for dictionary in lst:
#     for key in dictionary:
#         if key == 'account':
#             # value = dictionary['account'].replace('$','',1)
#             value = dictionary['account'][:2]
#             # print(value)
#             sum += int(value)
# print(sum)

# Ctr + Shift + P
# autopep8

# lst = [1, 2, 3, 4, 5, 6, 12, 15]
# lstmin = []
# lstmax = []
# final_lst = []

# sum = 0
# numb = 0
# for i in lst:
#     sum += i
#     numb += 1
# sr_ar = sum / numb
# print(sr_ar)
# for i in lst:
#     if i > sr_ar:
#         lstmax.append(i)
#     if i < sr_ar:
#         lstmin.append(i)
    
# print(lstmax, lstmin)


# for i in range((len(lstmax) + len(lstmin))):
#     print(i)
#     if i < len(lstmin):
#             final_lst.append(lstmin[i])
            
#     if i < len(lstmax):
#         final_lst.append(lstmax[i])
    

# print(final_lst)



    
