import argparse
import os
import shutil
import sys
from datetime import datetime
from os.path import basename
from typing import List
from zipfile import ZipFile


def butler_name():
    if "win" in sys.platform:
        return sys.argv[0].split("\\")[-1]
    else:
        return sys.argv[0].split("/")[-1]


# files_extension = [
#     ".txt",
#     ".ini",
#     ".md",
#     ".doc",
#     ".docx",
#     ".rtf",
#     ".pdf",
#     ".xlsx",
#     ".xls",
#     ".pptx",
#     ".zip",
#     ".7z",
#     ".gz",
#     ".bz",
#     ".gzip",
#     ".bzip",
#     ".iso",
#     ".mkv",
#     ".mov",
#     ".mp4",
#     ".bmp",
#     ".jpg",
#     ".png",
#     ".exe",
#     ".msi",
#     ".msu",
#     ".conf",
#     ".cfg",
#     ".net",
#     ".deny",
#     ".allow",
# ]

archives_extension = [".zip", ".7z", ".gz", ".bz", ".gzip", ".bzip", ".iso"]


def clean_the_dir(path_to_clean: str):
    """
    Clean the target directory, but not delete directory itself
    :param path_to_clean:
    :return:
    """
    if args.clean == "/":
        exit(1)
    else:
        for filename in os.listdir(path_to_clean):
            path = os.path.join(path_to_clean, filename)
            if butler_name().lower() in (path.split("/")[-1]).lower():
                pass
            else:
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)


def group_up_files(new_dir_name: str):
    """
    Group up files in target directory
    Create directory for files in target directory with ALL.EXT template according the files extensions
    Move all files to relevant directory
    :param new_dir_name:
    :return:
    """
    if args.source == "/":
        exit(1)
    else:
        for filename in os.listdir(args.source):
            if butler_name().lower() in filename.lower():
                pass
            else:
                # FIX
                for ext in files_extension:
                    if filename.endswith(ext):
                        file_path = os.path.join(args.source, filename)
                        if args.source == ".":
                            new_dir_path = new_dir_name.upper() + ext.upper()
                        else:
                            new_dir_path = (
                                args.source + new_dir_name.upper() + ext.upper()
                            )
                        try:
                            os.mkdir(new_dir_path)
                        except OSError:
                            pass
                        try:
                            shutil.move(file_path, new_dir_path)
                        except OSError as oserr:
                            print(
                                "File" + filename + "already exist in " + new_dir_path
                            )
                            print(oserr)


def create_archive(dir_to_archive: str):
    """
    Archive all files in target directory & add archive near the butler.exe
    Ignore files with archive extensions
    :param dir_to_archive:
    :return:
    """
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    if args.archive == "/":
        exit(1)
    else:
        with ZipFile(str(date_time) + ".zip", "w") as zip_obj:
            for folder_name, sub_folders, filenames in os.walk(dir_to_archive):
                for filename in filenames:
                    if butler_name().lower() in filename.lower():
                        pass
                    else:
                        for a_ext in archives_extension:
                            if filename.endswith(a_ext):
                                pass
                        zip_path = os.path.join(folder_name, filename)
                        zip_obj.write(zip_path, basename(zip_path))


root_parser = argparse.ArgumentParser(
    prog="butler",
    description="""The Butler helps keep the castle clean and tidy""",
    epilog="""(c) CoolCoderCarl""",
)

root_parser.add_argument(
    "-c",
    "--clean",
    help="Clean target directory. Example /tmp/, both slash required",
    type=str,
)

group_up_subparser = root_parser.add_subparsers(
    title="group_up_subparser",
    dest="group",
    help="Group up files in source dir with target dir name",
)

group_up_parser = group_up_subparser.add_parser(
    "group", help="Dir to group up the files."
)
group_up_parser.add_argument(
    "--source", help="Source dir name. Example /tmp/, both slash required", type=str
)
group_up_parser.add_argument(
    "--target", help="Target dir name. Example ALL", default="ALL", type=str
)


root_parser.add_argument(
    "-a",
    "--archive",
    help="Create archive from target directory. Example /tmp/, both slash required",
    type=str,
)

args = root_parser.parse_args()


def get_files_extension(path_to_dir: str) -> List:
    """
    Return list of files in target directory
    :param path_to_dir:
    :return:
    """
    list_dir = os.listdir(path_to_dir)

    files_extension = [
        file for file in list_dir if os.path.isfile("/test/test/" + file)
    ]

    result = []
    for ext in files_extension:
        result.append(ext.split(".")[-1])

    return result


if __name__ == "__main__":
    # if args.clean:
    #     clean_the_dir(args.clean)
    # elif args.group:
    #     group_up_files(args.target)
    # elif args.archive:
    #     create_archive(args.archive)
    print(get_files_extension("/test/test/"))
