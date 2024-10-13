import sys
import dbs_manager
import json

program_info_json = open('program_info.json')
program_info = json.load(program_info_json)

ezdata_ver = program_info["versions"]["ez_data"]
dc_alg_ver = program_info["versions"]["dc_alg"]
dd_alg_ver = program_info["versions"]["dd_alg"]
de_alg_ver = program_info["versions"]["de_alg"]

program_info_json.close()


def database_creation_algorithm():
    print(f"\nEzData Database Creation Algorithm v{dc_alg_ver} | \"op_return\" at any time to return")
    db_tables_names = []
    db_tables = 0
    db_name = (input("Database name: "))
    if db_name == "op_return":
        main()

    try:
        db_tables = (input("How many tables does it have: "))
        if db_tables == "op_return":
            main()
        else:
            int(db_tables)
    except:
        while type(db_tables) != int:
            try:
                db_tables = (input("ERROR: Type an integer value (1, 2, 3...) \n How many tables does it have: "))
                if db_tables == "op_return":
                    main()
                else:
                    int(db_tables)
                break
            except:
                continue

    cnt = db_tables
    while cnt > 0:
        db_tables_names.append(input(f"Type the tables names ({cnt} remaining): "))
        if db_tables_names == "op_return":
            main()
        cnt -= 1

    dbs_manager.create_database(db_name, db_tables, db_tables_names)
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

def main():
    print(f"\n EzData v{ezdata_ver}\n")

    def get_command():
        cmd = (input("Command (ez_help for help): "))
        match cmd:
            case "ez_help":
                print("ez_exit: Exit the program.")
                print("ez_create_db: Starts an setup for creating an local database.")
                print("ez_delete_db: Deletes an existing local database.")
                print("ez_edit_db: Edits an existing local database.\n")
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
            case _:
                print("Invalid command.\n")
                get_command()

    get_command()

main()