# a class is a blue print or a prototype

# class parent:
#     parentatrrib=100
#
#     def __init__(self):
#         print("calling the constructor")
#     def parentmethod(self):
#         print("calling the parent method")
#     def setAttr (self,attr):
#         parent.parentatrrib= attr
#     def getAttr(self):
#         print("parent atrribute :", parent.parentatrrib)
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("calling child constructor")
#     def childmethod(self):
#         print("calling child method")
#     def parentmethod(self):
#         print("override this method")
#
# p=child()
# p.childmethod()
# p.parentmethod()
# p.setAttr(200)
# p.getAttr()


class Student:
    # class variable are share across all instances
    reg_no=""
    grade=""
    total=0
    averange= 0


    def __init__(self,mat,eng,kis,sci,sss):
        self.total=self.totalmarks(mat, eng, kis, sci,sss)


    def totalmarks(self,mat,eng,kis,sci,sss):
         total=mat+eng+kis+sci+sss




    def calavg(self,tot):
        self.averange=tot/58








# variable brian is an object of a
brain = Student(25,25,85,78,90)

print(brain.total)