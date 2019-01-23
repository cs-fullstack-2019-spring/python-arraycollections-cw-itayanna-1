def main():
    #prob1()
    # prob2()
    #prob3()
    #prob4()
     prob5()



def prob1():
    arrayForProblem1 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem1[2])
    print(arrayForProblem1.__len__())
    arrayForProblem1.pop(1)
    print(arrayForProblem1[2])


def prob2():
    ui= ''
    while ui!="q":
        ui= input("enter something. enter q to quit")

def prob3():
    nickNames = {
        "Johnathan": "John",
        "Michale":"Mike",
        "William":"Bill",
        "Robert":"Rob"
    }

    for eachElement in nickNames:
        print(eachElement)
    print(nickNames["William"])

def prob4():
    numArray= [1,2,3,4,5]
    for i in range(len(numArray)-1,-1,-1):
        print(numArray[i])
def prob5():
    daList= [2,3,4,1,5]
    userIndex= int(input("Enter a number"))
    higher= 0
    lower= 0
    equal= 0
    for x in range(0,5):
        #daList[x]
        if userIndex>daList[x]:
            lower+=1
        elif userIndex<daList[x]:
            higher+=1
        elif userIndex==daList[x]:
            equal+=1
    print("higher= ",higher)
    print("lower= ", lower)
    print("equal= ",equal)

















if __name__ == '__main__':
    main()