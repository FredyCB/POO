from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen


SERVICIO = "https://www.bancatlan.hn/"

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen(SERVICIO, context=ctx).read()
sopa = BeautifulSoup(html, "html.parser")
p_dolar = sopa.find("p", {"id": "moneda_dolar"})
lista = p_dolar.text.split(" | ")
print(lista[0])
print(lista[1])
