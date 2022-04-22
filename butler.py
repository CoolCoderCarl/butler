import argparse
import platform
import os, shutil

def is_linux():
    """
    Check is current system Linux
    :return:
    """
    if 'Linux' in platform.system():
        return True
    else:
        return False


def clean_the_dir(directory_path):
    for files in os.listdir(directory_path):
        path = os.path.join(directory_path, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


parser = argparse.ArgumentParser(
        prog='butler',
        description='''The Butler helps keep the castle clean and tidy''',
        epilog='''(c) CoolCoderCarl'''
    )


parser.add_argument('clean', help="Clean trash can")

# parser.add_argument('--dir', default="/tmp/", help="Dir to group up the files")
args = parser.parse_args()


if args.clean == 'clean':
    print('You clean it!')
    if is_linux():
        clean_the_dir('/test/')
    # Clean func
# elif args.dir == '/tmp/':
#     print('You group up it!')
#     Group up dir
else:
    print('Something wrong')

