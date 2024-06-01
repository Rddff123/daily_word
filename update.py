'''import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Example HTML data
html_data = requests.get('https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}).text

# Create BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all list items
items = soup.find_all('li')
count = 0
with open('words.txt', 'w') as file:
# Iterate over the list items
    for item in items:
        if count > 33:
                # Extract word
            try:
                word = item.find('a').text.strip()
                
                # Extract part of speech if available
                pos_element = item.find('span', class_='pos')
                if pos_element:
                    pos = pos_element.text.strip()
                else:
                    pos = "N/A"
            except AttributeError:
                print('Program is finished')
                break

            # Print the result
            print("Word:", word)
            print("Part of Speech:", pos)
            print()
            file.write("Word: {}\n".format(word))
            file.write("Part of Speech: {}\n".format(pos))
            file.write("\n")                    
        count += 1'''
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Example HTML data
html_data = requests.get('https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}).text

# Create BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all list items
items = soup.find_all('li')
count = 0
with open('words.txt', 'w') as file:
    file.write('The list is from Oxford 3000\n\n')
    # Iterate over the list items
    
    for item in tqdm(items, desc='Progress', unit='words '):
        if count > 33:
            try:
                # Extract word
                word = item.find('a').text.strip()

                # Extract part of speech if available
                pos_element = item.find('span', class_='pos')
                if pos_element:
                    pos = pos_element.text.strip()
                else:
                    pos = "N/A"
            except AttributeError:
                break

            # Write the result to the file
            file.write("Word: {}\n".format(word))
            file.write("Part of Speech: {}\n".format(pos))
            file.write("\n")
        count += 1

print("Words and parts of speech have been written to 'words.txt'.")
input('Now run another file to generate random words :) \n')