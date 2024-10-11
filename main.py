import sys
import dbs_manager

def database_creation_algorithm():
    print("\nEzData Database Creation Algorithm v1.0.0")
    db_tables_names = []
    db_tables = 0
    db_name = str(input("Database name: "))
    try:
        db_tables = int(input("How many tables does it have: "))
    except:
        while type(db_tables) != int:
            try:
                db_tables = int(input("ERROR: Type an integer value (1, 2, 3...) \n How many tables does it have: "))
                break
            except:
                continue

    cnt = db_tables
    while cnt > 0:
        db_tables_names.append(input(f"Type the tables names ({cnt} remaining): "))
        cnt -= 1

    dbs_manager.create_database(db_name, db_tables, db_tables_names)
    main()

def database_deleting_algorithm():
    print("\nEzData Database Deleting Algorithm v1.0.0")
    db_name = str(input("Name of the database to be deleted: "))
    confirmation = str(input(f"Are you sure you want to delete {db_name}? (y: yes / n: no) "))
    match confirmation.upper():
        case "Y":
            dbs_manager.delete_database(db_name)
        case _:
            print("\nOperation canceled; action not confirmed by user.")
    main()

def database_editing_algorithm():
    print("\nEzData Database Editing Algorithm v1.0.0")
    db_name = str(input("Name of the database to be edited: "))
    confirmation = input(f"Select {db_name}? (y: yes / n: no) ")

    match confirmation.upper():
        case "Y":
            dbs_manager.edit_database(db_name)
        case _:
            print("\nOperation canceled; action not confirmed by user.")
    main()

def main():
    print("\n EzData v0.0.2\n")

    def get_command():
        cmd = str(input("Command (ez_help for help): "))
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