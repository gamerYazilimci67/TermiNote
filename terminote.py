import sys
import os

if len(sys.argv) != 2:
    print("Usage: python terminote.py <option>")
else:
    command = sys.argv[1]
    if command == "new":
        not_name = input("Not name: \n> ")
        not_value = input("Not contents: \n> ")
        not_file_name = not_name + ".txt"
        with open(not_file_name,"w") as not_file:
          not_file.write(not_value)
        print("Note is created.")
    elif command == "open":
        not_name = input("Not name: \n> ")
        not_file_name = not_name + ".txt"
        with open(not_file_name,"r") as not_file:
            note = not_file.read()
            print(note)
    elif command == "delete":
        not_name = input("Not name: \n> ")
        not_file_name = not_name + ".txt"
        try:
            os.remove(not_file_name)
            print("Note is deleted.")
        except Exception as e:
            print(f"Error: {e}")

            
          
    