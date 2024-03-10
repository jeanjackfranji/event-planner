import os
from bs4 import BeautifulSoup


def format_html_file(file_path):
    with open(file_path, "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    formatted_html = soup.prettify()

    with open(file_path, "w") as file:
        file.write(formatted_html)


def format_html_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".html"):
            file_path = os.path.join(directory_path, filename)
            format_html_file(file_path)
            print(f"Formatted: {filename}")


def main():
    templates_directory = "eventplannerdb/templates"
    format_html_directory(templates_directory)


if __name__ == "__main__":
    main()
