#bibliotecas
import re
#universal
linhas = int(input())
ligni = []
for linha in range(0, linhas):
    ligni.append(str(input())) 
#funcoes
def reconhecer_artista(lista):
    artistas = re.findall(r'"(.*?)"', str(lista))
    return(artistas[0].replace("\\", ""))
	
def find_discount_code(text):
    discount_code_regex = r'\b[A-Z]{3,}\b'
    discount_code = re.search(discount_code_regex, str(text))
    if discount_code:
        return f"Utilize o cupom {discount_code.group()}"
    else:
        return None

def find_ticket_price(text):
    ticket_price_regex = r'R\$ (\d+(?:[.,]\d+)?)|\b(\d+(?:[.,]\d+)?) reais\b'
    match = re.search(ticket_price_regex, str(text))
    if match:
        ticket_price = match.group(1) or match.group(2)
        ticket_price = ticket_price.replace(",", ".")
        ticket_price = float(ticket_price)
        return f'Ingressos: R$ {ticket_price:.2f}'
    else:
        return None


def find_url(text):
    url_regex = r'[a-z]{2,}(\.[a-z]{2,}){2,3}'
    url = re.search(url_regex, str(text))
    
    return url.group() if url else None

def find_dates(text):
    date_regex = r'\d{2}/(?:\d{2}|[a-zA-Z]{3})'
    dates = re.findall(date_regex, str(text))
    return dates if dates else None

def reconhecer_tourner(texto):
	regex2 = r'\b(turnê|espetáculo|show)\s(.*?)[.,;!?]'
	tour = re.findall(regex2, str(texto))[0][1]
	return(tour.replace("\\", ""))


def find_city_and_state(text):
    city_state_regex = r'\b([A-Za-záéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ]+),\s?([A-Z]{2})\b'
    match = re.search(city_state_regex, str(text))
    return match.group().replace(", ", "-").replace(",", "-") if match else None

def reconhecer_local(lista):
    local = re.findall(r'"(.*?)"', str(lista))
    return(local[1].replace("\\", ""))

def find_biggest_string(lista : list):
    if lista == []:
        return None
    else:
        maior = len(lista[0])
        for i in lista[0:]:
            if i != None:
                tamanho_atual = len(i)
                if tamanho_atual > maior:
                    maior = tamanho_atual
        return maior

def hashtag(a):
    print('#' * a)

def centralizar(texto, tamanho):
    no_de_espaços_antes = (tamanho - 2 - len(texto)) // (2)
    no_de_espaços_depois = ((tamanho - 2 - len(texto)) // (2)) + ((tamanho - 2 - len(texto)) % 2)
    print(f"#{' ' * no_de_espaços_antes}{texto}{' ' * no_de_espaços_depois}#")

def centralizar2(texto, tamanho):
    no_de_espaços_antes = (tamanho - 2 - len(texto)) // (2)
    no_de_espaços_depois = ((tamanho - 2 - len(texto)) // (2)) + ((tamanho - 2 - len(texto)) % 2)
    print(f"|{' ' * no_de_espaços_antes}{texto}{' ' * no_de_espaços_depois}|")

def ultima_linha(tamanho):
    traço = tamanho - 2
    print(f"+{'-' * traço}+")
#inicio do programa part1

artista = reconhecer_artista(ligni)
tourner = reconhecer_tourner(ligni)
cidade_e_estado = find_city_and_state(ligni)
local_de_ocorrencia = reconhecer_local(ligni)
datas = find_dates(ligni)
url = find_url(ligni)
preço = find_ticket_price(ligni)
coupon = find_discount_code(ligni)
lista_desejada = [artista,tourner,cidade_e_estado,
local_de_ocorrencia,datas,url,preço,coupon]
tamanho_da_linha = find_biggest_string(lista_desejada) + 4
hashtag(tamanho_da_linha)
centralizar(artista.upper(), tamanho_da_linha)
hashtag(tamanho_da_linha)
centralizar(tourner, tamanho_da_linha)
centralizar(cidade_e_estado, tamanho_da_linha)
centralizar(local_de_ocorrencia, tamanho_da_linha)
if datas != None:
    for data in datas:
        centralizar(data, tamanho_da_linha)
hashtag(tamanho_da_linha)
centralizar(url, tamanho_da_linha)
hashtag(tamanho_da_linha)
centralizar2(preço, tamanho_da_linha)
if coupon != None:
    centralizar2(coupon, tamanho_da_linha)
ultima_linha(tamanho_da_linha)





