import json

with open("managers.json","r") as f:
     managers_dict = json.load(f)

manager_id = input("enter manager id: ")
manager_password = input("enter manager password: ")

manager_validation = False

for manager in managers_dict["managers"]:
     if manager_id == manager["id"] and manager_password == manager["password"]:
          manager_validation = True
          print("data accessed")
          break



if manager_validation == True:


     with open("students.json","r") as f:
       students_dict = json.load(f)

     task = input("task to perform: ")
    

     class students_data():
      def __init__(self,id,name,age,marks):
          self.id = id
          self.name = name 
          self.age = age
          self.marks = marks
          
          student = {
               "id":self.id,
               "name": self.name,
               "age": self.age,
               "marks": self.marks}
          for existing_student in students_dict["students"]:
               if existing_student["id"] == self.id:
                    print("student already exists")
                    return
               else:
                    students_dict["students"].append(student)
                    print("student added")
                    break
     

     class student_manager():

      def find_student(self,id): 
          for student in students_dict["students"]:
           if student["id"] == id:
                    print(f"student found: {student}")
                    return
          else:
                    print("no student found")

      def update_student(self,id,name,age,marks):
            for student in students_dict["students"]:
                 if student["id"] == id:
                        student["name"] = name
                        student["age"] = age
                        student["marks"] = marks
                        print("student updated")
                        return
                 else:
                    print("no student found")
                        
     
      def delete_student(self,id):
          for student in students_dict["students"]:
               if student["id"] == id:
                    students_dict["students"].remove(student)
                    print("student deleted")
                    return
               else:
                    print("no student found")
               
      def show_detail():
          print(students_dict)
                    
     m = student_manager()


     if task == "find":
      id = int(input("enter student's id: "))
      m.find_student(id)
     elif task == "update":
      id = int(input("enter student's id: "))
      name = input("enter student's name: ")
      age = int(input("enter student's age: "))
      marks = int(input("enter student's marks: "))
      m.update_student(id,name,age,marks)
     elif task == "delete":
       id = int(input("enter student's id: "))
       m.delete_student(id)
     elif task == "add":
         id = int(input("enter id: "))
         name = input("enter name: ")
         age = int(input("enter age: "))
         marks = int(input("enter marks: "))
         s = students_data(id,name,age,marks)
     elif task == 'showdata':
      student_manager.show_detail()



     with open("students.json","w") as f:
       json.dump(students_dict, f,indent=4)
     
else:
    print("access denied")         
         










          


