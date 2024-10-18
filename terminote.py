import sys
import os
import shutil
from colorama import Fore
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

default_extension = config["file"]["extension"]

notes_folder = "notes/"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

if len(sys.argv) != 2:
    print(Fore.RED,"Usage on Windows: python terminote.py <option>")
    print(Fore.RED,"Usage on Linux: python terminote.py <option>")
else:
    command = sys.argv[1]
    print(Fore.CYAN," ",end="")
    if command == "create":
        not_name = input("Not name: \n> ")
        not_value = input("Not contents: \n> ")
        not_tags = input("Not tags(optional): \n> ")
        not_file_name = notes_folder + not_name + str(default_extension)
        try:
            with open(not_file_name,"w",encoding="UTF-8") as not_file:
                not_file.write(not_value + "\n" + "Your tags: " + not_tags)
            print(f"Note is succesfully created at: {not_file_name}")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "show":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + str(default_extension)
        try:
            with open(not_file_name,"r",encoding="UTF-8") as not_file:
              print(not_file.read())
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "delete" or command == "remove":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + str(default_extension)
        try:
            os.remove(not_file_name)
            print("Note is succesfully deleted.")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "edit":
        not_name = input("Not name: \n> ")
        not_file_name = notes_folder + not_name + str(default_extension)
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
        not_file_name = notes_folder + not_name + str(default_extension)
        try:
            new_name = notes_folder + input("New Name: ") + ".txt"
            os.rename(not_file_name, new_name)
            print("Note is succesfully renamed.")
        except Exception as e:
            print(Fore.RED,f"Error: {e}")
    elif command == "search":
        search_value = input("Not name: \n > ") + str(default_extension)
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
            not_file_name = notes_folder + not_name + str(default_extension)
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
    elif command == "settings":
        config.read('config.ini')

        extension = config['file']['extension']
        print(Fore.GREEN,f"Note File Extension: {extension}")
        yn = input("Do you want change file format?(y,n): ")
        if yn == "y":
            print(Fore.CYAN," ",end=" ")
            file_extension = input("New file format(.*): ")
            config.read('config.ini')
            config["file"]["extension"] = str(file_extension)
            with open('./config.ini','w',encoding="UTF-8") as config_file:
                config.write(config_file)
    else:
        print(f"Unknown command: {sys.argv[1]}")

            
          
    
