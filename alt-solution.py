fruit = input("Enter name of fruit: ")
name_list=[]
instance_list=[]

while fruit !="stop":
    name_list.append(fruit)
    instance= name_list.count(fruit)
    instance_list.append(instance)
    fruit = input("Enter name of fruit: ")
# print(name_list)
# print(instance_list)
# instance_dict= dict.fromkeys(name_list,instance_list)

inst_dict = dict(zip(name_list,instance_list))

print(inst_dict)