# Excel to Aiken Format Converter

This script converts Excel files containing quiz questions into Aiken format, which is commonly used in learning management systems like Moodle. It will create separate Aiken files for each argument/topic.

## Requirements

- Python 3.x
- pandas
- openpyxl

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Excel File Format

Your Excel file should have the following columns:
- Domanda: The question text
- Risposta A: First answer option
- Risposta B: Second answer option
- Risposta C: Third answer option
- Risposta D: Fourth answer option
- Risposta Corretta: The letter of the correct answer (A, B, C, or D)
- Sulla base degli articoli di codice civile mostrati nel documento: The argument/topic that will be used to separate questions into different files

## Usage

```bash
python excel_to_aiken.py input.xlsx [output_directory]
```

If no output directory is specified, the script will create a directory with the same name as the input file with '_aiken' appended.

The script will create separate .txt files for each unique argument in the 'Sulla base degli articoli di codice civile mostrati nel documento' column.
