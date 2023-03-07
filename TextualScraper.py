from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# lista dei siti in cui cercare
sites = ["amazon.it", "idealo.it", "trovaprezzi.it"]

# Inizializzazione del webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Esecuzione del browser in background
chrome_options.add_argument("--disable-web-security") # Disabilita la sicurezza web
chrome_options.add_argument("--allow-running-insecure-content") # Consente l'esecuzione di contenuti non sicuri
chrome_options.add_argument("--disable-extensions") # Disabilita le estensioni
chrome_options.add_argument("--disable-gpu") # Disabilita l'accelerazione GPU
chrome_options.add_argument("--disable-dev-shm-usage") # Disabilita l'uso della memoria condivisa /dev/shm
chrome_options.add_argument("--no-sandbox") # Disabilita il sandbox del browser
chrome_options.add_argument("--ignore-certificate-errors") # Ignora gli errori del certificato SSL
chrome_options.add_argument("--allow-file-access-from-files") # Consente l'accesso ai file locali
chrome_options.add_argument("--disable-notifications") # Disabilita le notifiche del browser
chrome_options.add_argument("--disable-popup-blocking") # Disabilita il blocco dei popup
chrome_options.add_argument("--start-maximized") # Massimizza la finestra del browser all'avvio
chrome_options.add_argument("--ignore-mime-types") # Ignora i MIME type
driver = webdriver.Chrome(options=chrome_options)

def search_urls(query, url):
    urls = []
    for site in sites:
        if site in url:
            urls.append(url)
            break
    return urls

def scrape_prices(query):
    for site in sites:
        for url in search(query + " site:" + site, stop=1):
            print("URL trovato:", url)
            urls = search_urls(query, url)
            for url in urls:
                driver.get(url)
                sleep(3) # attendiamo che la pagina sia completamente caricata
                try:
                    # Ricerca del prezzo tramite xpath
                    price = driver.find_element_by_xpath("(//span[@class='a-price-whole'])[1]/text()")[0]
                    price = price_element.text
                    print(f"Prezzo trovato per {url}: {price.text}")
                except:
                    print(f"Prezzo non trovato per {url}")

if __name__ == "__main__":
    query = "RTX 4070 Ti"
    scrape_prices(query)
