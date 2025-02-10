# README

## Project: Holberton School - Higher Level Programming

**Author**: Matteo Foti

This project contains a series of Python functions for file manipulation and JSON serialization. The functions are organized in the `python-input_output` directory.

### Features

Here is an overview of the functionalities provided by the various functions in the project:

1. **Read a file**
   - **Prototype**: `def read_file(filename="")`
   - Reads a text file (UTF8) and prints it to stdout.
   - Uses the `with` statement.
   - Does not handle exceptions related to permissions or the absence of the file.

2. **Write to a file**
   - **Prototype**: `def write_file(filename="", text="")`
   - Writes a string to a text file (UTF8) and returns the number of characters written.
   - Uses the `with` statement.
   - Creates the file if it does not exist and overwrites its content if it already exists.

3. **Append to a file**
   - **Prototype**: `def append_write(filename="", text="")`
   - Appends a string at the end of a text file (UTF8) and returns the number of characters added.
   - Uses the `with` statement.
   - Creates the file if it does not exist.
