# LINKED LIST OPERATIONS
# STORE STUDENT OBJECTS IN LIST

class Student :
    def __init__(self,rollno,name,mobile):
        self.__rollno=rollno
        self.__name=name
        self.__mobile=mobile

    def get_name(self):
        return self.__name
    def get_mobile(self):
        return self.__mobile
    def get_rollno(self):
        return self.__rollno
    def set_name(self,name):
        self.__name=name
    def set_rollno(self,rollno):
        self.__rollno=rollno
    def set_mobile(self,mobile):
        self.__mobile=mobile

class Node :
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_next(self):
        return self.__next

    def get_data(self):
        return self.__data

    def set_next(self,next):
        self.__next=next

    def set_data(self,data):
        self.__data=data

class LinkedList :
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def set_head(self,head):
        self.__head=head
    def set_tail(self,tail):
        self.__tail=tail

    def addNode(self,data):
        new_node=Node(data)
        if self.__head==None :
           self.__head=self.__tail=new_node
        else :
           self.__tail.set_next(new_node)
           self.__tail=new_node

    def display(self):

        temp=self.__head
        if temp==None :
            print("List is Empty")
        i=1
        while temp != None :
            x=temp.get_data()
            print("Node {} = [ {} , {} , {} ]".format(i,x.get_rollno(),x.get_name(),x.get_mobile()))
            i+=1
            temp=temp.get_next()

    def getPreviousNode(self,rollno):
        temp=self.__head

        while temp!=None :
          pre=temp
          if pre.get_next().get_data().get_rollno() == rollno :
             return pre
          temp = temp.get_next()

        return -1

    def deleteNodeByRollno(self,rollno):
        if self.__head==None :
            print("* List is Empty")
        elif self.__head.get_next()==None :
           if self.__head.get_data().get_rollno() == rollno :
                self.__head=None
                print("Node Deleted Successfully")
           else :
                print("* Node Not Found")
        else :
            temp=self.getPreviousNode(rollno)
            if temp != -1 :
                temp.set_next(temp.get_next().get_next())
                print("Node Deleted Successfully")
            else :
                print("* Node Not Found")

    def find(self,rollno):
        temp = self.__head

        while temp != None :
            if temp.get_data().get_rollno()==rollno :
                return temp
            temp=temp.get_next()
        return -1

    def insert(self,rollno_before,node):
        temp = self.find(rollno_before)
        if temp!=-1 :
           if rollno_before=="None" :
             # if rollno_before is 'None' insert new Node at Beginning of List
             node.set_next(self.__head)
             self.__head=node
           else :
             node.set_next(temp.get_next())
             temp.set_next(node)
        else :
           print("* Node not Found with roll no = ",rollno_before)

    # Update Particular Node Data in List
    def update(self,rollno,*args) :
        temp=self.find(rollno)
        if temp!=-1 :
               x=temp.get_data()
               if args[0]!=None :
                  x.set_rollno(args[0])
               elif args[1]!=None :
                  x.set_name(args[1])
               elif args[2]!=None :
                  x.set_mobile(args[2])

               print("  Details has been Successfully Updated")
               print("* Updated Details for Roll No {} =>\n* Roll No : {} , Name : {} , Mobile : {}".format(rollno,x.get_rollno(),x.get_name(),x.get_mobile()))
        else :
               print("* Node not Found with Roll number = ",rollno)

    def reverse(self):
        temp=self.get_head()
        l=[]

        while temp != None :
            l+=[temp.get_data()]
            temp=temp.get_next()
        self.__head=self.__tail=None
        i = len(l) - 1
        while i>=0 :
              list.addNode(l[i])
              i-=1

list=LinkedList()
try :

  choice=0
  print("1. Add New Node\n2. Display Linked List\n3. Delete Node by Roll Number\n4. Insert New Node after some node\n5. Update Node Data\n6. Reverse List\n7. Exit")
  while choice != 7 :

      choice = int(input("Enter Your Choice : "))
      if choice==1 :
          print("======================== STUDENT DETAILS ======================")
          rollno=input("Enter Roll number : ")
          name=input("Enter Name : ")
          mobile=input("Enter Mobile : ")
          list.addNode(Student(rollno,name,mobile))
      elif choice==2 :
          list.display()
      elif choice==3 :
          rollno = input("Enter Roll number : ")
          list.deleteNodeByRollno(rollno)
      elif choice == 4 :
          rollno_before=input("Enter Roll No after which new node is added : ")
          if list.find(rollno_before) != -1  :
              print("======================== STUDENT DETAILS ======================")
              rollno = input("Enter Roll number : ")
              name = input("Enter Name : ")
              mobile = input("Enter Mobile : ")
              node=Node(Student(rollno,name,mobile))
              list.insert(rollno_before,node)
          else :
              print("* Node not Found with Roll number = ",rollno_before)
      elif choice== 5 :
          rollno=input("Enter Roll Number for which Student data has to be updated : ")
          if list.find(rollno) != -1  :

             rollstatus=input("Do you want to update roll Number of Student having roll number {} ? (Y/N) : ".format(rollno))
             if rollstatus=='Y' :
                 updated_rollno=input("Enter New Roll Number : ")
             else :
                 updated_rollno=None

             namestatus=input("Do you want to update Name of Student having roll number {} ? (Y/N) : ".format(rollno))
             if namestatus=='Y' :
                 updated_name=input("Enter New Name : ")
             else :
                 updated_name=None

             mobilestatus=input("Do you want to update Mobile Number of Student having roll number {} ? (Y/N) : ".format(rollno))
             if mobilestatus=='Y' :
                 updated_mobile=input("Enter New Mobile Number : ")
             else :
                 updated_mobile=None

             if updated_rollno!=None or updated_mobile!=None or updated_name!=None :
                list.update(rollno,updated_rollno,updated_name,updated_mobile)
             else :
                print("* Details Not Updated for Roll Number {}".format(rollno))

          else :
              print("* Node not Found with Roll number = ",rollno)
      elif choice==6 :
          list.reverse()

except Exception :
    print("Error Occured")
