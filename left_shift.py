'''
[2, 2, 3, 4, 5]
[2, 3, 3, 4, 5]
[2, 3, 4, 4, 5]
[2, 3, 4, 5, 5]
[2, 3, 4, 5, 2]
def shift(aList):
    n = len(aList)
    for i in range(len(aList)):
        if aList[i] != aList[n-1]:
            aList[i] = aList[i+1]
            print(aList)
        elif aList[i] == aList[i-1]:
            aList[i] = aList[0]
            print(aList)
shift(aList=[1,2,3,4,5])'''

for i in range(1,5):
    test_list = [1, 4, 6, 7, 2]
    print ("Original list : " + str(test_list))
    test_list = test_list[1:] + test_list[:3]
    print ("List after left rotate : " + str(test_list))
    test_list = test_list[-1:] + test_list[:-3]
    print ("List after right rotate(back to original) : "
										+ str(test_list))