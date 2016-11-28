#<variable> = [<list_item>,<list_item>,...]
#list
fruitList=["apple","orange","banana","grape","tomato","mango"]
#first word
print(fruitList[0])
#second to last word
print(fruitList[-2])
#group of words
print(fruitList[2:5])
print(fruitList[:4])
print(fruitList[5:])
#changing value in position 1
fruitList[1] = "KIWIWIWIWIWIWIWIWIWIWIWIWIWI"

#adding lists
numberList1 = [1,2,3]
numberList2 = [6,7,8]
numberList3 = numberList1+numberList2
print(numberList3)




numberList = [1,2,3]

print(numberList * 3)

print(numberList,"\n",numberList,"\n",numberList  )





olympicList = [["london",2012],["beijing",2008],["athens",2004]]
print(olympicList)
print(olympicList[1])#print second element of list
print(olympicList[1][0])#print the first part of the



#adding to list
inventoryList = ["m4a4","bulletproof vest","riot shield","first aid kit"]
print(inventoryList)
inventoryList.append("potion of margarine")
print(inventoryList)

#insert into specific part of list
inventoryList = ["m4a4","bulletproof vest","riot shield","first aid kit"]
print(inventoryList)
inventoryList.insert(2,"potion of margarine")
print(inventoryList)

#sorting the list
inventoryList = ["m4a4","bulletpoof vest","riot shield","first aid kit"]
print(inventoryList)
inventoryList.sort()
print(inventoryList)



inventoryList = ["m4a4","bulletproof vest","riot shield","first aid kit"]
print(inventoryList)
print(inventoryList.count("m4a4"))



inventoryList = ["m4a4","bulletproof vest","riot shield","first aid kit"]
fruitList1 = ["apple","orange","banana","grape","tomato","mango"]
print(inventoryList)
print(fruitList1)
inventoryList.extend(fruitList1)
print(inventoryList)
print(fruitList1)



#removing items
fruitList2=["apple","orange","banana","grape","tomato","mango"]
print(fruitList)
v_fruit = fruitList2.pop()
print(fruitList2)
print(v_fruit)
_fruit = fruitList2.pop(0)
print(fruitList2)
print(v_fruit)


#find position of a word in the list
fruitlist3 = ["apple","orange","banana","grape"]
print(fruitlist3)
v_index = fruitlist3.index("banana")
print(v_index)

#number of words in the list
print(fruitlist3)
print(len(fruitlist3))

#print true or false depending if apple is in the list
print("apple" in fruitlist3)




#smallest of the list
print(fruitlist3)
print(min(fruitlist3))

#biggest of the list
print(fruitlist3)
print(max(fruitlist3))



