from pegar_proxy import BuscarProxy
from proxy import ExecutarProxy

def main():
    buscar = BuscarProxy(test_timeout=8, max_test=90)
    proxies_validos = buscar.run(save_all_proxies="proxies.txt", save_proxies_validos="validado_proxies.txt")

    if not proxies_validos:
        print("Nenhum proxy válido encontrado. Verifique conexão ou aumente o max_test.")
        return

    selecionado = proxies_validos[0]
    print("Proxy selecionado:", selecionado)

    executar = ExecutarProxy(proxy=selecionado, headless=False, page_timeout=25)
    success = executar.open_url("https://meuip.com.br/")
    if success:
        print("Test com Selenium finalizado com sucesso (ou pelo menos tentativa feita).")
    else:
        print("Falha ao abrir com Selenium usando o proxy selecionado.")

if __name__ == "__main__":
    main()
