#write a python program to find the smallest and the largest number in the list
l1 = []
n = int(input("enter number of elements required: "))
for i in range(0, n):
    element = int(input("Enter element: "))
    l1.append(element)
print("Original List:", l1)
# sorting in decending
for i in range(0, len(l1)):
  for j in range(i+1, len(l1)):
    if l1[i] <= l1[j]:
      l1[i], l1[j] = l1[j], l1[i]
print("Maximum: ",l1[0])
print("Minimum: ",l1[-1])