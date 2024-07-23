from typing import Union, List

import os
import logging

logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class CreateDirectory:
    """
    A class to create new directories either as a single directory or multiple directories
    at a specified path. The directory names can be strings or lists of strings.
    """
    def __init__(self, folder_name: Union[str, List[str]], dir_path: str) -> None:
        """Initializes the CreateDirectory instance with the provided folder_name and dir_path.

        Args:
            folder_name (Union[str, List[str]]): The name of the directory or list of names to be created.
            dir_path (str): The path where the directories will be created.
        """
        self.folder_name = folder_name
        self.dir_path = dir_path
        self._process()
    
    def _process(self) -> None:
        """
        Validates the directory path and creates the directories.
        Raises:
            ValueError: If the provided path is not a valid directory.
        """
        if self.path_validation() is False:
            raise ValueError("The provided path is not a valid directory")
        
        self.create_directory()
    
    def path_validation(self) -> bool:
        """
        Validates if the provided directory path exists.
        
        Returns:
            bool: True if the path is valid, otherwise False.
        """
        logging.info("Validating the path")
        if os.path.isdir(self.dir_path):
            logging.info("The path is valid")
            return True
        
        logging.error("The path is invalid")
        return False
    
    def create_directory(self) -> None:
        """
        Creates directories based on the folder_name attribute. If folder_name is a string, 
        a single directory is created. If it is a list of strings, multiple directories are created.
        
        Raises:
            TypeError: If folder_name is neither a string nor a list of strings, or if any item 
                       in the list is not a string.
        """
        if isinstance(self.folder_name, str):
            folder_name_without_whitespace = self.folder_name.replace(" ", "-")
            full_path = os.path.join(self.dir_path, folder_name_without_whitespace)
            os.makedirs(full_path, exist_ok=True)
            logging.info(f"Directory was created: {self.folder_name}")
            
            self.new_path = full_path
            
        elif isinstance(self.folder_name, list):
            
            if not all(isinstance(name, str) for name in self.folder_name):
                raise TypeError("All items in the list must be strings")
                                
            self.new_path = []
            
            for folder_name in self.folder_name:
                folder_name_without_whitespace = folder_name.replace(" ", "-")
                full_path = os.path.join(self.dir_path, folder_name_without_whitespace)
                os.makedirs(full_path, exist_ok=True)
                logging.info(f"Directory was created: {folder_name}")
                
                self.new_path.append(full_path)
                
        else:
            raise TypeError("folder_name need to be a string or a list[string]")
        
    def get_new_path(self) -> Union[str, List[str]]:
        """
        Returns the path(s) of the created directory or directories.
        
        Returns:
            Union[str, List[str]]: The path of the created directory if a single directory was created,
                                    or a list of paths if multiple directories were created.
        """
        return self.new_path
        
    def __del__(self) -> None:
        """
        Logs a message when the instance is deleted.
        """
        logging.info("Stopping the process")
        
    def __str__(self) -> str:
        """
        Returns the string representation of the directory path.
        
        Returns:
            str: The directory path.
        """
        return self.dir_path