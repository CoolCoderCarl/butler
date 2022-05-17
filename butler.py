import argparse
import os
import shutil
from datetime import datetime
from os.path import basename
from zipfile import ZipFile

files_extension = [
    ".txt",
    ".ini",
    ".doc",
    ".docx",
    ".pdf",
    ".xlsx",
    ".xls",
    ".pptx",
    ".zip",
    ".7z",
    ".gz",
    ".bz",
    ".gzip",
    ".bzip",
    ".iso",
    ".bmp",
    ".jpg",
    ".png",
    ".exe",
    ".msi",
    ".msu",
    ".rtf",
    ".conf",
    ".cfg",
    ".net",
    ".deny",
    ".allow",
]

archives_extension = [".zip", ".7z", ".gz", ".bz", ".gzip", ".bzip"]

target_dir_name = "ALL"


def clean_the_dir(path_to_clean: str):
    if args.clean == "/":
        print("It is totally not great idea to remove all things")
        exit(1)
    else:
        for filename in os.listdir(path_to_clean):
            path = os.path.join(path_to_clean, filename)
            if "butler" in (path.split("/")[-1]):
                print("Skipped " + path.split("/")[-1])
            else:
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)


def group_up_files(new_dir_name: str):
    for filename in os.listdir(args.dir):
        if "butler" in filename:
            print("Skipped " + filename)
        else:
            for ext in files_extension:
                if filename.endswith(ext):
                    file_path = os.path.join(args.dir, filename)
                    if args.dir == ".":
                        new_dir_path = new_dir_name + ext.upper()
                    else:
                        new_dir_path = args.dir + new_dir_name + ext.upper()
                    try:
                        os.mkdir(new_dir_path)
                    except OSError:
                        pass
                    shutil.move(file_path, new_dir_path)


def create_archive(dir_to_archive: str):
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    with ZipFile(str(date_time) + ".zip", "w") as zip_obj:
        for folder_name, sub_folders, filenames in os.walk(dir_to_archive):
            for filename in filenames:
                if "butler" in filename:
                    print("Skipped " + filename)
                else:
                    for a_ext in archives_extension:
                        if filename.endswith(a_ext):
                            pass
                    zip_path = os.path.join(folder_name, filename)
                    zip_obj.write(zip_path, basename(zip_path))


parser = argparse.ArgumentParser(
    prog="butler",
    description="""The Butler helps keep the castle clean and tidy""",
    epilog="""(c) CoolCoderCarl""",
)

parser.add_argument(
    "--clean", help="Clean target directory. Example /tmp/, both slash required"
)

parser.add_argument(
    "--dir", help="Dir to group up the files. Example /tmp/, both slash required"
)

parser.add_argument(
    "--archive",
    help="Create archive from target directory. Example /tmp/, both slash required",
)

args = parser.parse_args()


if __name__ == "__main__":
    if args.clean:
        clean_the_dir(args.clean)
    elif args.dir:
        group_up_files(target_dir_name)
    elif args.archive:
        create_archive(args.archive)
