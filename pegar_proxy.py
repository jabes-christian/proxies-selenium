import requests
from bs4 import BeautifulSoup
import time

class BuscarProxy:
    """
    Busca proxies do free-proxy-list.net, filtra HTTPS + anonimato (anonymous/elite),
    testa com requests e grava arquivos:
      - proxies.txt (todos listados filtrados)
      - validado_proxies.txt (apenas os que responderam ao teste)
    """
    URL = "https://free-proxy-list.net/"

    def __init__(self, test_url="https://meuip.com.br/", test_timeout=8, max_test=100):
        self.test_url = test_url
        self.test_timeout = test_timeout
        self.max_test = max_test

    def buscar_lista(self):
        resp = requests.get(self.URL, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        tabela = soup.select_one("div.fpl-list table")
        proxies = []

        if not tabela or not tabela.tbody:
            return proxies
        
        for linha in tabela.tbody.find_all("tr"):
            colunas = [c.text.strip() for c in linha.find_all("td")]
            if len(colunas) < 8:
                continue
            ip, port, code, country, anonymity, google, https, last_checked = colunas[:9]
            if https.lower() == "yes" and anonymity.lower() in ("anonymous", "elite proxy"):
                proxies.append(f"{ip}:{port}")
        return proxies

    def test_proxy(self, proxy):
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        try:
            r = requests.get(self.test_url, proxies=proxies, timeout=self.test_timeout)
            return r.status_code == 200
        except Exception:
            return False

    def run(self, save_all_proxies="proxies.txt", save_proxies_validos="validado_proxies.txt"):
        print("Buscando lista de proxies...")
        all_proxies = self.buscar_lista()
        print(f"Encontrados {len(all_proxies)} proxies (filtrados HTTPS/anon).")

        with open(save_all_proxies, "w", encoding="utf-8") as f:
            for p in all_proxies:
                f.write(p + "\n")

        validos = []
        limite = min(len(all_proxies), self.max_test)
        print(f"Testando até os primeiros {limite} proxies (timeout={self.test_timeout}s)...")
        for i, p in enumerate(all_proxies[:limite], start=1):
            print(f"[{i}/{limite}] Testando {p} ... ", end="", flush=True)
            ok = self.test_proxy(p)
            if ok:
                print("OK")
                validos.append(p)
            else:
                print("FALHA")
            time.sleep(0.5)

        with open(save_proxies_validos, "w", encoding="utf-8") as f:
            for p in validos:
                f.write(p + "\n")

        print(f"Testes finalizados. Validos: {len(validos)}")
        return validos
