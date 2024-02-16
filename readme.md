# CIF Scraper

This project is designed to extract the CIF (Corporate Identification Number) of enterprises that are specified in an Excel (.xlsx) file.

## Project Structure

The project has the following structure:

- `main.py`
- `intro_func.py`
- `logic.py`

## Files Description

- `main.py`: This is the main entry point of the application. It reads the enterprises from the Excel file, retrieves the CIF for each enterprise, and writes the results to an output Excel file.
- `intro_func.py`: This file contains helper functions for reading the Excel file and extracting the list of enterprises.
- `logic.py`: This file contains the logic for retrieving the CIF of an enterprise.

## How to Run

To run the project, execute the `main.py` script. Make sure you have an Excel file in the same directory as the script. The Excel file should contain the names of the enterprises in the first column.

```sh
python main.py
```
## Dependencies

The project requires the following Python libraries:

- `pandas`: For reading and writing Excel files and manipulating data.
- `os`: For interacting with the operating system.
- `tkinter`: For rendering a warning message to the user.
- `time`: For pausing execution between requests.
- `python-dotenv`: For loading enviroment variables.

## Environment Variables

This project uses environment variables for configuration. These are the environment variables used:

- `URL_FIRST`: This is the first part of the URL used to fetch the CIF of the enterprises. 
- `URL_SECOND`: This is the second part of the URL used to fetch the CIF of the enterprises. 

### Setting Environment Variables

Environment variables can be set in a `.env` file in the root directory of the project. This file should not be committed to version control.
