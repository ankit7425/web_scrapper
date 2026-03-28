#python data scraper project using all the concepts of python 
#This project is a simple web scraper that collects data from a website and saves it to a CSV file.
#The project uses the following concepts of Python:
#1. Requests library to make HTTP requests
#2. BeautifulSoup library to parse HTML content
#3. CSV library to write data to a CSV file
#4. Exception handling to handle errors
#5. Functions to organize code
#6. List comprehensions to create lists
import requests
from bs4 import BeautifulSoup   
import csv
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        
        # Example: Scrape all the headings from the website
        headings = soup.find_all('h2')
        data = [heading.text.strip() for heading in headings]
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
def save_to_csv(data, filename):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Heading'])  # Write the header
            for item in data:
                writer.writerow([item])  # Write each heading as a new row
    except IOError as e:
        print(f"An error occurred while writing to the CSV file: {e}")
if __name__ == "__main__":
    url = input("Enter the website URL: ")   # Replace with the target website URL
    data = scrape_website(url)
    if data:
        save_to_csv(data, 'headings.csv')
        print("Data has been saved to headings.csv")
    else:
        print("No data to save.")
