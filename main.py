import PyPDF2
import os
def search_document(content, keyword):
    matches = []
    for line in content.splitlines():
        if keyword.lower() in line.lower():
            matches.append(line)

    return matches, len(matches)
def read_pdf(filename):
    with open(filename, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        content = ""

        for page in reader.pages:
            content += page.extract_text() or ""

    return content
try:
    filename = input("Enter document name: ")

    if filename.endswith(".pdf"):
        content = read_pdf(filename)

    elif filename.endswith(".txt"):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    else:
        print("Unsupported file format.")
        raise SystemExit

    keyword = input("What do you want to search for? ").strip()

    if not keyword:
        print("Please enter a keyword to search.")

    else:
        print("\nSearching in:", filename)

        matches, count = search_document(content, keyword)

        if matches:
            print("\nInformation found!")
            print("\nMatching lines:")

            for line in matches:
                print(line)

            print("\nTotal matching lines:", count)

        else:
            print("Sorry, that information was not found.")

except FileNotFoundError:
    print("Error: The specified file was not found.")