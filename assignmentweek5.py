import os

def main():
    # Ask the user for the input file path
    file_path = input("Enter the path to the file you want to read: ").strip()

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("Error: File not found. Please check the path and try again.")
        return

    try:
        # Open and read the file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print("File read successfully.")

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create the output file name (e.g., adds _modified before the extension)
        base, ext = os.path.splitext(file_path)
        output_file = base + "_modified" + ext

        # Write the modified content to the new file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(modified_content)

        print(f"Modified file saved as: {output_file}")

    except UnicodeDecodeError:
        print("Error: Could not decode the file. Make sure it's a readable text file.")
    except PermissionError:
        print("Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()