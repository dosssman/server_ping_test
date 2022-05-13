# Linux

Requires Python 3 and root access (for the ping).

1. Elevate to root using `sudo su`

2. Install dependencies: `pip install -r requirements.txt`

3. Run `python server_ping_test.py`

This will generate a file of the form `benchresults.2022-05-13_11_54_44.pkl` to be used in the `compare_results.py` script.


# Windows 10 (Native)

1. Download Python 3 for Windows 10 from: https://www.python.org/downloads/release/python-3104/ or [Direct link](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)

2. Run the installer, make sure that "pip" is included in the install settings, and forget not to tick "Add Python to PATH".

3. Download and extract this repository to folder of your choice.

4. Start "Command Prompt" as Administrator and navigate to the previously extracted folder.

5. Execute `pip install -r requirements.txt`

6. Run `python server_ping_test.py`

This will generate a file of the form `benchresults.2022-05-13_11_54_44.pkl` to be used in the `compare_results.py` script.

7. Uninstall Python 3 and delete the downloaded files.


# Windows 10 (Git Bash)

### 1. Gitbash is required. 
- Download and install the latest Gitbash from https://git-scm.com/downloads

### 2. Installing Python 3 in Git Bash on Windows 10:
- Download and install the Windows x86-64 executable installer from https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe
   
  - Check the `Add Python 3.8 to Path` check box
  - Click `Customize installation`
  - All `Optional Features` should already be checked; click `Next`
  - Check `Install for all users`, then click `Install`
  - When prompted, allow the installer to modify your system
   
- Once installed, open a new git bash window (otherwise, the PATH change will not be in effect)
- Check python version to make sure it is installed successfully. Run in gitbash: `python -V`
######  The Latest Python 3 Release https://www.python.org/downloads/windows/

### 3. Pip is required.
- Run in gitbash to check pip version: `py -m pip --version`
- If pip is not found, please install it.

### 4. Download ZIP file and unzip to your to folder of your choice (e.g. `E:/server_ping_test-main`)
  1). Run Gitbash as administrator. (Right click Github icon, "Run as administrator")
  
  2). Open the folder. Run `cd E:/server_ping_test-main`
  
  3). Install dependencies: `pip install -r requirements.txt`
  - If you meet some version conflicts, just install the dependency one by one: `pip install <package_name>` or `py -m pip install <package_name>` (without specific version number)
  
  4). Run `python server_ping_test.py`
  
  This will generate a file of the form `benchresults.2022-05-13_11_54_44.pkl` to be used in the `compare_results.py` script.
