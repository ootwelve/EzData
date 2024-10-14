import sqlite3
import os
import json

program_info_json = open('program_info.json')
program_info = json.load(program_info_json)

operations_path = program_info["dbs_path"]
if operations_path == "":
    operations_path = os.getcwd()

program_info_json.close()

def create_database(db_name, tables, tables_names):
    database = sqlite3.connect(f"{operations_path}/{db_name}.db")

    try:
        ciclo = 0
        current_table = 0
        while current_table < tables:
            for n in tables_names:
                database.execute(f"CREATE TABLE IF NOT EXISTS {tables_names[ciclo]}(id STRING)")
                ciclo += 1
                current_table += 1
        print("\nDatabase succesfully created. Returning...")
    except Exception as e:
        print(f"ERROR: {e}")
        create_database(db_name, tables, tables_names)

def delete_database(db_name):
    print(f"Deleting {db_name}...")
    try:
        os.remove(f"{operations_path}/{db_name}.db")
        print("\nDatabase succesfully deleted. Returning...")
    except Exception as e:
        print(f"ERROR: {e}")

def edit_database(db_name):
    print("Avaible operations:\ndb_add_table: Add a new table to the selected database;\ndb_delete_table: Delete an existing table.\n")
    operation = input("Operation: ")

    match operation:
        case "db_add_table":
            database = sqlite3.connect(f"{operations_path}/{db_name}.db")
            table_name = input("Name of the table to create: ")

            print("Adding table to the database...")
            database.execute(f"CREATE TABLE IF NOT EXISTS {table_name}(id STRING)")
            print("\nTable succesfully created. Returning...\n")
        case "db_delete_table":
            database = sqlite3.connect(f"{operations_path}/{db_name}.db")
            table_name = input("Name of the table to delete: ")

            confirmation = input(f"Do you really want to delete {table_name} from {db_name}? (y: yes / n: no) ")
            match confirmation.upper():
                case "Y":
                    print("Deleting table...")
                    try:
                        database.execute(f"DROP TABLE IF EXISTS {db_name}")
                        print("\nTable succesfully deleted. Returning...")
                    except Exception as e:
                        print(f"ERROR: {e}")
                        edit_database(db_name)
                case _:
                    print("\nOperation canceled; action not confirmed by user.")
        case _:
            print("Invalid operation.")
            edit_database(db_name)