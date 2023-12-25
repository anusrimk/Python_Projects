#ANUSRI.GPT

# class Lu:
#     def _init_(self):
#         self._sub = ["Python","Java","C++"]
#         self._trainer = ["Sai Sondarkar Sir","Sumit Sir","Sheetal Ma'am"]
#         self._duration = [1.0,2.0,1.5]

# class ITM:
#     def _init_(self):
#         self._sub1 = ["Business" ,"MBA" ,"Pgdm" ]
#         self._trainer1 = ["Business Mam" , "MBA Sir" , "Pgdm Mam"]
#         self._duration1 = [1.0,2.0,3.0]


# class Child(ITM,Lu):

#     def _init_(self):
#         Lu._init_(self)
#         ITM._init_(self)
    
#     def setsub(self):
#         print("\n\nHey Which one of the course you want ? ","LU : ",self._sub,"ITM : ",self._sub1,sep="\n")
#         self.subj = (input()).split(",")
    
#     def getsub(self):
#         totalhour=  0
#         print("_________________\n|SUB\t       | TRAINER\t\t| DURATION|\n___________________")
        

#         for i in self.subj:
            
#             index = None
#             if(i in self._sub ):
#                 index = self._sub.index(i)
#                 print("|" , i ,((8-len(i))" "),"   |   " , self._trainer[index], ((17-len(self._trainer[index]))" "), " | ",self._duration[index],"hr" , "|")
#                 totalhour += self._duration[index]
#             else:
#                 index = self._sub1.index(i)
#                 print("|" , i ,((8-len(i))" "),"   |   " , self._trainer1[index] ,((17-len(self._trainer1[index]))" "), " | ",self._duration1[index],"hr", "|")
#                 totalhour += self._duration1[index]

#         print("\n\nTotal Duration : ",totalhour)



# a = Child()
# a.setsub()
# a.getsub()



#USING MY METHODD


class LetsUpgrade:
    def __init__(self):
        self.subjects = {1: 'AIMLS', 2: 'Block-Chain', 3: 'Full-Stack', 4: 'UI/UX'}
        self.trainer = 'Saikiran Sondarkar sir'
        self.duration = {1: 1, 2: 1, 3: 0.5, 4: 0.5}

class ITM:
    def __init__(self):
        self.subjects = {1: 'Bsc Finance', 2: 'Hotel Management', 3: 'Health and Science', 4: 'Fashion and Design'}
        self.trainer = 'Nitin sir'
        self.duration = {1: 3, 2: 3, 3: 3, 4: 3}

class Child(LetsUpgrade, ITM):
    def __init__(self):
        super().__init__()

    def get_subject_details(self, choice):
        if choice in self.subjects:
            print(f"Subject: {self.subjects[choice]}")
            print(f"Trainer: {self.trainer}")
            print(f"Duration: {self.duration[choice]} months")
        else:
            print("Invalid choice")

def main():
    child_btech = Child()
    child_pgdm = Child()
    chose = int(input("\nChoose a subject\n1=B.Tech\n2=Business School\n "))
    if chose == 1:
        print("1. AIML\n2. Block-Chain\n3. Full-Stack\n4. UI/UX\n")
    else:
        print("5. Bsc Finance\n6. Hotel Management\n7. Health and Science\n8. Fashion and Design\n"
              "9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 9:
        print("Exiting program.")
    elif 1 <= choice <= 4:
        print('B.Tech Subjects: ')
        child_btech.get_subject_details(choice)
    else:
        child_pgdm.get_subject_details(choice)

if __name__ == "__main__":
    main()