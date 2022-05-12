import argparse
import os
import shutil

files_extension = [
    ".txt",
    ".doc",
    ".docx",
    ".pdf",
    ".xlsx",
    ".bmp",
    ".jpg",
    ".rtf",
    ".pptx",
    ".conf",
    ".cfg",
    ".net",
    ".deny",
    ".allow",
]

target_dir_name = "ALL"


def clean_the_dir(directory_path):
    for files in os.listdir(directory_path):
        path = os.path.join(directory_path, files)
        if files == os.path.basename(__file__):
            pass
        else:
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)


def group_up_files(new_dir_name):
    print(new_dir_name)
    for file in os.listdir(args.dir):
        for ext in files_extension:
            if file.endswith(ext):
                file_path = os.path.join(args.dir, file)
                print(file_path)
                new_dir_path = args.dir + new_dir_name + ext.upper()
                print(new_dir_path)
                try:
                    os.mkdir(new_dir_path)
                except OSError as os_error:
                    print(os_error)
                shutil.move(file_path, new_dir_path)


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
args = parser.parse_args()


if __name__ == "__main__":
    if args.clean:
        clean_the_dir(args.clean)
    elif args.dir:
        group_up_files(target_dir_name)
