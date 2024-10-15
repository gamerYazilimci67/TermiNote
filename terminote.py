#this shebang is for best usage on linux
#!/usr/bin/env/ python3 
import sys
import os
import shutil
from colorama import Fore

notes_folder = "notes/"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

if len(sys.argv) != 2:
    print(Fore.RED,"Usage on Windows: python terminote.py <option>")
    print(Fore.RED,"Usage on Linux: terminote <option>")
else:
    command = sys.argv[1]
    print(Fore.CYAN," ",end="")
    if command == "create":
        not_name = input("Not name: \n> ")
        not_value = input("Not contents: \n> ")
        not_tags = input("Not tags(optional): \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            with open(not_file_name,"w",encoding="UTF-8") as not_file:
                not_file.write(not_tags + "\n" + not_value)
            print(f"Note is succesfully created at: {not_file_name}")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "show":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            with open(not_file_name,"r",encoding="UTF-8") as not_file:
              lines = not_file.readlines()
              note = [line.strip() for line in lines[1:]]
              print(note)
              note_tag  = lines[0].strip()
              if note_tag == "": note_tag = "No note tags is found."
              print(f"Tags: {note_tag}")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "delete" or command == "remove":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            os.remove(not_file_name)
            print("Note is succesfully deleted.")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "edit":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            with open(not_file_name, "r",encoding="UTF-8") as not_file:
                note = not_file.read()
                print("Old Text: ",note)
            with open(not_file_name, "w",encoding="UTF-8") as not_file:
                edited_note = input("Edited(New) Text: ")
                not_file.write(edited_note)
            print("Note is succesfully edited.")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "rename":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + ".txt"
        try:
            new_name = notes_folder + input("New Name: ") + ".txt"
            os.rename(not_file_name, new_name)
            print("Note is succesfully renamed.")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "search":
        search_value = input("Not name: \n > ") + ".txt"
        note_lists = os.listdir(notes_folder)
        if search_value in note_lists:
            print(f"Note is founded: {notes_folder + search_value}")
        else:
            print("Note isn't founded.")
    elif command == "list":
        print(os.listdir(notes_folder))
    elif command == "export":
        try:
            not_name = input("Not name: \n > ")
            not_file_name = notes_folder + not_name + ".txt"
            export_path = input("Path to export: \n > ")
            shutil.copy(not_file_name, export_path)
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "import":
        try:
            import_path = input("Path to import: \n > ")
            shutil.copy(import_path, "./notes")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
            
    else:
        print(f"Unknown command: {sys.argv[1]}")

            
          
    