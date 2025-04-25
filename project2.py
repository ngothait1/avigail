def saveNewEntry(records):
    id_number_input=input("ID: ")
    if not id_number_input.isdigit():
        print("Error: Input must be a number , "+ id_number_input + " is not a number")
        input("Press enter to continue")
        return
    if id_number_input in records:
            record = records[id_number_input]
            print("Error :ID is already exsist name :"+record["name"] +", age :"+ str(record["age"]))
            input("Press enter to continue")
            return
    name = input("Name: ")
    age = input("Age :")
    if not age.isdigit():
        print("age must me integer")
        input("Press enter to continue")
        return
    records[id_number_input] = {"name": name, "age": int(age)}  
    print("ID [" + str(id_number_input) + "] saved succesfuly")
    input("Press enter to continue")

def searchById(records):
     id = input("Please enter the id you want to look for :")
     if not id.isdigit():
          print("ID need to be number")
          input("Press enter to continue")
          return
     if not id in records:
          print("Error : ID " + str(id) + " is not saved")
          input("Press enter to continue")
          return
     record = records[id]
     print("ID :"+ id + "\n" +
           "Name :"+ record["name"] + "\n" +
           "age :" + str(record["age"]) )
     input("Press enter to continue")
    
def printAgesAvarage(records):
     count = 0
     ageAvarage = 0
     for record in records.values():
          ageAvarage += record["age"]
          count += 1
     if count > 0:
          avg = ageAvarage / count
          print(avg)
          input("Press enter to continue")
          return
     else :
          print("0")
          input("Press enter to continue")
          return

def printAllNames(records):
     for index , record in enumerate(records.values()):
          print(str(index) + ". " + record["name"])
     input("Press enter to continue")
     return

def printAllIds(records):
     for index , record in enumerate(records):
          print(str(index) + ". " + record)
     input("Press enter to continue")
     return


def printAllEntries(records):
    for index, (id, record) in enumerate(records.items()):
          print(str(index) + ". " + str(id) +
               " Name :" + record["name"] +
                 " age :" + str(record["age"])
                )
    input("Press enter to continue")
    return

def printByIndex(records):
     index = input(" Please enter the index of the entry you want to print :")
     if not index.isdigit():
          print("the index need to be number")
          input("Press enter to continue")
          return
     index = int (index)
     if not index >= 0 or not index < len(records):
          print("the index is out of range , the maximum is " + str(len(records)))
          input("Press enter to continue")
          return
     items = list(records.items())
     id ,record = items[index]
     print("ID :" + str(id) +
           " Name :" + record["name"]+
           " Age :" + str(record["age"]))
     input("Press enter to continue")
     return

   
records = {}
while True:
    print(
        "1. Save an entry\n"
        "2. Search by ID\n"
        "3. Print average age\n"
        "4. Print all names\n"
        "5. Print all IDs\n"
        "6. Print all entries\n"
        "7. Print entry by index\n"
        "8. Exit\n")
    option =input("Please enter your choice: ")
    if option == "1":
        saveNewEntry(records)
    if option == "2":
         searchById(records)
    if option == "3":
         printAgesAvarage(records)
    if option == "4":
         printAllNames(records)
    if option == "5":
         printAllIds(records)
    if option == "6":
         printAllEntries(records)
    if option == "7":
         printByIndex(records)
    if option == "8":
         ans = input("Are you sure? (y/n)")
         while not ans == "y" and not ans == "n":
              ans = input("Are you sure? (y/n)")
         if ans == "n":
              continue
         if ans == "y":
              print("GoodBye!")
              break
    else :
         print("option "+ str(option) + " does not exist please try again")