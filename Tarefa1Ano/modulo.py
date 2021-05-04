import re
import os
import sys

try:
    import requests

    REQUESTS_FOUND = True
except ModuleNotFoundError:
    REQUESTS_FOUND = False


def resolver_url(url, url_base):

    url = re.sub(r"#.*$", "", url)

    if url.find("://") == -1:

        partes_base = url_base.split("/")
        partes_url = url.split("/")
        partes_base.pop()

        while partes_url:
            if partes_url[0] == "." or partes_url[0] == "":
                partes_url.pop(0)
            elif partes_url[0] == "..":
                partes_base.pop()
                partes_url.pop(0)
            else:
                break

        url = "/".join(partes_base + partes_url)

    return url


def eh_url_valida(url, url_inicial):

    if not re.match(r"^https?://[^#@\s]+(.html?|/)$", url):
        return False

    url_inicial = re.sub(r"/[^/]*$", "/", url_inicial)
    if not url.startswith(url_inicial):
        return False

    return True


def obter_nome_cache(url):
    assert url.startswith("http://") or url.startswith("https://"), url
    assert url.endswith(".html") or url.endswith(".htm") or url.endswith("/"), url

    if url[-1] == "/":
        url = url + "index.html"

    i = url.find("://") + 3
    partes = ["cache"] + url[i:].split("/")
    nome_cache = os.path.join(*partes)
    diretorio = os.path.join(*partes[:-1])
    if not os.path.isdir(diretorio):
        os.makedirs(diretorio)

    return nome_cache


def obter_html(url):

    nome_cache = obter_nome_cache(url)

    if os.path.isfile(nome_cache):
        with open(nome_cache, encoding="UTF-8") as arquivo:
            html = arquivo.read()
    else:
        if not REQUESTS_FOUND:
            print("O módulo requests é necessário para baixar outras páginas:", file=sys.stderr)
            print("tente digitar:  pip3 install --user requests", file=sys.stderr)
            sys.exit(1)
        response = requests.get(url, allow_redirects=True)
        if response.status_code != 200:
            return None
        try:
            html = response.content.decode("UTF-8")
        except UnicodeDecodeError:
            html = response.content.decode("ISO-8859-1")
        if "text/html" not in response.headers["Content-Type"]:
            return None
        with open(nome_cache, "w", encoding="UTF-8") as arquivo:
            arquivo.write(html)

    return html
