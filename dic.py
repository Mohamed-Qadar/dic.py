#dictionary example
student ={}
number =input("please enter your student N0:")
name =input("please enter your name:")
surname =input("please enter your surname:")
phone =input("please enter your phone number:")
#student[number] ={
 #   'name' :name,
 #   'surnam':surname,
  #  'phone number':phone
#}
#print(student)

student.update({
    number:{
    'name' :name,
    'surnam':surname,
    'phone number':phone
    }

})

student ={}
number =input("please enter your student N0:")
name =input("please enter your name:")
surname =input("please enter your surname:")
phone =input("please enter your phone number:")

student.update({
    number:{
    'name' :name,
    'surnam':surname,
    'phone number':phone
    }

})
#print(student)
Stud_No =input("please enter your student No:")
student_No =student[Stud_No]
print(student_No)