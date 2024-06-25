import matplotlib.pyplot as plt
# with open("json_info__100000_fuzzy.txt", 'r') as f:
#     json_services = [float(i) for i in f]
    
# min_j = min(json_services)
# max_j = max(json_services)

# h = (max_j - min_j) / 100

# step = min_j

# counts = [0]*101
# pos = -1
# while(step<max_j):
#     pos+=1
#     step_next = step + h
#     for i in json_services:
#         if  i <= step_next and i >= step:
#             counts[pos]+=1
#     step= step_next
            
# print(counts)
# plt.hist(counts, 20, density = True, 
#          histtype ='bar')
# plt.show()


import matplotlib.pyplot as plt
with open("json_info__100000_fuzzy.txt", 'r') as f:
    json_services = [float(i) for i in f]
    
min_j = min(json_services)
max_j = max(json_services)

h = (max_j - min_j) / 100

step = min_j

counts = [0]*101
pos = -1
while(step<max_j):
    pos+=1
    step_next = step + h
    for i in json_services:
        if  i <= step_next and i >= step:
            counts[pos]+=1
    step= step_next
            
print(counts)
plt.hist(counts, 20, density = True, 
         histtype ='bar')
plt.show()