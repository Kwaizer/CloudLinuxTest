# File System Analyzer
A command-line tool developed in Python that analyzes and reports on the file system structure and usage on a Linux system.
## What it can do?
- **Directory Traversal**: The tool is able to traverse through a specified directory recursively.
- **File Type Categorization**: It can classify files into categories (e.g., text, image, empty, etc.) based on their extensions or file signatures.
- **Size Analysis**: It calculates and display the total size for each file type category.
- **File Permissions Report**: It can generate a report of files with unusual permission settings (e.g., world-writable files).
- **Directory Access Report**: It can generate a report of directories it cannot access.
- **Large Files Identification**: It can identify and list files above a certain size threshold.
- **File tree**: It can display tree of files and directories.
## User Interface
User has ability to set parameters for CLI. There is 1 required parameter and 4 optional arguments:
#### Required:
- path to file like `"/CloudLinuxTest"`. `"` is not required but directories with separate words must be written using `"` (like `"CloudLinux Test"`).
#### Optional:
>Optional arguments can be specified in any order
- `--thr` specify threshold value for files.
- `--rep` flag to get report of file with suspicious permissions and inaccessible directories.
- `--ctg` flag to get report with categories and their sizes.
- `--dsp` flag to display file tree of traversed directory.
