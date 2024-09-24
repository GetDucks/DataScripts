This tool detects the file type by checking the file extension (.xls, .xlsx, .csv, .json) and loads the file accordingly using pandas.
It prints metadata about the file like the number of rows and columns, data types, column names, and missing values.
Support for CSV, Excel, and JSON Files:
For Excel files (.xls, .xlsx), it parses each sheet.
For CSV files (.csv), it loads and displays metadata directly.
For JSON files (.json), it also loads and displays metadata.
Error Handling:
If the file type is unsupported, it prints an error message.

1. Download this file to your local system.
2. Move to the directory of the python script and run this command "chmod +x your_script.py".
3. Run "echo $PATH" to find check your directory path.
4. Move your script file to the bin directory (command example: sudo mv your_script.py /usr/local/bin/)
5. If you want to run the script without the .py extention use "sudo mv your_script.py your_script"

