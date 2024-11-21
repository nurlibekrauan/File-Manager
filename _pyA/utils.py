import os
import logging
from _pyA.common import configur_logging


configur_logging(logging.DEBUG)

class FileManager:
    @staticmethod
    def create_directory(directory_path):
        """Создаёт директорию, если её не существует."""
        try:
            os.makedirs(directory_path, exist_ok=True)
            logging.debug(f"Directory {directory_path} created")
        except Exception as e:
            logging.error(f"Error creating directory {directory_path}: {str(e)}")

    @staticmethod
    def create_file(file_path, directory=None, file_extension=".py"):
        """
        Создаёт файл в указанной директории с заданным расширением.
        Если директория не указана, используется текущая директория.
        """
        if not file_path:
            logging.error("File path cannot be empty")
            return

        if directory is None:
            directory = os.getcwd()

        try:
            # Формируем полный путь к файлу
            if "." not in os.path.basename(file_path):
                file_path = os.path.join(directory, file_path + file_extension)

            # Проверяем существование файла
            if os.path.exists(file_path):
                logging.warning(f"File {file_path} already exists")
                return

            # Создаём файл
            with open(file_path, "w") as file:
                pass
            logging.debug(f"File {file_path} created")
        except Exception as e:
            logging.error(f"Error creating file {file_path}: {str(e)}")

    @staticmethod
    def create_files(files, file_extension=".py", directory=None):
        """
        Создаёт несколько файлов в указанной директории с заданным расширением.
        Если директория не указана, используется текущая директория.
        """
        if not files:
            logging.error("Files list cannot be empty")
            return

        if directory is None:
            directory = os.getcwd()

        for file_name in files:
            try:
                FileManager.create_file(file_name, directory=directory, file_extension=file_extension)
            except Exception as e:
                logging.error(f"Error creating file {file_name}: {str(e)}")

    @staticmethod
    def create_directories(directories):
        """
        Создаёт несколько директорий.
        """
        if not directories:
            logging.error("Directories list cannot be empty")
            return

        for directory_path in directories:
            try:
                FileManager.create_directory(directory_path)
            except Exception as e:
                logging.error(f"Error creating directory {directory_path}: {str(e)}")
    @staticmethod
    def delete_file(file_path):
        """
        Удаляет указанный файл.
        """
        if not file_path:
            logging.error("File path cannot be empty")
            return
        if not os.path.exists(file_path):
            logging.warning(f"File {file_path} does not exist")
            return
        os.remove(file_path)
    @staticmethod
    def delete_directory(directory_name):
        """
        Удаляет указанную директорию и все её содержимое.
        """
        if not directory_name:
            logging.error("Directory name cannot be empty")
            return
        if not os.path.exists(directory_name):
            logging.warning(f"Directory {directory_name} does not exist")
            return
        try:
            for root, dirs, files in os.walk(directory_name, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(directory_name)
            logging.debug(f"Directory {directory_name} deleted")
        except Exception as e:
            logging.error(f"Error deleting directory {directory_name}: {str(e)}")



# Пример использования
if __name__ == "__main__":
    FileManager.create_directory("test_dir")
    FileManager.create_file("test_file", directory="test_dir")
    FileManager.create_files(["file1", "file2"], directory="test_dir")
    FileManager.create_directories(["dir1", "dir2", "dir3"])
