from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class ExecutarProxy:

    def __init__(self, proxy, headless=False, page_timeout=30):
        self.proxy = proxy
        self.headless = headless
        self.page_timeout = page_timeout
        self.driver = None

    def _build_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server=http://{self.proxy}')

        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")
        chrome_options.add_argument("--allow-insecure-localhost")

        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        if self.headless:
            chrome_options.add_argument("--headless=new") 

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.maximize_window()
        except Exception:
            pass
        driver.set_page_load_timeout(self.page_timeout)
        return driver

    def open_url(self, url="https://meuip.com.br/"):
        try:
            print(f"Abrindo Chrome com proxy {self.proxy} ...")
            self.driver = self._build_driver()
            self.driver.get(url)
            print("Página carregada (ou carregamento iniciado).")
            time.sleep(10)
            return True
        
        except Exception as e:
            print("Erro ao abrir a página:", e)
            return False
        
        finally:
            if self.driver:
                time.sleep(10)
                try:
                    self.driver.quit()
                except Exception:
                    pass
