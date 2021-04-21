'''
03/01/2021

List 

A data structure that is a mutable(changeable) ordered sequence of elements. Defined by having values between square brackets.

student1 = "John"

student2 = ["John", "Chloe", "Ian", "Ashey"]

box = ["Anything", 123, True, 4.28, -13]
print(box)
>> ['Anything', 123, True, 4.28, -13]


Indexing List
Each item is a list corresponds to an index number which is zero based.

print(box[1])
box = ["Anything", 123, True, 4.28, -13]
print(box)
>> 123

List Functions

adding elements/items:
  1. LISTNAME.append(ELEMENT)
    ex.
    box = ["Anything", 123, True, 4.28, -13]
    box.append("john")
    print(box)
    >> ["Anything", 123, True, 4.28, -13, "john"]

  2. LISTNAME.insert(INDEX, ELEMENT)


'''

box = ["Anything", 123, True, 4.28, -13]
box.append("toy")
box.insert(1,False)
print(box)