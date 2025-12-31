import random
def average(list):
    summ=0
    for i in range(len(list)):
        summ+=list[i]
    return summ/len(list)




x= int(input("enter number of your exams"))
class_marks=[]
for i in range(x):
    marks= random.randint(0,20)
    class_marks.append(marks)
print(class_marks)
print(average(class_marks))