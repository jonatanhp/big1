import requests
from bs4 import BeautifulSoup
from collections import deque

#array de registro de enlaces visitados

visited_links = set()

def search_word(word, url):
    #print("init f1")
    response = requests.get(url)

    if response.status_code  == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content_div  = soup.find('body')
        #print(type(content_div))
        #print(content_div.soup.find('div', class_='jeg_post_meta'))
        if(word in content_div.text):
            print("finded word at the url : ", url)

    else:
        print("error ")

def explore_links(init_url, lvl):
    cola = deque([(init_url,0)])
    #print("inicio")
    while cola:
        #print("2")
        actual_url, actual_lvl = cola.popleft()
        visited_links.add(actual_url)
        print(actual_lvl)
        print(lvl)
        if actual_lvl < lvl:
            #print("3ff")
            response = requests.get(actual_url)

            if response.status_code == 200:
                #print("4ff")
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links:
                    url = link['href']
                    #print("first for")
                    if url.startswith('http') and url not in visited_links:
                        #print("6ff")
                        search_word("Juliaca", url)
                        cola.append((url, actual_lvl+1))
                        visited_links.add(url)
                      





#function call
#search_word("Juliaca", "https://www.losandes.com.pe/")

explore_links("https://www.losandes.com.pe/", 2)
    


    
    