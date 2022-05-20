# butler
Clean your castle


## Prehistory
This CLI program provides functions for maintaining order on a server or home computer.

> How tired I am of looking at this trash in Downloads.  
> (c) Author

To fix this problem this program was developed in the Python language.

In fact, this program is a working prototype for a similar Golang program, but you can already use it now.

Enjoy.


## How to use
The program provides three functions:  
1. **Cleaning**  
2. **Grouping**  
3. **Archiving**

In case the first and third functions are already familiar, grouping may seem like an interesting function.

**It is important to close slashes.**

### Examples 
**Cleaning**  
`butler.exe --clean /path/to/dir/`  
Clean target dir but not delete it.

**Grouping**  
`butler.exe group --source /path/to/dir/ --target DIRNAME`  
Group up files by extensions to new directory named.  
From `--source` get path to directory where the files will be group up.  
From `--target` get new directory name where the files will be moved. Default *ALL*.  
For example, you have a lot of *.exe* files, after this command you will have one directory called *ALL.EXE* with all your *.exe* files in it.

**Archiving**  
`butler.exe --archive /path/to/dir/`  
Create zip archive in current directory for target directory.


## Golang version
[butler_go](https://github.com/CoolCoderCarl/butler_go)
