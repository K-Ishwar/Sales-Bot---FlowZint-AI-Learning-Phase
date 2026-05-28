filename = input("Enter file name: ")

try:

    with open(filename, "r") as file:
        content = file.read()

    paragraphs = content.split("\n\n")

    for index, para in enumerate(paragraphs, start=1):

        clean_para = para.strip()

        print(f"\nParagraph {index}:")
        print(clean_para)

except FileNotFoundError:
    print("File not found.")