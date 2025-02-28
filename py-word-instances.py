fruit_list= []
fruit_dict1 = {}
fruit = input("please enter name of fruit: ")

while fruit != "stop":

    fruit= fruit.strip()
    fruit_list.append(fruit)
    instance = fruit_list.count(fruit)
    
    fruit_dict1[f"{fruit}"]= instance

    fruit = input("please enter name of fruit: ")
    
print(fruit_dict1)


# print(fruit_list)

# fruit_dict1 = {}

# for x in range(len(fruit_list)):
        
#         instance=0
#         for name in fruit_list:
#             instance = fruit_list.count(name)
#             # print(name)
#             # print(instance)
#             # print(fruit_list[x])
#             fruit_dict1[f"{fruit_list[x]}"]= instance 
# print(instance)
# print(fruit_list[0])
# print(name)
# print(instance)