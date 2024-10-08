#this shebang is for best usage on linux
#!/usr/bin/env/ python3 
import sys
import os

notes_folder = "notes/"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

if len(sys.argv) != 2:
    print("Usage on Windows: python terminote.py <option>")
    print("Usage on Linux: terminote <option>")
else:
    command = sys.argv[1]
    if command == "create":
        not_name = input("Not name: \n> ")
        not_value = input("Not contents: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        with open(not_file_name,"w") as not_file:
          not_file.write(not_value)
        print(f"Note is succesfully created at: {not_file_name}")
    elif command == "show":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        with open(not_file_name,"r") as not_file:
            note = not_file.read()
            print(note)
    elif command == "delete":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            os.remove(not_file_name)
            print("Note is succesfully deleted.")
        except Exception as e:
            print(f"Error: {e}")
    elif command == "edit":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            with open(not_file_name, "r") as not_file:
                note = not_file.read()
                print("Old Text: ",note)
            with open(not_file_name, "w") as not_file:
                edited_note = input("Edited(New) Text: ")
                not_file.write(edited_note)
            print("Note is succesfully edited.")
        except Exception as e:
            print(f"Error: {e}")
    elif command == "rename":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            new_name = notes_folder + input("New Name: ") + ".txt"
            os.rename(not_file_name, new_name)
            print("Note is succesfully renamed.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Unknown command: {sys.argv[1]}")

            
          
    