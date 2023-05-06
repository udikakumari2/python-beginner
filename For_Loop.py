#Character
for i in 'Python':
    print(i)
# List
for i in ['Apple','Mango','Banana']:
    print(i)
#range build in fuction can be used
for i in range(10):
    print(i)
for i in range(5,20,3):
    print(i)
total=0
prices=[10,20,30]
for price in prices:
    total=total+price
print(f"Total:{total}")
#2D list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#matrix[row][columns]
print(matrix[0][2])
#modified
matrix[0][2]=20
#print 2d array
for i in matrix:
    for item in i:
        print(item)