# butler
Clean your castle


## Prehistory
This CLI program provides functions for maintaining order on a server or home computer.

The author was tired of watching how a dump is constantly formed in his Downloads directory (and not only) and he decided to end it.

For this purpose this program was developed in the Python language.

In fact, this program is a working prototype for a similar Golang program, but you can already use it now.

Enjoy.


## How to use
The program provides three functions:  
**Cleaning**  
**Grouping**  
**Archiving**

In case the first and third functions are already familiar, grouping may seem like an interesting function.

### In order  
**Cleaning**  
`butler.exe --clean /path/to/dir/`  
Clean target dir. It is important to close slashes.

**Grouping**  
`butler.exe --dir /path/to/dir/`  
Group up files by extensions to new directory named *ALL*.*EXT*.  
For example, you have a lot of *.exe* files, after this command you will have one directory called *ALL.EXE* with all your *.exe* files in it.  
It is important to close slashes.

**Archiving**  
`butler.exe --archive /path/to/dir/`  
Create zip archive in current directory for target directory. It is important to close slashes.


## Golang version
[butler_go](https://github.com/CoolCoderCarl/butler_go)
