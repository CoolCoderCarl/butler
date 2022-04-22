import argparse
import os, shutil


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


parser.add_argument('--clean', help="Clean trash can")

# parser.add_argument('--dir', default="/tmp/", help="Dir to group up the files")
args = parser.parse_args()


if args.clean:
    clean_the_dir(args.clean)
# elif args.dir == '/tmp/':
#     print('You group up it!')
#     Group up dir

