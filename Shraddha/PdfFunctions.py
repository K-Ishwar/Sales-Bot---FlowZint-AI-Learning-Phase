
try:
    # Open file using with
    with open("file1.txt", "r") as file:

        # Read all lines
        lines = file.readlines()

        # Clean each line using list comprehension
        cleaned_lines = [
            line.strip().replace(" ", "_")
            for line in lines
            if line.strip() != ""
        ]

        # Join all cleaned lines
        final_text = " | ".join(cleaned_lines)

        print("Processed Text:")
        print(final_text)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)
