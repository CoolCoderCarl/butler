import argparse
import os, shutil


files_extension = [".txt", ".doc", ".docx", ".pdf", ".xlsx", ".bmp", ".jpg"]


def clean_the_dir(directory_path):
    for files in os.listdir(directory_path):
        path = os.path.join(directory_path, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

# def is_dir_exist():


parser = argparse.ArgumentParser(
        prog='butler',
        description='''The Butler helps keep the castle clean and tidy''',
        epilog='''(c) CoolCoderCarl'''
    )


parser.add_argument('--clean', help="Clean trash can")

parser.add_argument('--dir', help="Dir to group up the files")
args = parser.parse_args()


if args.clean:
    clean_the_dir(args.clean)
elif args.dir:
    for file in os.listdir(args.dir):
        for ext in files_extension:
            if file.endswith(ext):
                print(os.path.join(args.dir, file))
                print("ALL_" + ext.upper())
                try:
                    os.mkdir(args.dir + "ALL_" + ext.upper())
                except OSError as os_error:
                    print(os_error)
                shutil.move(os.path.join(args.dir, file), args.dir + "ALL_" + ext.upper())


