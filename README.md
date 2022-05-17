# butler
Clean your castle


## Prehistory
This CLI program provides functions for maintaining order on a server or home computer.

The author was tired of watching how a dump is constantly formed in his Downloads directory (and not only) and he decided to end it.

For this purpose this program was developed in the Python language.

In fact, this program is a working prototype for a similar program in golang, but you can already use it now.

You can download it and enjoy

## How to use
The program provides three functions:  
**Cleaning**  
**Grouping**  
**Archiving**

In case the first and third functions are already familiar, grouping may seem like an interesting function.

In order  
**Cleaning**  
`butler.exe --clean /path/to/dir/`  
Clean target dir. It is important to close slash.

**Grouping**  
`butler.exe --dir /path/to/dir/`  
Group up files by extensions to new directory named *ALL*.*EXT*.  
For example, you have a lot of *.exe* files, after this command you will have one directory called *ALL.EXE* with all your *.exe* files in it.
It is important to close slash.

**Archiving**  
`butler.exe --archive /path/to/dir/`  
Create zip archive in current directory for target directory. It is important to close slash.
