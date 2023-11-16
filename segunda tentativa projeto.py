#modulos
import re
#universal
linhas = input()
texto = str(input())
#funcoes
def reconhecer_artista()
artistas = re.findall(r'"(,.;!?)"')

	
def tem_coupon():
	coupons = ["MAISAPC", "NAODUVIDO", "RPM"]
	for coupons in texto:
		if not coupons in texto:
			return("")
		return(f"|Utilize o cupom {coupons[]}|")

def preco():
	preço = ["250.00", "0.00", "123.45", "100.00", 
	"5000.50", "500", "42.00"]
	for preço in texto:
		return(f"Ingressos: R$ {preço[]}")

def data():
	data = [["26/fev", "27/fev", "28/fev"], ["31/10", "01/11"], 
	["27/06", "28/06", "04/07", "11/07"], ["11/11"], ["13/jan"]]
	for data in texto:
		if not data in texto:
			return("")
		return(f"data[]")

def site():
	site = ["palhas.do.coqueiro.br", "www.queen.mus",
	 "www.quarando.br", "www.autoramasrock.com.br",
	 "right.words.to.say", "www.rpm.mus", "www.grandfunk.mus"]
    for site in texto:
    	return(f"{site[]}")
def localidade_atracao():
	atração = ["Retorno da Jurema", "Mustapha Mustapha Mustapha Ibrahim",
	 "Tu Vens", "Bom Veneno", "The Promisse", "Alvorada Voraz", "I'm your Captain"]
	cidade = ["JamPessoa", "Brasília", "Chapecó", "Ceilândia", "Londrina"] 
    estado = ["-PB", "-DF", "-SC", "-PR"]
    local = ["Bersange's", "Mané Garrincha", "Bruma Leve", "Little Quail",
    "Colosseum", "Esplanada dos Ministérios", "El Grand Teatrón de la Frontera"]
    for atração, cidade, estado, local in texto:
    	return(f"{atração[]}")
    	return(f"{cidade[]}{estado[]}")
    	return(f"{local[]}")
#inicio do programa



