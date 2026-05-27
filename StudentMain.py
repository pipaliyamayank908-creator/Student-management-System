# Student Managment System 

StdList = []

print("=====Welcome To Student Managemant System=====")

while True:

  print("1. Add Student ")
  print("2. Viwe All Student ")
  print("3. Upadet Student Information ")
  print("4. Delete Student Recorde ")
  print("5. Exite Student Managemant System(SMS) ")

  Choice = int(input("Enter The Choice :"))


  if(Choice == 1):
    id = int(input("Enter The UId :"))
    Name = input("Enter The Student Name :")
    Age = int(input("Enter The Age :"))
    Bod =  input("Enter The Birth Date(dd/mm/yy) :")
    LastResult = input("Enter The Last Result (Pass/Fail) :")
    LastSchool = input("Enter Last School Name :")
    LastStander = int(input("Enter The LastStd  :"))

    StudentList ={
      "id":id,
      "Name" : Name,
      "Age" : Age,
      "Bod" : Bod,
      "LastResult" : LastResult,
      "LastSchool":LastSchool,
      "LastStander":LastStander
    }

    StdList.append(StudentList)
    print("====Enter Your Recorde Save Successfully 🎉")
  
  elif(Choice == 2):

    if(len(StdList) == 0):
        print("NO Record Found")

    else:

        print("\n==================== STUDENT RECORDS ====================\n")

        # TABLE HEADER
        print(f"{'No':<5} {'ID':<5} {'Name':<15} {'Age':<5} {'DOB':<15} {'Result':<10} {'School':<20} {'Std':<5}")

        print("-" * 90)

        count = 1

        # TABLE DATA
        for Student in StdList:

            print(f"{count:<5} "
                  f"{Student['id']:<5} "
                  f"{Student['Name']:<15} "
                  f"{Student['Age']:<5} "
                  f"{Student['Bod']:<15} "
                  f"{Student['LastResult']:<10} "
                  f"{Student['LastSchool']:<20} "
                  f"{Student['LastStander']:<5}")

            count += 1
  elif(Choice == 3):
    id = int(input("Enter id to update :"))

    found = False

    for s in StdList:
      if s["id"] == id :
        print("Student Found!") 

        new_Name = input("Enter New Name :")
        new_Age = int(input("Enter New Age :"))
        new_Bod = input("Enter New Bod :")
        new_LastResult = input("Enter New LastResult :")
        new_LastSchool = input("Enter New LastSchool :")
        new_LastStander = int(input("Enter New LastStander :")) 

        s["Name"] = new_Name
        s["Age"] = new_Age
        s["Bod"] = new_Bod
        s["LastResult"] = new_LastResult
        s["LastSchool"] = new_LastSchool
        s["LastStander"] = new_LastStander
        

        print("Student Information Updated SuccessFully!")
        found = True
        break

    if not found:
      print("Student Not Found")




  elif(Choice == 4):
    id = int(input("Enter id to delete : "))

    found = False

    for s in StdList:
        if s["id"] == id:
            print("Student Found!")

            StdList.remove(s)

            found = True
            print("Student Deleted Successfully!")
            break

    if not found:
        print("Student Not Found!")
 
  elif(Choice == 5):
    break
  else:
    print("🚨===========================Your Choice is Ronge===========================🚨")



