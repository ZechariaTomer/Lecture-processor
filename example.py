"""
This script processes a text file using the
TextProcessor class and saves the processed output to a new file.
"""

from pathlib import Path
from src.processor import TextProcessor

def main():
    """
    Main function to process a text file using the TextProcessor class.
    It reads the input file, processes it, and saves the output to the specified location.
    """
    processor = TextProcessor()

    # Define input and output file paths
    input_file = Path("data/raw/kinyani_tora_part_a.txt")
    output_file = Path("data/processed/kinyani_tora_part_a_processed.txt")

    # Ensure the output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Process the input file and save the result
    processor.process_file(input_file, output_file)
    print("File processed successfully!")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()
