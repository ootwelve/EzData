import sys
import os
import dbs_manager
import json

try:
    with open('program_info.json') as file:
        program_info = json.load(file)

        try:
            ezdata_ver = program_info["versions"]["ez_data"]
            dc_alg_ver = program_info["versions"]["dc_alg"]
            dd_alg_ver = program_info["versions"]["dd_alg"]
            de_alg_ver = program_info["versions"]["de_alg"]
        except Exception as e:
            print(f"ERROR LOADING BASIC INFO: {e}")
except Exception as e:
    print(f"ERROR LOADING BASIC INFO: {e}")

file.close()

def database_creation_algorithm():
    print(f"\nEzData Database Creation Algorithm v{dc_alg_ver} | \"op_return\" at any time to return")
    db_tables_names = []
    db_tables_cnt = 0

    db_name = input("Database name: ")
    if db_name == "op_return":
        main()

    db_tables_cnt = input("How many tables does it have to have: ")
    if db_tables_cnt == "op_return":
        main()
    else:
        while True:
            try:
                db_tables_cnt = int(db_tables_cnt)
                break
            except:
                if type(db_tables_cnt) != int:
                    db_tables_cnt = input("ERROR: Type an integer value (1, 2, 3...) | How many tables does it have to have: ")

    cnt = 0
    while db_tables_cnt > cnt:
        db_tables_names.append(input(f"Name of the table number {cnt+1}: "))
        cnt += 1

    dbs_manager.create_database(db_name, db_tables_cnt, db_tables_names)
    database_creation_algorithm()

def database_deleting_algorithm():
    print(f"\nEzData Database Deleting Algorithm v{dd_alg_ver} | \"op_return\" at any time to return")
    db_name = (input("Name of the database to be deleted: "))
    if db_name == "op_return":
        main()

    confirmation = (input(f"Are you sure you want to delete {db_name}? (y: yes / n: no) "))
    match confirmation.upper():
        case "Y":
            dbs_manager.delete_database(db_name)
        case "op_return":
            main()
        case _:
            print("\nOperation canceled; action not confirmed by user.")
    database_deleting_algorithm()

def database_editing_algorithm():
    print(f"\nEzData Database Editing Algorithm v{de_alg_ver} | \"op_return\" at any time to return")
    db_name = (input("Name of the database to be edited: "))
    if db_name == "op_return":
        main()

    confirmation = input(f"Select {db_name}? (y: yes / n: no) ")
    match confirmation.upper():
        case "Y":
            dbs_manager.edit_database(db_name)
        case "op_return":
            main()
        case _:
            print("\nOperation canceled; action not confirmed by user.")
    database_editing_algorithm()

def ez_config():
    print("Avaible operations: \ncfg_set_path: Set the default path to manage the databases.\n")

    operation = input("Operation: ")
    match operation:
        case "cfg_set_path":
            path = input("Enter the new default path for managing the databases, from root: ")
            try:
                with open("program_info.json", "r") as file:
                    program_info = json.load(file)

                with open("program_info.json", "w+") as file:
                    program_info["dbs_path"] = path
                    json.dump(program_info, file)

                    print("Path succesfully saved.\n")

                file.close()
            except Exception as e:
                print(f"ERROR: {e}")
        case _:
            "Invalid operation."

    main()

def main():
    print(f"\n EzData v{ezdata_ver}\n")

    def get_command():
        cmd = input("Command (ez_help for help): ")
        match cmd:
            case "ez_help":
                print("ez_exit: Exit the program.")
                print("ez_create_db: Starts an setup for creating an local database.")
                print("ez_delete_db: Deletes an existing local database.")
                print("ez_edit_db: Edits an existing local database.")
                print("ez_config: Enters the EzData's configuration algorithm.\n")
                get_command()
            case "ez_exit":
                print("Thank you for using EzData! Exiting...\n")
                sys.exit()
            case "ez_create_db":
                database_creation_algorithm()
            case "ez_delete_db":
                database_deleting_algorithm()
            case "ez_edit_db":
                database_editing_algorithm()
            case "ez_config":
                ez_config()
            case _:
                print("Invalid command.\n")
                get_command()

    get_command()

main()