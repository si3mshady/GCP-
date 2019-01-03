from google.cloud import translate 
from urllib.request import urlopen as URL
from bs4 import BeautifulSoup as soup
import re

url = 'http://www.lingoes.net/en/translator/langcode.htm'
html_data = URL(url)
html_soup = soup(html_data,"html.parser")
processed_soup = html_soup.findAll('tr') #parse html document with beautiful soup 
languages  = dict(re.findall(r'<tr><td>([\w-]+)\<\/td\>\<td\>(\w+)',str(processed_soup)))  #parse the html data with regex 


def translation(word,country_code):
    babel = translate.Client()
    babel_fish = babel.translate(word,target_language=country_code)
    return babel_fish


def say_something():    
    go = True 
    while go:
        word = input('Please enter a word to translate: ')        
        for key,value in languages.items():
            print(key,"-",value)
        code = input('Using the list of codes provided\nplease indicate the language code you wish to translate word:\n ')        
        translation(word,code)
        


if __name__ == '__main__':
    say_something()
#1-2-19 exploring google translate api. Simple exercises  Elliott Arnold     
        
    
    

    




