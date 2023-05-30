import os
import re
import requests

def extract_pattern(text, pattern):
    return re.findall(pattern, text)

def save_to_file(data, filename):
    file_path = input(f"Enter the file path to save '{filename}': ")
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))
    return file_path

def main():
    url = input("Enter the website URL: ")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        html_content = response.text

        phone_numbers = extract_pattern(html_content, r"234[789][01]\d{8}\b")
        emails = extract_pattern(html_content, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        links = extract_pattern(html_content,  r'<a\s+(?:[^>])?href="([^"])"')

        save_to_file(phone_numbers, 'phone_numbers.txt')
        save_to_file(emails, 'emails.txt')
        save_to_file(links, 'links.txt')

        print("Extraction complete. Phone numbers, emails, and links saved to separate files.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while retrieving the webpage: {e}")

main()
