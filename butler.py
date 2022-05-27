import argparse
import os
import shutil
import sys
from datetime import datetime
from os.path import basename
from typing import Set
from zipfile import ZipFile

archives_extension = [".zip", ".7z", ".gz", ".bz", ".gzip", ".bzip", ".iso"]


def get_args():
    """
    Get arguments from CLI
    :return:
    """
    root_parser = argparse.ArgumentParser(
        prog="butler",
        description="""The Butler helps keep the castle clean and tidy""",
        epilog="""(c) CoolCoderCarl""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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

    return root_parser.parse_args()


def get_butler_name() -> str:
    """
    Get Butler name from sys.argv to escape it in logic
    One option for Windows OS family
    Second for Nix based OS
    :return:
    """
    if "win" in sys.platform:
        return sys.argv[0].split("\\")[-1]
    else:
        return sys.argv[0].split("/")[-1]


def get_files_extension(path_to_dir: str) -> Set:
    """
    Return list of files in target directory
    :param path_to_dir:
    :return:
    """
    list_dir = os.listdir(path_to_dir)

    files = [file for file in list_dir if os.path.isfile(path_to_dir + file)]

    result = []
    for ext in files:
        result.append("." + ext.split(".")[-1])

    result = set(result)

    return result


def moving_files(move_from: str, move_to: str):
    """
    Moved files from source to target
    Check is files ext and target directory match
    :param move_from: got from file_path in group_up_files func
    :param move_to: got from new_dir_path in group_up_files func
    :return:
    """
    file_ext = move_from.split(".")[-1]
    dir_ext = move_to.split(".")[-1]
    if file_ext.lower() == dir_ext.lower():
        shutil.move(move_from, move_to)


def clean_the_dir(path_to_clean: str):
    """
    Clean the target directory, but not delete directory itself
    :param path_to_clean:
    :return:
    """
    if get_args().clean == "/":
        exit(1)
    else:
        if len(os.listdir(path_to_clean)) == 0:
            exit(1)
        else:
            for filename in os.listdir(path_to_clean):
                path = os.path.join(path_to_clean, filename)
                if get_butler_name().lower() in (path.split("/")[-1]).lower():
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
    if get_args().source == "/":
        exit(1)
    else:
        extensions = get_files_extension(get_args().source)
        if len(os.listdir(get_args().source)) == 0:
            exit(1)
        else:
            for filename in os.listdir(get_args().source):
                if get_butler_name().lower() in filename.lower():
                    pass
                elif os.path.isdir(get_args().source + filename):
                    pass
                else:
                    for ext in extensions:
                        file_path = os.path.join(get_args().source, filename)
                        if get_args().source == ".":
                            new_dir_path = new_dir_name.upper() + ext.upper()
                        else:
                            new_dir_path = (
                                get_args().source + new_dir_name.upper() + ext.upper()
                            )
                        try:
                            os.mkdir(new_dir_path)
                        except OSError:
                            pass
                        try:
                            moving_files(file_path, new_dir_path)
                        except OSError:
                            pass


def create_archive(dir_to_archive: str):
    """
    Archive all files in target directory & add archive near the butler.exe
    Ignore files with archive extensions
    :param dir_to_archive:
    :return:
    """
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    if get_args().archive == "/":
        exit(1)
    else:
        if len(os.listdir(dir_to_archive)) == 0:
            exit(1)
        else:
            with ZipFile(str(date_time) + ".zip", "w") as zip_obj:
                for folder_name, sub_folders, filenames in os.walk(dir_to_archive):
                    for filename in filenames:
                        if get_butler_name().lower() in filename.lower():
                            pass
                        else:
                            for a_ext in archives_extension:
                                if filename.endswith(a_ext):
                                    pass
                            zip_path = os.path.join(folder_name, filename)
                            zip_obj.write(zip_path, basename(zip_path))


def combine():
    pass


if __name__ == "__main__":
    if get_args().clean:
        clean_the_dir(get_args().clean)
    elif get_args().group:
        group_up_files(get_args().target)
    elif get_args().archive:
        create_archive(get_args().archive)
