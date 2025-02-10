import sys
import os
import shutil
from colorama import Fore
import configparser

config_path = 'config.ini'
default_config = """
[file]
extension = .txt
encoding = UTF-8

[theme]
background = CYAN
warning_background = RED
success_background = GREEN
"""

if not os.path.exists(config_path):
    with open(config_path, 'w', encoding="utf-8") as cf:
        cf.write(default_config)

config = configparser.ConfigParser()
config.read(config_path)

default_extension = config["file"]["extension"]
default_encoding = config["file"]["encoding"]
default_background = getattr(Fore, config["theme"].get("background", "CYAN"))
default_warning_background = getattr(Fore, config["theme"].get("warning_background", "RED"))
default_success_background = getattr(Fore, config["theme"].get("success_background", "GREEN"))

notes_folder = "notes/"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

if len(sys.argv) < 2:
    print(default_warning_background, "Usage on Windows: python terminote.py <option>")
    print(default_warning_background, "Usage on Linux: python terminote.py <option>")
else:
    command = sys.argv[1]
    print(default_background, " ", end="")

    if command == "create":
        note_name = input("Note name: \n> ")
        note_value = input("Note contents: \n> ")
        note_tags = input("Note tags(optional): \n> ")
        note_author = input("Note author(optional): \n> ")
        note_file_name = notes_folder + note_name + str(default_extension)

        try:
            with open(note_file_name, "w", encoding=str(default_encoding)) as note_file:
                note_file.write(f"{note_value}\nYour tags: {note_tags}\nAuthor: {note_author}")
            print(default_success_background, f"Note is succesfully created at: {note_file_name}")

        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "show":
        note_name = input("Note name: \n> ")
        note_file_name = notes_folder + note_name + str(default_extension)

        try:
            with open(note_file_name, "r", encoding=str(default_encoding)) as note_file:
                print(default_background, note_file.read())
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "delete" or command == "remove":
        note_name = input("Note name: \n> ")
        note_file_name = notes_folder + note_name + str(default_extension)

        try:
            os.remove(note_file_name)
            print(default_success_background, "Note is succesfully deleted.")
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "edit":
        note_name = input("Note name: \n> ")
        note_file_name = notes_folder + note_name + str(default_extension)

        try:
            with open(note_file_name, "r", encoding=str(default_encoding)) as note_file:
                note = note_file.read()
                print(default_background, "Old Text: ", note)

            with open(note_file_name, "w", encoding=str(default_encoding)) as note_file:
                edited_note = input("Edited(New) Text: ")
                edited_tags = input("Edited tags: ")
                edited_author = input("Edited Author: ")

                note_file.write(f"{edited_note}\nYour tags: {edited_tags}\nAuthor: {edited_author}")
            print(default_success_background, "Note is succesfully edited.")
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "rename":
        note_name = input("Note name: \n> ")
        note_file_name = notes_folder + note_name + str(default_extension)

        try:
            new_name = notes_folder + input("New Name: ") + ".txt"
            os.rename(note_file_name, new_name)

            print(default_success_background, "Note is succesfully renamed.")
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "search":
        search_value = input("Note name: \n > ") + str(default_extension)
        note_lists = os.listdir(notes_folder)

        if search_value in note_lists:
            print(default_success_background, f"Note is founded: {notes_folder + search_value}")
        else:
            print(default_warning_background, "Note isn't founded.")

    elif command == "list":
        print(default_background, os.listdir(notes_folder))

    elif command == "export":
        try:
            note_name = input("Note name: \n > ")
            note_file_name = notes_folder + note_name + str(default_extension)

            export_path = input("Path to export: \n > ")
            shutil.copy(note_file_name, export_path)

            print(default_success_background, "Note is succesfully exported.")
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "import":
        try:
            import_path = input("Path to import: \n > ")
            shutil.copy(import_path, "./notes")

            print(default_success_background, "Note is successfuly imported.")
        except Exception as e:
            print(default_warning_background, f"Error: {e}")

    elif command == "settings":
        config.read('config.ini')

        extension = config["file"]["extension"]
        encoding = config["file"]["encoding"]
        background = config["theme"]["background"]
        warning_background = config["theme"]["warning_background"]
        success_background = config["theme"]["success_background"]

        print(default_background, f"Note File Extension: {extension}")
        print(f"Note File Encoding: {encoding}")
        print(f"Background Color: {background}")
        print(f"Warning Background Color: {warning_background}")
        print(f"Success Background Color: {success_background}")

        yn = input("Do you want change settings?(y,n): ")

        if yn == "y":
            print(default_background, " ", end=" ")

            file_extension = str(input("New file format(.*): "))
            file_encoding = str(input("New file encoding(Ex: UTF-8): "))
            new_background = str(input("New background color: "))
            new_warning_background = str(input("New warning background color: "))
            new_success_background = str(input("New success background color: "))

            config.read('config.ini')

            config["file"]["extension"] = file_extension
            config["file"]["encoding"] = file_encoding
            config["theme"]["background"] = new_background.upper()
            config["theme"]["warning_background"] = new_warning_background.upper()
            config["theme"]["success_background"] = new_success_background.upper()

            with open('./config.ini', 'w', encoding="UTF-8") as config_file:
                config.write(config_file)
    else:
        print(default_warning_background, f"Unknown command: {sys.argv[1]}")
