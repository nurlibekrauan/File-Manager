from _pyA.utils import FileManager


def menu():
    print(
        "Creating files...\n1. Create file\n2. Create files\n3. Create directory\n4. Create directories\n5. Delete by path\b6. Delete directory"
    )
    value = int(input("Enter the choise"))
    match value:
        case 1:
            file_manager = FileManager()
            file_name = input("Enter the name of the file: ")
            file_extention = input("Enter the exctension to the file: ")
            file_manager.create_file(file_name, file_extension=file_extention)
        case 2:
            file_manager = FileManager()
            file_names = input(
                "Enter the names of the files (separated by comma): "
            ).split(",")
            file_manager.create_files(file_names)
        case 3:
            directory_name = input("Enter the name of the directory: ")
            file_manager = FileManager()
            file_manager.create_directory(directory_name)
        case 4:
            directory_names = input(
                "Enter the names of the directories (separated by comma): "
            ).split(",")
            file_manager = FileManager()
            file_manager.create_directories(directory_names)
        case 5:
            file_path = input("Enter the path to the file/directory: ")
            file_manager = FileManager()
            file_manager.delete_by_path(file_path)
        case 6:
            directory_path = input("Enter the path to the directory: ")
            file_manager = FileManager()
            file_manager.delete_directory(directory_path)
        case _:
            print("Invalid choice. Please try again.")


def main():
    menu()


if __name__ == "__main__":
    while True:
        main()
