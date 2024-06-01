import random,re
user_resp=0
# Read the words.txt file
while user_resp != 'q':
    with open('words.txt', 'r') as file:
        words = file.readlines()
    words = ' '.join(words)
    word_list = re.findall('Word: (.*?)\n',words)
    random_num = random.randint(0,len(word_list))
    random_word = word_list[random_num]

    from requests import *
    from bs4 import BeautifulSoup

    html_content_original = get(f'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{random_word}',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
    html_content = html_content_original.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    pos_list = soup.find_all('span', class_='pos dpos')
    extracted_pos = [' '.join(pos.stripped_strings) for pos in pos_list]
    # Find all div elements with class "def ddef_d db"
    div_elements = soup.find_all('div', class_='def ddef_d db')

    # Extract the text from the div elements and add spaces
    extracted_text = [' '.join(div.stripped_strings) for div in div_elements]
    print('------Generate Word--------')
    # Print the extracted text
    print(random_word)
    for pos in extracted_pos:
        print(pos,end=' ')
    print()
    count = 1
    for meaning in extracted_text:
        print(f'{count}. {meaning}\n')
        count+=1
    print('-----------------------------')
    user_resp = input('Continue? Q to exit').lower()