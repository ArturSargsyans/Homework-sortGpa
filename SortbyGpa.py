class Student:

    def __init__(self, fullname = None, gpa = None):
        self.fullname = fullname
        self.gpa = gpa
        self.next = None

class Class:
    list = []
    def __init__(self):
        self.head = None
        Class.list.append(self)


    def setHead(self, student, gpa):
        self.head = Student(student, gpa)

    def append(self, fullname, gpa):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        newStudent = Student(fullname, gpa)
        temp.next = newStudent

    @staticmethod
    def FindIndexofLargest(list, last):
        currlist = list[0:last]
        maxval = currlist[0]
        for i in range(0, len(currlist)):
            if maxval.gpa < list[i].gpa:
                maxval = list[i]
        return currlist.index(maxval)

    @staticmethod
    def Swap(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    def SortbyGPA(self):
        n = len(Class.list)
        for last in range(n-1,1,-1):
            largest = FindIndexofLargest(Class.list, last)
            Swap(Class.list, largest, last)
        return Class.list


    def Display(self):
        printval = self.head
        while printval is not None:
            print(printval.fullname, printval.gpa)
            printval = printval.next

def main():

    my_class = Class()

    my_class.setHead("Petros Petrosyan", 2.5)

    my_class.append("Poxos Poxosyan", 2)
    my_class.append("Arshak Arshakyan", 1)
    my_class.append("Bagrat, Bagratyan", 3)
    my_class.append("Mxitar Mxitaryan", 4)

    my_class.SortbyGPA()
    my_class.Display()

main()



