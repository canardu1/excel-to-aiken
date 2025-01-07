#!/usr/bin/env python3
import pandas as pd
import sys
import os

def convert_excel_to_aiken(excel_file, output_dir=None):
    """
    Convert Excel file to Aiken format, separating questions by argument.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        # Print column names for debugging
        print("Found columns in Excel file:")
        for col in df.columns:
            print(f"- {col}")
        
        # Create output directory if not specified
        if output_dir is None:
            output_dir = os.path.splitext(excel_file)[0] + '_aiken'
        os.makedirs(output_dir, exist_ok=True)
        
        # Group by argument
        grouped = df.groupby('Sulla base degli articoli di codice civile mostrati nel documento')
        
        for argument, group in grouped:
            # Create a safe filename from the argument
            safe_filename = "".join(x for x in str(argument) if x.isalnum() or x in (' ', '-', '_')).rstrip()
            output_file = os.path.join(output_dir, f'{safe_filename}.txt')
            
            with open(output_file, 'w', encoding='utf-8') as f:
                for idx, row in group.iterrows():
                    # Write question
                    f.write(f"{row['Domanda']}\n")
                    
                    # Write options
                    if pd.notna(row['RispostaA']):
                        f.write(f"A) {row['RispostaA']}\n")
                    if pd.notna(row['RispostaB']):
                        f.write(f"B) {row['RispostaB']}\n")
                    if pd.notna(row['RispostaC']):
                        f.write(f"C) {row['RispostaC']}\n")
                    if pd.notna(row['RispostaD']):
                        f.write(f"D) {row['RispostaD']}\n")
                    
                    # Write correct answer
                    f.write(f"ANSWER: {row['Risposta Corretta']}\n\n")
        
        print(f"Successfully converted {excel_file} to Aiken format.")
        print(f"Output files saved in directory: {output_dir}")
        return True
        
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python excel_to_aiken.py <excel_file> [output_directory]")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(excel_file):
        print(f"Error: File {excel_file} not found")
        sys.exit(1)
    
    convert_excel_to_aiken(excel_file, output_dir)

if __name__ == "__main__":
    main()
