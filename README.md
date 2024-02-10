# File System Analyzer
A command-line tool developed in Python that analyzes and reports on the file system structure and usage on a Linux system.
## What it can do?
- **Directory Traversal**: The tool is able to traverse through a specified directory recursively.
- **File Type Categorization**: It can classify files into categories (e.g., text, image, empty, etc.) based on their MIME type.
- **Size Analysis**: It calculates and display the total size for each file type category.
- **File Permissions Report**: It can generate a report of files with unusual permission settings (e.g. world-writable files).
- **Directory Access Report**: It can generate a report of directories it cannot access.
- **Large Files Identification**: It can identify and list files above a certain size threshold.
- **File Tree**: It can display tree of files and directories.
## User Interface
User has ability to set parameters for CLI. There are 1 required parameter and 4 optional arguments:
#### Required:
- path to file (like `"/CloudLinuxTest"`). `"` is not required but directories with separate words must be written using `"`<br>
(like `"/CloudLinux Test"`).
>Setting only a required parameter will result just in a recursive traverse of the specified directory without any output. Consider using optional arguments with a required path in order to get some useful information.
#### Optional:
>Optional arguments can be specified in any order
- `--thr` specify threshold value for files.
- `--rep` flag to get report of file with suspicious permissions and inaccessible directories.
- `--ctg` flag to get report with categories and their sizes.
- `--dsp` flag to display file tree of traversed directory.
## Example commands
1. The next command will traverses `Telegram Desktop` folder and outputs file categories. File categories itself have names, sizes and number of files each has:<br>
```
python main.py "/home/<user>/Downloads/Telegram Desktop" --ctg
```
2. If you want to see files that are above a certain threshold value, you can specify a value in megabytes with `--thr`:<br>
```
python main.py "/home/<user>/Downloads/Telegram Desktop" --ctg --thr 50
```
3. `--rep` will print a report of files with suspicious permissions and directories the tool cannot access:<br>
```
python main.py "/home/<user>/Downloads/Telegram Desktop" --ctg --thr 50 --rep
```
4. `--dsp` is a flag that allow to generate a file tree:<br>
```
python main.py "/home/<user>/Downloads/Telegram Desktop" --ctg --thr 50 --rep --dsp
```
## Dependencies
The program itself mainly relies on 2 external libraries: `typer` for CLI interface and `magic` for file type categorization. These dependencies were installed with:
```
pip install "typer[all]"
```
and 
```
pip install python-magic
```
but all dependencies can be already found in `requirements.txt` and installed with thr next command:
```
pip install -r requirements.txt
```
