# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Steven Jones, 091022, Mod 7)
# 
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.pkl'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file_obj =  open(file_name, "wb")
    pickle.dump(list_of_data,file_obj )
    file_obj.close()

def read_data_from_file(file_name):
    f = open(file_name, "rb")
    list1  = pickle.load(f)
    return list1


## GENERATING DATA FROM THE USER

n =int(input("Enter how many entries you want to do: "))
for i in range(n):
    id = input(f"Enter ID {i+1}: ")
    name = input(f"Enter Name {i+1}: ")
    lstCustomer.append([id, name])
    print()


## SAVING DATA IN BINARY FILE
save_data_to_file(strFileName, lstCustomer)

## READING THE BINARY FILE
content  = read_data_from_file(strFileName)
print(content)
    

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
# TODO: store the list object into a binary file
# TODO: Read the data from the file into a new list object and display the contents