# A script to demonstrate Python File-handling operations.
# It will be copying & renaming files of multiple extensions.

import shutil
import re
from pathlib import Path


# A function to copy & rename the files from one folder to a new folder
def doc_renamer(current_dir, new_dir, extensions=("*.pdf",)):
    for ext in extensions:
        doc_files_list = list(current_dir.glob(ext))
        for doc in doc_files_list:
            original_file_path = Path(doc)
            new_file_name = current_dir.name + "#" + doc.name
            new_file_path = Path(new_dir / new_file_name)

            if not new_file_path.exists():
                print(f'Copying {doc.name} to {new_dir.name + "/"}.')

                # A call to shutil.copy(),
                # which copies & renames the file to specified name
                shutil.copy(original_file_path, new_file_path)
                print(f'SUCCESS: File {doc.name} renamed to {new_file_name}.')


if __name__ == "__main__":
    # Declaring constants
    HOME_DIR = Path.home()  # Saves home directory of user
    WORKSPACE_DIR = Path(str(HOME_DIR) + r'\Downloads\my_FLAP3T_workspace')
    ORIGINAL_SRC_FILES_DIR = Path(str(WORKSPACE_DIR) + r'\all_flap3t_LNIs')
    RENAMED_DOCS_DIR = Path(str(WORKSPACE_DIR) + r'\all_flap3t_renamed_docs')
    LNI_REGEX_PATTERN = r'(?:\w{4}\-){4}\d{5}\-\d{2}'
    EXTENSIONS = ("*.pdf", "*.docx")

    # A condition to check, if path of original files is present
    if not ORIGINAL_SRC_FILES_DIR.is_dir():
        raise FileNotFoundError('No folder exists at the location specified. Please give a proper path.')
    else:
        print(f'Originals located at: {ORIGINAL_SRC_FILES_DIR}')

        # A condition to create a folder if not exists, for storing unique pdfs
        # and if already exists, doesn't raise any FileExistsError
        RENAMED_DOCS_DIR.mkdir(parents=True, exist_ok=True)

        # Step _1_ Iterate over all the sub-folders in "ORIGINAL_SRC_FILES_DIR"
        # and call the doc_renamer() on each folder
        for item in ORIGINAL_SRC_FILES_DIR.iterdir():
            if item.is_dir() and re.match(LNI_REGEX_PATTERN, item.name):
                doc_renamer(item, RENAMED_DOCS_DIR, EXTENSIONS)
