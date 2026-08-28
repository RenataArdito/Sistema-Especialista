# ============================================================
# VERSOES CORRETAS DE REFERENCIA (nao entram no dataset de treino)
# ============================================================

def calcular_media_correto(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def ordenar_lista_correto(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def busca_linear_correto(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def fatorial_correto(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def reverter_string_correto(s):
    reversa = ''
    for char in s:
        reversa = char + reversa
    return reversa


def media_ponderada_correto(valores, pesos):
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def bubble_sort_correto(lista):
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def busca_binaria_correto(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def fibonacci_correto(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def contar_vogais_correto(s):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


# ============================================================
# CATEGORIA 1: INICIALIZACAO
# Ocorre quando se tenta acessar uma variavel que nao foi
# inicializada (Tabela 2 do artigo).
# ============================================================

# --- calcular_media ---

def calcular_media_inicializacao_v1(numeros):
    # DEFEITO (inicializacao): omite "soma = 0" antes do laco
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_inicializacao_v2(numeros):
    # DEFEITO (inicializacao): inicializa com tipo incompativel (None)
    soma = None
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_inicializacao_v3(numeros):
    # DEFEITO (inicializacao): inicializa com tipo incompativel (string)
    soma = ''
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_inicializacao_v4(numeros):
    # DEFEITO (inicializacao): reinicializa o acumulador a cada iteracao
    for num in numeros:
        soma = 0
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_inicializacao_v5(numeros):
    # DEFEITO (inicializacao): inicializa variavel com nome diferente da usada no laco
    total = 0
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_inicializacao_v6(numeros):
    # DEFEITO (inicializacao): inicializa o acumulador depois de usa-lo
    for num in numeros:
        soma += num
    soma = 0
    return soma / len(numeros) if numeros else 0


# --- ordenar_lista ---

def ordenar_lista_inicializacao_v1(lista):
    # DEFEITO (inicializacao): omite "auxiliar = []" antes do laco
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar.append(lista[i])
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_inicializacao_v2(lista):
    # DEFEITO (inicializacao): contador de trocas inicializado com None
    trocas = None
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    return lista


def ordenar_lista_inicializacao_v3(lista):
    # DEFEITO (inicializacao): contador de trocas inicializado como string
    trocas = ''
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    return lista


def ordenar_lista_inicializacao_v4(lista):
    # DEFEITO (inicializacao): contador de trocas reinicializado a cada iteracao externa
    for i in range(len(lista)):
        trocas = 0
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    return lista


def ordenar_lista_inicializacao_v5(lista):
    # DEFEITO (inicializacao): inicializa nome errado (n_trocas em vez de trocas)
    n_trocas = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    return lista


def ordenar_lista_inicializacao_v6(lista):
    # DEFEITO (inicializacao): contador inicializado apos o laco que o usa
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    trocas = 0
    return lista


# --- busca_linear ---

def busca_linear_inicializacao_v1(lista, alvo):
    # DEFEITO (inicializacao): omite "i = 0" antes do laco while
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1


def busca_linear_inicializacao_v2(lista, alvo):
    # DEFEITO (inicializacao): indice inicializado com None
    i = None
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1


def busca_linear_inicializacao_v3(lista, alvo):
    # DEFEITO (inicializacao): contador de comparacoes inicializado como string
    comparacoes = ''
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_inicializacao_v4(lista, alvo):
    # DEFEITO (inicializacao): posicao encontrada reinicializada a cada iteracao
    for i in range(len(lista)):
        posicao_encontrada = None
        if lista[i] == alvo:
            posicao_encontrada = i
    return posicao_encontrada if posicao_encontrada is not None else -1


def busca_linear_inicializacao_v5(lista, alvo):
    # DEFEITO (inicializacao): inicializa variavel com nome diferente da usada no laco
    indice = 0
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1


def busca_linear_inicializacao_v6(lista, alvo):
    # DEFEITO (inicializacao): indice inicializado apos o laco que o usa
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    i = 0
    return -1


# --- fatorial ---

def fatorial_inicializacao_v1(n):
    # DEFEITO (inicializacao): omite "resultado = 1" antes do laco
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_inicializacao_v2(n):
    # DEFEITO (inicializacao): inicializa resultado com None
    resultado = None
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_inicializacao_v3(n):
    # DEFEITO (inicializacao): inicializa resultado como string
    resultado = ''
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_inicializacao_v4(n):
    # DEFEITO (inicializacao): resultado reinicializado a cada iteracao
    for i in range(1, n + 1):
        resultado = 1
        resultado *= i
    return resultado


def fatorial_inicializacao_v5(n):
    # DEFEITO (inicializacao): inicializa variavel com nome diferente da usada no laco
    valor = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_inicializacao_v6(n):
    # DEFEITO (inicializacao): resultado inicializado depois do laco que o usa
    for i in range(1, n + 1):
        resultado *= i
    resultado = 1
    return resultado


# --- reverter_string ---

def reverter_string_inicializacao_v1(s):
    # DEFEITO (inicializacao): omite "reversa = ''" antes do laco
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_inicializacao_v2(s):
    # DEFEITO (inicializacao): inicializa reversa com None
    reversa = None
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_inicializacao_v3(s):
    # DEFEITO (inicializacao): inicializa reversa como lista em vez de string
    reversa = []
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_inicializacao_v4(s):
    # DEFEITO (inicializacao): reversa reinicializada a cada iteracao
    for char in s:
        reversa = ''
        reversa = char + reversa
    return reversa


def reverter_string_inicializacao_v5(s):
    # DEFEITO (inicializacao): inicializa variavel com nome diferente da usada no laco
    resultado = ''
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_inicializacao_v6(s):
    # DEFEITO (inicializacao): reversa inicializada depois do laco que a usa
    for char in s:
        reversa = char + reversa
    reversa = ''
    return reversa


# --- media_ponderada ---

def media_ponderada_inicializacao_v1(valores, pesos):
    # DEFEITO (inicializacao): omite inicializacao de soma_valores e soma_pesos
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_inicializacao_v2(valores, pesos):
    # DEFEITO (inicializacao): soma_valores inicializada com None
    soma_valores = None
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_inicializacao_v3(valores, pesos):
    # DEFEITO (inicializacao): soma_pesos inicializada como string
    soma_valores = 0
    soma_pesos = ''
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_inicializacao_v4(valores, pesos):
    # DEFEITO (inicializacao): acumuladores reinicializados a cada iteracao
    for v, p in zip(valores, pesos):
        soma_valores = 0
        soma_pesos = 0
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_inicializacao_v5(valores, pesos):
    # DEFEITO (inicializacao): inicializa nome errado (soma_v em vez de soma_valores)
    soma_v = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_inicializacao_v6(valores, pesos):
    # DEFEITO (inicializacao): soma_pesos inicializada apos o laco que a usa
    soma_valores = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    soma_pesos = 0
    return soma_valores / soma_pesos if soma_pesos else 0


# --- bubble_sort ---

def bubble_sort_inicializacao_v1(lista):
    # DEFEITO (inicializacao): omite "trocado = False" antes do laco interno
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_inicializacao_v2(lista):
    # DEFEITO (inicializacao): "trocado" inicializado com None
    n = len(lista)
    for i in range(n):
        trocado = None
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if not trocado:
            break
    return lista


def bubble_sort_inicializacao_v3(lista):
    # DEFEITO (inicializacao): "n" inicializado como string em vez de len(lista)
    n = str(len(lista))
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_inicializacao_v4(lista):
    # DEFEITO (inicializacao): "trocado" e reinicializado a cada comparacao interna
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            trocado = False
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_inicializacao_v5(lista):
    # DEFEITO (inicializacao): inicializa nome errado (houve_troca em vez de trocado)
    n = len(lista)
    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_inicializacao_v6(lista):
    # DEFEITO (inicializacao): "trocado" inicializado apos o laco que o usa
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        trocado = False
        if not trocado:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_inicializacao_v1(lista, alvo):
    # DEFEITO (inicializacao): omite "esquerda = 0" e "direita = len(lista) - 1"
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_inicializacao_v2(lista, alvo):
    # DEFEITO (inicializacao): "esquerda" inicializada com None
    esquerda = None
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_inicializacao_v3(lista, alvo):
    # DEFEITO (inicializacao): "direita" inicializada como string
    esquerda = 0
    direita = str(len(lista) - 1)
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_inicializacao_v4(lista, alvo):
    # DEFEITO (inicializacao): "direita" reinicializada a cada iteracao do laco
    esquerda = 0
    while esquerda <= direita:
        direita = len(lista) - 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_inicializacao_v5(lista, alvo):
    # DEFEITO (inicializacao): inicializa nome errado (ultimo em vez de direita)
    esquerda = 0
    ultimo = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_inicializacao_v6(lista, alvo):
    # DEFEITO (inicializacao): "esquerda" inicializada apos o laco que a usa
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    esquerda = 0
    return -1


# --- fibonacci ---

def fibonacci_inicializacao_v1(n):
    # DEFEITO (inicializacao): omite "a, b = 0, 1" antes do laco
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_inicializacao_v2(n):
    # DEFEITO (inicializacao): "a" e "b" inicializados com None
    a, b = None, None
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_inicializacao_v3(n):
    # DEFEITO (inicializacao): "a" e "b" inicializados como strings
    a, b = '', ''
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_inicializacao_v4(n):
    # DEFEITO (inicializacao): "a" e "b" reinicializados a cada iteracao
    for _ in range(n):
        a, b = 0, 1
        a, b = b, a + b
    return a


def fibonacci_inicializacao_v5(n):
    # DEFEITO (inicializacao): inicializa nomes errados (x, y em vez de a, b)
    x, y = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_inicializacao_v6(n):
    # DEFEITO (inicializacao): "a" e "b" inicializados apos o laco que os usa
    for _ in range(n):
        a, b = b, a + b
    a, b = 0, 1
    return a


# --- contar_vogais ---

def contar_vogais_inicializacao_v1(s):
    # DEFEITO (inicializacao): omite "contador = 0" antes do laco
    vogais = 'aeiouAEIOU'
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_inicializacao_v2(s):
    # DEFEITO (inicializacao): contador inicializado com None
    vogais = 'aeiouAEIOU'
    contador = None
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_inicializacao_v3(s):
    # DEFEITO (inicializacao): contador inicializado como string
    vogais = 'aeiouAEIOU'
    contador = ''
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_inicializacao_v4(s):
    # DEFEITO (inicializacao): contador reinicializado a cada iteracao
    vogais = 'aeiouAEIOU'
    for char in s:
        contador = 0
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_inicializacao_v5(s):
    # DEFEITO (inicializacao): inicializa nome errado (total em vez de contador)
    vogais = 'aeiouAEIOU'
    total = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_inicializacao_v6(s):
    # DEFEITO (inicializacao): contador inicializado apos o laco que o usa
    vogais = 'aeiouAEIOU'
    for char in s:
        if char in vogais:
            contador += 1
    contador = 0
    return contador


# ============================================================
# CATEGORIA 2: COMPUTACAO
# Similar a comissao; ocorre quando um valor e definido
# erroneamente para uma variavel (Tabela 2 do artigo).
# Inicializacao e estrutura de controle permanecem corretas;
# apenas o OPERADOR que produz o valor esta trocado.
# ============================================================

# --- calcular_media ---

def calcular_media_computacao_v1(numeros):
    # DEFEITO (computacao): "+=" trocado por "-=" na acumulacao
    soma = 0
    for num in numeros:
        soma -= num
    return soma / len(numeros) if numeros else 0


def calcular_media_computacao_v2(numeros):
    # DEFEITO (computacao): divisao real trocada por divisao inteira
    soma = 0
    for num in numeros:
        soma += num
    return soma // len(numeros) if numeros else 0


def calcular_media_computacao_v3(numeros):
    # DEFEITO (computacao): valor acumulado multiplicado indevidamente
    soma = 0
    for num in numeros:
        soma += num * 2
    return soma / len(numeros) if numeros else 0


def calcular_media_computacao_v4(numeros):
    # DEFEITO (computacao): denominador calculado com termo extra
    soma = 0
    for num in numeros:
        soma += num
    return soma / (len(numeros) + 1) if numeros else 0


def calcular_media_computacao_v5(numeros):
    # DEFEITO (computacao): acumulador sobrescrito em vez de somado
    soma = 0
    for num in numeros:
        soma = num
    return soma / len(numeros) if numeros else 0


def calcular_media_computacao_v6(numeros):
    # DEFEITO (computacao): acumula o quadrado do valor em vez do valor
    soma = 0
    for num in numeros:
        soma += num ** 2
    return soma / len(numeros) if numeros else 0


# --- ordenar_lista ---

def ordenar_lista_computacao_v1(lista):
    # DEFEITO (computacao): comparador invertido (> trocado por <)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_computacao_v2(lista):
    # DEFEITO (computacao): comparador trocado por "!="
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] != lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_computacao_v3(lista):
    # DEFEITO (computacao): troca parcial, so atualiza uma posicao
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i] = lista[j]
    return lista


def ordenar_lista_computacao_v4(lista):
    # DEFEITO (computacao): comparador trocado por ">="
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_computacao_v5(lista):
    # DEFEITO (computacao): compara com elemento adjacente errado (j-1 em vez de j)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j - 1]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_computacao_v6(lista):
    # DEFEITO (computacao): indices da troca calculados errados (troca com i+1 em vez de j)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


# --- busca_linear ---

def busca_linear_computacao_v1(lista, alvo):
    # DEFEITO (computacao): "==" trocado por "!=" na comparacao
    for i in range(len(lista)):
        if lista[i] != alvo:
            continue
        return i
    return -1


def busca_linear_computacao_v2(lista, alvo):
    # DEFEITO (computacao): compara com o indice em vez do valor
    for i in range(len(lista)):
        if i == alvo:
            return i
    return -1


def busca_linear_computacao_v3(lista, alvo):
    # DEFEITO (computacao): retorna o valor em vez do indice
    for i in range(len(lista)):
        if lista[i] == alvo:
            return lista[i]
    return -1


def busca_linear_computacao_v4(lista, alvo):
    # DEFEITO (computacao): comparacao usa "in" sobre a lista inteira, nao o elemento
    for i in range(len(lista)):
        if alvo in lista:
            return i
    return -1


def busca_linear_computacao_v5(lista, alvo):
    # DEFEITO (computacao): comparacao trocada por "maior que"
    for i in range(len(lista)):
        if lista[i] > alvo:
            return i
    return -1


def busca_linear_computacao_v6(lista, alvo):
    # DEFEITO (computacao): retorna i - 1 em vez de i (deslocamento no valor calculado)
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i - 1
    return -1


# --- fatorial ---

def fatorial_computacao_v1(n):
    # DEFEITO (computacao): "*=" trocado por "+="
    resultado = 1
    for i in range(1, n + 1):
        resultado += i
    return resultado


def fatorial_computacao_v2(n):
    # DEFEITO (computacao): multiplica por i * 2 em vez de i
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i * 2
    return resultado


def fatorial_computacao_v3(n):
    # DEFEITO (computacao): resultado sobrescrito em vez de multiplicado
    resultado = 1
    for i in range(1, n + 1):
        resultado = i
    return resultado


def fatorial_computacao_v4(n):
    # DEFEITO (computacao): "*=" trocado por "**="
    resultado = 1
    for i in range(1, n + 1):
        resultado **= i
    return resultado


def fatorial_computacao_v5(n):
    # DEFEITO (computacao): multiplica por (i - 1) em vez de i
    resultado = 1
    for i in range(1, n + 1):
        resultado *= (i - 1)
    return resultado


def fatorial_computacao_v6(n):
    # DEFEITO (computacao): "*=" trocado por "//="
    resultado = 1
    for i in range(1, n + 1):
        resultado //= i
    return resultado


# --- reverter_string ---

def reverter_string_computacao_v1(s):
    # DEFEITO (computacao): concatenacao na ordem errada (nao inverte)
    reversa = ''
    for char in s:
        reversa += char
    return reversa


def reverter_string_computacao_v2(s):
    # DEFEITO (computacao): reversa sobrescrita em vez de concatenada
    reversa = ''
    for char in s:
        reversa = char
    return reversa


def reverter_string_computacao_v3(s):
    # DEFEITO (computacao): concatena o caractere em maiusculo indevidamente
    reversa = ''
    for char in s:
        reversa = char.upper() + reversa
    return reversa


def reverter_string_computacao_v4(s):
    # DEFEITO (computacao): concatena caractere duas vezes
    reversa = ''
    for char in s:
        reversa = char + char + reversa
    return reversa


def reverter_string_computacao_v5(s):
    # DEFEITO (computacao): usa espaco como separador na concatenacao
    reversa = ''
    for char in s:
        reversa = char + ' ' + reversa
    return reversa


def reverter_string_computacao_v6(s):
    # DEFEITO (computacao): concatenacao alterna a ordem de forma incorreta
    reversa = ''
    for char in s:
        reversa = reversa + char
    return reversa


# --- media_ponderada ---

def media_ponderada_computacao_v1(valores, pesos):
    # DEFEITO (computacao): "*" trocado por "+" no produto valor-peso
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v + p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_computacao_v2(valores, pesos):
    # DEFEITO (computacao): soma_pesos acumula o valor em vez do peso
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += v
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_computacao_v3(valores, pesos):
    # DEFEITO (computacao): divisao real trocada por divisao inteira
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores // soma_pesos if soma_pesos else 0


def media_ponderada_computacao_v4(valores, pesos):
    # DEFEITO (computacao): peso elevado ao quadrado no produto
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * (p ** 2)
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_computacao_v5(valores, pesos):
    # DEFEITO (computacao): soma_valores sobrescrita em vez de acumulada
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores = v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_computacao_v6(valores, pesos):
    # DEFEITO (computacao): denominador soma "soma_valores" em vez de "soma_pesos"
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_valores if soma_valores else 0


# --- bubble_sort ---

def bubble_sort_computacao_v1(lista):
    # DEFEITO (computacao): comparador invertido (> trocado por <)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_computacao_v2(lista):
    # DEFEITO (computacao): compara com "j+2" em vez de "j+1"
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 2 - 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_computacao_v3(lista):
    # DEFEITO (computacao): comparador trocado por ">="
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] >= lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_computacao_v4(lista):
    # DEFEITO (computacao): troca so copia um valor, nao efetua swap completo
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j] = lista[j + 1]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_computacao_v5(lista):
    # DEFEITO (computacao): limite do laco interno calculado com operador errado
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i + 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_computacao_v6(lista):
    # DEFEITO (computacao): comparacao usa lista[j] duas vezes em vez de lista[j+1]
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_computacao_v1(lista, alvo):
    # DEFEITO (computacao): calculo do meio sem parenteses (precedencia errada)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = esquerda + direita // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_computacao_v2(lista, alvo):
    # DEFEITO (computacao): atualizacoes de esquerda/direita trocadas entre si
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            direita = meio + 1
        else:
            esquerda = meio - 1
    return -1


def busca_binaria_computacao_v3(lista, alvo):
    # DEFEITO (computacao): comparacao de direcao invertida (< trocado por >)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_computacao_v4(lista, alvo):
    # DEFEITO (computacao): retorna "esquerda" em vez de "meio" ao encontrar
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return esquerda
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_computacao_v5(lista, alvo):
    # DEFEITO (computacao): atualizacao de "esquerda" nao soma 1 ao meio
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio
        else:
            direita = meio - 1
    return -1


def busca_binaria_computacao_v6(lista, alvo):
    # DEFEITO (computacao): calculo do meio usa media aritmetica com peso errado
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita * 2) // 3
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# --- fibonacci ---

def fibonacci_computacao_v1(n):
    # DEFEITO (computacao): soma trocada por multiplicacao
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a * b
    return a


def fibonacci_computacao_v2(n):
    # DEFEITO (computacao): "a" e "b" nao sao trocados, so "b" e atualizado
    a, b = 0, 1
    for _ in range(n):
        b = a + b
    return a


def fibonacci_computacao_v3(n):
    # DEFEITO (computacao): soma usa apenas "b" duas vezes
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + b
    return a


def fibonacci_computacao_v4(n):
    # DEFEITO (computacao): subtracao no lugar da soma
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a - b
    return a


def fibonacci_computacao_v5(n):
    # DEFEITO (computacao): retorna "b" em vez de "a"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def fibonacci_computacao_v6(n):
    # DEFEITO (computacao): termo seguinte soma o dobro de "a"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a * 2) + b
    return a


# --- contar_vogais ---

def contar_vogais_computacao_v1(s):
    # DEFEITO (computacao): "+=" trocado por "-="
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador -= 1
    return contador


def contar_vogais_computacao_v2(s):
    # DEFEITO (computacao): incrementa em 2 em vez de 1
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 2
    return contador


def contar_vogais_computacao_v3(s):
    # DEFEITO (computacao): contador sobrescrito em vez de incrementado
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador = 1
    return contador


def contar_vogais_computacao_v4(s):
    # DEFEITO (computacao): compara com string vazia de vogais (comparacao sempre falsa via fatia errada)
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais[1:]:
            contador += 1
    return contador


def contar_vogais_computacao_v5(s):
    # DEFEITO (computacao): condicao usa "not in" em vez de "in"
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char not in vogais:
            contador += 1
    return contador


def contar_vogais_computacao_v6(s):
    # DEFEITO (computacao): incrementa contador para toda letra, nao so vogal (usa .isalpha)
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char.isalpha():
            contador += 1
    return contador


# ============================================================
# CATEGORIA 3: DESEMPENHO
# Algumas rotinas executam comandos ou lacos (loops)
# desnecessarios (Tabela 2 do artigo). O resultado final
# costuma permanecer correto; o defeito esta no CUSTO
# computacional desnecessario introduzido.
# ============================================================

# --- calcular_media ---

def calcular_media_desempenho_v1(numeros):
    # DEFEITO (desempenho): recalcula a soma parcial a cada iteracao (O(n^2))
    soma = 0
    for num in numeros:
        soma = sum(numeros[:numeros.index(num) + 1])
    return soma / len(numeros) if numeros else 0


def calcular_media_desempenho_v2(numeros):
    # DEFEITO (desempenho): laco aninhado desnecessario
    soma = 0
    for num in numeros:
        for _ in numeros:
            pass
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_desempenho_v3(numeros):
    # DEFEITO (desempenho): recalcula sum(numeros) inteiro a cada iteracao
    soma = 0
    for num in numeros:
        soma = sum(numeros)
    return soma / len(numeros) if numeros else 0


def calcular_media_desempenho_v4(numeros):
    # DEFEITO (desempenho): verifica pertencimento na lista inteira a cada iteracao
    soma = 0
    for num in numeros:
        if num in numeros:
            soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_desempenho_v5(numeros):
    # DEFEITO (desempenho): cria copia da lista a cada iteracao sem necessidade
    soma = 0
    for num in numeros:
        copia = list(numeros)
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_desempenho_v6(numeros):
    # DEFEITO (desempenho): ordena a lista a cada iteracao antes de somar
    soma = 0
    for num in numeros:
        numeros_ordenados = sorted(numeros)
        soma += num
    return soma / len(numeros) if numeros else 0


# --- ordenar_lista ---

def ordenar_lista_desempenho_v1(lista):
    # DEFEITO (desempenho): laco interno percorre a lista inteira, nao apenas i+1 em diante
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_desempenho_v2(lista):
    # DEFEITO (desempenho): recalcula len(lista) a cada iteracao do laco interno
    for i in range(len(lista)):
        for j in range(i + 1, len(list(lista))):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_desempenho_v3(lista):
    # DEFEITO (desempenho): verifica se a lista ja esta ordenada a cada passo (sorted() e caro)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if sorted(lista) == lista:
                pass
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_desempenho_v4(lista):
    # DEFEITO (desempenho): copia a lista inteira a cada iteracao externa
    for i in range(len(lista)):
        copia = lista[:]
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_desempenho_v5(lista):
    # DEFEITO (desempenho): laco extra que apenas conta elementos, sem uso do resultado
    for i in range(len(lista)):
        contagem = 0
        for k in range(len(lista)):
            contagem += 1
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_desempenho_v6(lista):
    # DEFEITO (desempenho): reordena a sublista com sorted() a cada passo, alem da troca manual
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            lista[i:] = sorted(lista[i:], reverse=True) if False else lista[i:]
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


# --- busca_linear ---

def busca_linear_desempenho_v1(lista, alvo):
    # DEFEITO (desempenho): laco aninhado desnecessario para cada posicao avaliada
    for i in range(len(lista)):
        for _ in range(len(lista)):
            if lista[i] == alvo:
                return i
    return -1


def busca_linear_desempenho_v2(lista, alvo):
    # DEFEITO (desempenho): nao interrompe a busca ao encontrar; continua percorrendo
    posicao = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            posicao = i
    return posicao


def busca_linear_desempenho_v3(lista, alvo):
    # DEFEITO (desempenho): verifica pertencimento na lista inteira antes de cada comparacao
    for i in range(len(lista)):
        if alvo in lista and lista[i] == alvo:
            return i
    return -1


def busca_linear_desempenho_v4(lista, alvo):
    # DEFEITO (desempenho): recria a lista via list() a cada iteracao
    for i in range(len(lista)):
        lista_temp = list(lista)
        if lista_temp[i] == alvo:
            return i
    return -1


def busca_linear_desempenho_v5(lista, alvo):
    # DEFEITO (desempenho): ordena a lista a cada iteracao (alem de alterar a saida esperada)
    for i in range(len(lista)):
        sorted(lista)
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_desempenho_v6(lista, alvo):
    # DEFEITO (desempenho): usa recursao profunda em vez do laco iterativo simples
    def busca_rec(indice):
        if indice >= len(lista):
            return -1
        if lista[indice] == alvo:
            return indice
        return busca_rec(indice + 1)
    return busca_rec(0)


# --- fatorial ---

def fatorial_desempenho_v1(n):
    # DEFEITO (desempenho): recursao sem memoizacao (custo extra de pilha de chamadas)
    def auxiliar(valor):
        if valor <= 1:
            return 1
        return valor * auxiliar(valor - 1)
    return auxiliar(n)


def fatorial_desempenho_v2(n):
    # DEFEITO (desempenho): recalcula o fatorial parcial do zero a cada iteracao
    resultado = 1
    for i in range(1, n + 1):
        resultado = 1
        for k in range(1, i + 1):
            resultado *= k
    return resultado


def fatorial_desempenho_v3(n):
    # DEFEITO (desempenho): laco aninhado desnecessario dentro do calculo
    resultado = 1
    for i in range(1, n + 1):
        for _ in range(1):
            for _ in range(1):
                resultado *= i
    return resultado


def fatorial_desempenho_v4(n):
    # DEFEITO (desempenho): cria lista de todos os numeros antes de multiplicar
    numeros = [i for i in range(1, n + 1)]
    resultado = 1
    for i in numeros:
        resultado *= i
    return resultado


def fatorial_desempenho_v5(n):
    # DEFEITO (desempenho): usa reduce reimplementado manualmente com chamada redundante
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        _ = str(resultado)  # conversao desnecessaria a cada iteracao
    return resultado


def fatorial_desempenho_v6(n):
    # DEFEITO (desempenho): reconstroi o intervalo de calculo do zero a cada passo
    resultado = 1
    for i in range(1, n + 1):
        intervalo = list(range(1, i + 1))
        resultado = 1
        for k in intervalo:
            resultado *= k
    return resultado


# --- reverter_string ---

def reverter_string_desempenho_v1(s):
    # DEFEITO (desempenho): acessa por indice calculado a cada iteracao em vez de iterar direto
    reversa = ''
    for i in range(len(s)):
        reversa += s[len(s) - 1 - i]
    return reversa


def reverter_string_desempenho_v2(s):
    # DEFEITO (desempenho): reconstroi a string inteira a cada iteracao usando slicing
    reversa = ''
    for i in range(len(s)):
        reversa = s[:i + 1][::-1]
    return reversa


def reverter_string_desempenho_v3(s):
    # DEFEITO (desempenho): laco aninhado desnecessario percorrendo a string a cada passo
    reversa = ''
    for char in s:
        for _ in s:
            pass
        reversa = char + reversa
    return reversa


def reverter_string_desempenho_v4(s):
    # DEFEITO (desempenho): recursao sem necessidade em vez do laco simples
    def auxiliar(texto):
        if len(texto) == 0:
            return ''
        return auxiliar(texto[1:]) + texto[0]
    return auxiliar(s)


def reverter_string_desempenho_v5(s):
    # DEFEITO (desempenho): converte para lista e concatena novamente a cada iteracao
    reversa = ''
    for char in s:
        lista_temp = list(s)
        reversa = char + reversa
    return reversa


def reverter_string_desempenho_v6(s):
    # DEFEITO (desempenho): verifica se caractere pertence a string original a cada iteracao
    reversa = ''
    for char in s:
        if char in s:
            reversa = char + reversa
    return reversa


# --- media_ponderada ---

def media_ponderada_desempenho_v1(valores, pesos):
    # DEFEITO (desempenho): laco aninhado desnecessario (produto calculado para todos os pares)
    soma_valores = 0
    for v in valores:
        for p in pesos:
            soma_valores += v * p
    soma_pesos = sum(pesos)
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_desempenho_v2(valores, pesos):
    # DEFEITO (desempenho): recalcula sum(pesos) a cada iteracao do laco principal
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos = sum(pesos)
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_desempenho_v3(valores, pesos):
    # DEFEITO (desempenho): reconstroi as listas via list() a cada iteracao
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        v_temp, p_temp = list(valores), list(pesos)
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_desempenho_v4(valores, pesos):
    # DEFEITO (desempenho): verifica pertencimento nas listas inteiras a cada iteracao
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        if v in valores and p in pesos:
            soma_valores += v * p
            soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_desempenho_v5(valores, pesos):
    # DEFEITO (desempenho): ordena as listas a cada iteracao sem necessidade
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        sorted(valores)
        sorted(pesos)
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_desempenho_v6(valores, pesos):
    # DEFEITO (desempenho): usa indices manuais com len() recalculado a cada iteracao
    soma_valores = 0
    soma_pesos = 0
    for i in range(min(len(valores), len(pesos))):
        for _ in range(len(valores)):
            pass
        soma_valores += valores[i] * pesos[i]
        soma_pesos += pesos[i]
    return soma_valores / soma_pesos if soma_pesos else 0


# --- bubble_sort ---

def bubble_sort_desempenho_v1(lista):
    # DEFEITO (desempenho): remove a flag "trocado", percorrendo sempre todas as passagens
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_desempenho_v2(lista):
    # DEFEITO (desempenho): laco interno sempre percorre a lista inteira (nao usa n-i-1)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_desempenho_v3(lista):
    # DEFEITO (desempenho): verifica se a lista esta ordenada com sorted() a cada passagem
    n = len(lista)
    for i in range(n):
        trocado = False
        if lista == sorted(lista):
            pass
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_desempenho_v4(lista):
    # DEFEITO (desempenho): copia a lista inteira a cada passagem externa
    n = len(lista)
    for i in range(n):
        copia = lista[:]
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_desempenho_v5(lista):
    # DEFEITO (desempenho): recalcula "n" chamando len(lista) a cada iteracao do laco interno
    for i in range(len(lista)):
        trocado = False
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
            _ = len(lista)
        if not trocado:
            break
    return lista


def bubble_sort_desempenho_v6(lista):
    # DEFEITO (desempenho): laco aninhado extra que apenas conta comparacoes sem uso
    n = len(lista)
    for i in range(n):
        trocado = False
        comparacoes = 0
        for j in range(0, n - i - 1):
            for _ in range(n):
                comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_desempenho_v1(lista, alvo):
    # DEFEITO (desempenho): recursiva sem memoizacao no lugar da versao iterativa
    def busca(esquerda, direita):
        if esquerda > direita:
            return -1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            return busca(meio + 1, direita)
        else:
            return busca(esquerda, meio - 1)
    return busca(0, len(lista) - 1)


def busca_binaria_desempenho_v2(lista, alvo):
    # DEFEITO (desempenho): verifica "alvo in lista" (O(n)) antes de cada iteracao da busca binaria
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        if alvo in lista:
            pass
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_desempenho_v3(lista, alvo):
    # DEFEITO (desempenho): ordena a lista novamente a cada iteracao, mesmo ja ordenada
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        lista_ordenada = sorted(lista)
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_desempenho_v4(lista, alvo):
    # DEFEITO (desempenho): cria copia da lista a cada iteracao do laco
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        copia = lista[:]
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_desempenho_v5(lista, alvo):
    # DEFEITO (desempenho): laco aninhado desnecessario dentro da busca binaria
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        for _ in range(len(lista)):
            pass
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_desempenho_v6(lista, alvo):
    # DEFEITO (desempenho): recalcula len(lista) repetidamente dentro do laco
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        _ = len(lista)
        _ = len(lista)
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# --- fibonacci ---

def fibonacci_desempenho_v1(n):
    # DEFEITO (desempenho): recursao exponencial sem memoizacao no lugar da versao iterativa
    def auxiliar(valor):
        if valor <= 1:
            return valor
        return auxiliar(valor - 1) + auxiliar(valor - 2)
    return auxiliar(n)


def fibonacci_desempenho_v2(n):
    # DEFEITO (desempenho): recalcula toda a sequencia do zero a cada iteracao
    a, b = 0, 1
    for i in range(n):
        a, b = 0, 1
        for _ in range(i):
            a, b = b, a + b
    return a


def fibonacci_desempenho_v3(n):
    # DEFEITO (desempenho): constroi lista completa de termos apenas para obter o ultimo
    termos = []
    a, b = 0, 1
    for _ in range(n):
        termos.append(a)
        a, b = b, a + b
    return termos[-1] if termos else 0


def fibonacci_desempenho_v4(n):
    # DEFEITO (desempenho): laco aninhado desnecessario a cada iteracao
    a, b = 0, 1
    for _ in range(n):
        for _ in range(1):
            for _ in range(1):
                a, b = b, a + b
    return a


def fibonacci_desempenho_v5(n):
    # DEFEITO (desempenho): converte termos para string desnecessariamente a cada iteracao
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        _ = str(a)
    return a


def fibonacci_desempenho_v6(n):
    # DEFEITO (desempenho): usa soma de todos os termos anteriores em vez de acumulador direto
    termos = [0, 1]
    for i in range(2, n + 2):
        termos.append(sum(termos[i - 2:i]))
    return termos[n] if n < len(termos) else termos[-1]


# --- contar_vogais ---

def contar_vogais_desempenho_v1(s):
    # DEFEITO (desempenho): laco aninhado percorrendo a string de vogais a cada caractere
    contador = 0
    for char in s:
        for vogal in 'aeiouAEIOU':
            if char == vogal:
                contador += 1
    return contador


def contar_vogais_desempenho_v2(s):
    # DEFEITO (desempenho): recalcula a string de vogais a cada iteracao
    contador = 0
    for char in s:
        vogais = 'a' + 'e' + 'i' + 'o' + 'u' + 'A' + 'E' + 'I' + 'O' + 'U'
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_desempenho_v3(s):
    # DEFEITO (desempenho): converte a string inteira para lista a cada iteracao
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        letras = list(s)
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_desempenho_v4(s):
    # DEFEITO (desempenho): conta ocorrencias de cada vogal na string inteira a cada caractere
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            s.count(char)
            contador += 1
    return contador


def contar_vogais_desempenho_v5(s):
    # DEFEITO (desempenho): laco extra que apenas percorre a string sem uso
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        for _ in s:
            pass
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_desempenho_v6(s):
    # DEFEITO (desempenho): soma contagens individuais de cada vogal via count() (multiplas varreduras)
    contador = 0
    for vogal in 'aeiouAEIOU':
        contador += s.count(vogal)
    return contador


# ============================================================
# CATEGORIA 4: CONTROLE
# Ocorre quando um comando de desvio condicional e usado de
# forma incorreta (Tabela 2 do artigo): condicao de laco
# trocada, incremento de controle ausente, ramificacao
# if/else invertida, etc.
# ============================================================

# --- calcular_media ---

def calcular_media_controle_v1(numeros):
    # DEFEITO (controle): laco while sem incremento do indice (risco de loop infinito)
    soma = 0
    i = 0
    while i < len(numeros):
        soma += numeros[i]
    return soma / len(numeros) if numeros else 0


def calcular_media_controle_v2(numeros):
    # DEFEITO (controle): condicao do laco while invertida
    soma = 0
    i = 0
    while i > len(numeros):
        soma += numeros[i]
        i += 1
    return soma / len(numeros) if numeros else 0


def calcular_media_controle_v3(numeros):
    # DEFEITO (controle): usa "or" no lugar de condicao simples, alterando o desvio
    soma = 0
    for num in numeros:
        if num > 0 or num < 0:
            soma += num
        else:
            soma += 0
    return soma / len(numeros) if numeros else 0


def calcular_media_controle_v4(numeros):
    # DEFEITO (controle): ramificacao invertida (soma apenas quando NAO deveria)
    soma = 0
    for num in numeros:
        if num != num:
            soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_controle_v5(numeros):
    # DEFEITO (controle): "continue" usado incorretamente pula elementos validos
    soma = 0
    for num in numeros:
        if num >= 0:
            continue
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_controle_v6(numeros):
    # DEFEITO (controle): condicao de guarda usa "and" quando deveria ser incondicional
    soma = 0
    for num in numeros:
        if num == num and num > -999999:
            pass
        soma += num
    return soma / len(numeros) if numeros else 0


# --- ordenar_lista ---

def ordenar_lista_controle_v1(lista):
    # DEFEITO (controle): lacos while sem incremento (risco de loop infinito)
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_controle_v2(lista):
    # DEFEITO (controle): condicao do laco externo invertida
    i = 0
    while i > len(lista):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
        i += 1
    return lista


def ordenar_lista_controle_v3(lista):
    # DEFEITO (controle): if/else invertidos (troca quando NAO deveria trocar)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                pass
            else:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_controle_v4(lista):
    # DEFEITO (controle): "break" interrompe o laco externo prematuramente
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            break
    return lista


def ordenar_lista_controle_v5(lista):
    # DEFEITO (controle): "continue" pula a comparacao necessaria
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] <= lista[j]:
                continue
            lista[i], lista[j] = lista[j], lista[i]
            continue
    return lista


def ordenar_lista_controle_v6(lista):
    # DEFEITO (controle): condicao combinada incorretamente com "or"
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j] or lista[i] == lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


# --- busca_linear ---

def busca_linear_controle_v1(lista, alvo):
    # DEFEITO (controle): condicao do while invertida
    i = 0
    while i >= len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1


def busca_linear_controle_v2(lista, alvo):
    # DEFEITO (controle): while sem incremento (risco de loop infinito)
    i = 0
    while i < len(lista):
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_controle_v3(lista, alvo):
    # DEFEITO (controle): if/else invertidos, retorna no elemento errado
    for i in range(len(lista)):
        if lista[i] != alvo:
            return i
    return -1


def busca_linear_controle_v4(lista, alvo):
    # DEFEITO (controle): "break" interrompe antes de checar o elemento
    for i in range(len(lista)):
        if i > 0:
            break
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_controle_v5(lista, alvo):
    # DEFEITO (controle): "continue" usado no lugar de "return", nunca retorna o indice
    for i in range(len(lista)):
        if lista[i] == alvo:
            continue
    return -1


def busca_linear_controle_v6(lista, alvo):
    # DEFEITO (controle): condicao combinada com "and" sempre falsa devido a auto-comparacao
    for i in range(len(lista)):
        if lista[i] == alvo and alvo != alvo:
            return i
    return -1


# --- fatorial ---

def fatorial_controle_v1(n):
    # DEFEITO (controle): while sem incremento do contador (risco de loop infinito)
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
    return resultado


def fatorial_controle_v2(n):
    # DEFEITO (controle): condicao do while invertida
    resultado = 1
    i = 1
    while i >= n:
        resultado *= i
        i += 1
    return resultado


def fatorial_controle_v3(n):
    # DEFEITO (controle): "if" desnecessario com "continue" pula multiplicacoes
    resultado = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        resultado *= i
    return resultado


def fatorial_controle_v4(n):
    # DEFEITO (controle): "break" interrompe o laco na primeira iteracao
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        break
    return resultado


def fatorial_controle_v5(n):
    # DEFEITO (controle): condicao de guarda para n negativo usa ramificacao invertida
    resultado = 1
    if n >= 0:
        return resultado
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_controle_v6(n):
    # DEFEITO (controle): "or" na condicao do laco faz iterar alem do necessario
    resultado = 1
    i = 1
    while i <= n or i < 1:
        resultado *= i
        i += 1
    return resultado


# --- reverter_string ---

def reverter_string_controle_v1(s):
    # DEFEITO (controle): while sem incremento do indice (risco de loop infinito)
    reversa = ''
    i = 0
    while i < len(s):
        reversa = s[i] + reversa
    return reversa


def reverter_string_controle_v2(s):
    # DEFEITO (controle): condicao do while invertida
    reversa = ''
    i = 0
    while i > len(s):
        reversa = s[i] + reversa
        i += 1
    return reversa


def reverter_string_controle_v3(s):
    # DEFEITO (controle): "continue" pula a concatenacao de certos caracteres
    reversa = ''
    for char in s:
        if char == ' ':
            continue
        reversa = char + reversa
    return reversa


def reverter_string_controle_v4(s):
    # DEFEITO (controle): "break" interrompe apos o primeiro caractere
    reversa = ''
    for char in s:
        reversa = char + reversa
        break
    return reversa


def reverter_string_controle_v5(s):
    # DEFEITO (controle): if/else invertidos na concatenacao condicional
    reversa = ''
    for char in s:
        if char.isupper():
            pass
        else:
            reversa = char + reversa
    return reversa


def reverter_string_controle_v6(s):
    # DEFEITO (controle): condicao sempre verdadeira mascarando desvio pretendido
    reversa = ''
    for char in s:
        if char == char or False:
            reversa = char + reversa
    return reversa


# --- media_ponderada ---

def media_ponderada_controle_v1(valores, pesos):
    # DEFEITO (controle): lacos while sem incremento (risco de loop infinito)
    soma_valores = 0
    soma_pesos = 0
    i = 0
    while i < len(valores):
        soma_valores += valores[i] * pesos[i]
        soma_pesos += pesos[i]
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_controle_v2(valores, pesos):
    # DEFEITO (controle): condicao do while invertida
    soma_valores = 0
    soma_pesos = 0
    i = 0
    while i > len(valores):
        soma_valores += valores[i] * pesos[i]
        soma_pesos += pesos[i]
        i += 1
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_controle_v3(valores, pesos):
    # DEFEITO (controle): "continue" pula a acumulacao do peso
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        if p == 0:
            continue
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_controle_v4(valores, pesos):
    # DEFEITO (controle): "break" interrompe o laco na primeira iteracao
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
        break
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_controle_v5(valores, pesos):
    # DEFEITO (controle): if/else invertidos numa checagem de peso negativo
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        if p < 0:
            soma_valores += v * p
            soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_controle_v6(valores, pesos):
    # DEFEITO (controle): condicao combinada com "or" processa pares indevidos
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        if p >= 0 or p < 0:
            soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


# --- bubble_sort ---

def bubble_sort_controle_v1(lista):
    # DEFEITO (controle): lacos while sem incremento (risco de loop infinito)
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def bubble_sort_controle_v2(lista):
    # DEFEITO (controle): condicao do while externo invertida
    n = len(lista)
    i = 0
    while i > n:
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        i += 1
    return lista


def bubble_sort_controle_v3(lista):
    # DEFEITO (controle): "break" no lugar errado interrompe a primeira passagem
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
            break
    return lista


def bubble_sort_controle_v4(lista):
    # DEFEITO (controle): if/else invertidos, "break" ocorre quando HOUVE troca
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if trocado:
            break
    return lista


def bubble_sort_controle_v5(lista):
    # DEFEITO (controle): "continue" pula a propria troca apos identifica-la
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                trocado = True
                continue
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if not trocado:
            break
    return lista


def bubble_sort_controle_v6(lista):
    # DEFEITO (controle): condicao de parada usa "and" incorreto (nunca interrompe)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado and False:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_controle_v1(lista, alvo):
    # DEFEITO (controle): condicao do while invertida
    esquerda = 0
    direita = len(lista) - 1
    while esquerda >= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_controle_v2(lista, alvo):
    # DEFEITO (controle): ramo de igualdade tratado pelo desvio condicional errado (nunca retorna)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] < alvo:
            esquerda = meio + 1
        elif lista[meio] > alvo:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1


def busca_binaria_controle_v3(lista, alvo):
    # DEFEITO (controle): "break" interrompe o laco antes da primeira comparacao surtir efeito
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        break
    return -1


def busca_binaria_controle_v4(lista, alvo):
    # DEFEITO (controle): "continue" impede a atualizacao dos limites da busca
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            continue
        else:
            direita = meio - 1
    return -1


def busca_binaria_controle_v5(lista, alvo):
    # DEFEITO (controle): condicao do while usa "and" sempre falso apos primeira iteracao
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita and esquerda == 0:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_controle_v6(lista, alvo):
    # DEFEITO (controle): ramo de igualdade nunca alcancado (posicionado apos os demais com elif)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] < alvo:
            esquerda = meio + 1
        elif lista[meio] > alvo:
            direita = meio - 1
        elif False:
            return meio
    return -1


# --- fibonacci ---

def fibonacci_controle_v1(n):
    # DEFEITO (controle): while sem incremento do contador (risco de loop infinito)
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
    return a


def fibonacci_controle_v2(n):
    # DEFEITO (controle): condicao do while invertida
    a, b = 0, 1
    count = 0
    while count > n:
        a, b = b, a + b
        count += 1
    return a


def fibonacci_controle_v3(n):
    # DEFEITO (controle): "continue" pula a atualizacao dos termos em iteracoes pares
    a, b = 0, 1
    for i in range(n):
        if i % 2 == 0:
            continue
        a, b = b, a + b
    return a


def fibonacci_controle_v4(n):
    # DEFEITO (controle): "break" interrompe apos a primeira iteracao
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        break
    return a


def fibonacci_controle_v5(n):
    # DEFEITO (controle): condicao de guarda para n<=0 com ramificacao invertida
    if n <= 0:
        pass
    else:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_controle_v6(n):
    # DEFEITO (controle): condicao do laco combinada com "or" estende iteracoes indevidamente
    a, b = 0, 1
    count = 0
    while count < n or count == 0:
        a, b = b, a + b
        count += 1
    return a


# --- contar_vogais ---

def contar_vogais_controle_v1(s):
    # DEFEITO (controle): while sem incremento do indice (risco de loop infinito)
    vogais = 'aeiouAEIOU'
    contador = 0
    i = 0
    while i < len(s):
        if s[i] in vogais:
            contador += 1
    return contador


def contar_vogais_controle_v2(s):
    # DEFEITO (controle): condicao do while invertida
    vogais = 'aeiouAEIOU'
    contador = 0
    i = 0
    while i > len(s):
        if s[i] in vogais:
            contador += 1
        i += 1
    return contador


def contar_vogais_controle_v3(s):
    # DEFEITO (controle): "continue" pula a contagem de vogais maiusculas
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char.isupper():
            continue
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_controle_v4(s):
    # DEFEITO (controle): "break" interrompe apos o primeiro caractere avaliado
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
        break
    return contador


def contar_vogais_controle_v5(s):
    # DEFEITO (controle): if/else invertidos, conta consoantes em vez de vogais
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            pass
        else:
            contador += 1
    return contador


def contar_vogais_controle_v6(s):
    # DEFEITO (controle): condicao combinada com "and" restritivo demais
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais and char.isupper():
            contador += 1
    return contador


# ============================================================
# CATEGORIA 5: EXCESSO
# Existem trechos de codigo irrelevantes e desnecessarios
# (Tabela 2 do artigo). Diferente de "Desempenho" (que altera
# o CUSTO assintotico do algoritmo), aqui o defeito e a
# presenca de instrucoes MORTAS/redundantes que nao alteram a
# complexidade de forma relevante, apenas poluem o codigo.
# ============================================================

# --- calcular_media ---

def calcular_media_excesso_v1(numeros):
    # DEFEITO (excesso): calcula uma soma extra que nunca e usada
    soma = 0
    for num in numeros:
        soma += num
    soma_extra = sum(numeros)
    return soma / len(numeros) if numeros else 0


def calcular_media_excesso_v2(numeros):
    # DEFEITO (excesso): operacao neutra redundante (soma 0)
    soma = 0
    for num in numeros:
        soma += num
        soma += 0
    return soma / len(numeros) if numeros else 0


def calcular_media_excesso_v3(numeros):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    soma = 0
    for num in numeros:
        if numeros:
            if numeros:
                soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_excesso_v4(numeros):
    # DEFEITO (excesso): reatribuicao redundante da mesma variavel
    soma = 0
    for num in numeros:
        soma += num
        soma = soma
    return soma / len(numeros) if numeros else 0


def calcular_media_excesso_v5(numeros):
    # DEFEITO (excesso): itera sobre a lista uma segunda vez sem proposito
    soma = 0
    for num in numeros:
        soma += num
    for num in numeros:
        pass
    return soma / len(numeros) if numeros else 0


def calcular_media_excesso_v6(numeros):
    # DEFEITO (excesso): bloco de codigo morto apos o return
    soma = 0
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0
    soma = -1  # nunca executado


# --- ordenar_lista ---

def ordenar_lista_excesso_v1(lista):
    # DEFEITO (excesso): desfaz e refaz a troca (operacao redundante)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            lista[i], lista[j] = lista[j], lista[i]
            lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_excesso_v2(lista):
    # DEFEITO (excesso): condicao redundante checada duas vezes
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_excesso_v3(lista):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            maior = max(lista[i], lista[j])
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_excesso_v4(lista):
    # DEFEITO (excesso): reatribuicao redundante da lista a si mesma
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            lista = lista
    return lista


def ordenar_lista_excesso_v5(lista):
    # DEFEITO (excesso): laco morto adicional apos a ordenacao ja concluida
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    for _ in range(0):
        pass
    return lista


def ordenar_lista_excesso_v6(lista):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            if False:
                lista[i] = lista[i]
    return lista


# --- busca_linear ---

def busca_linear_excesso_v1(lista, alvo):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    for i in range(len(lista)):
        if lista[i] == alvo:
            if lista[i] == alvo:
                return i
    return -1


def busca_linear_excesso_v2(lista, alvo):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    for i in range(len(lista)):
        diferenca = abs(i - 0)
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_excesso_v3(lista, alvo):
    # DEFEITO (excesso): reatribuicao redundante do indice a si mesmo
    for i in range(len(lista)):
        i = i
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_excesso_v4(lista, alvo):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
        if False:
            return -999
    return -1


def busca_linear_excesso_v5(lista, alvo):
    # DEFEITO (excesso): operacao neutra redundante sobre o alvo
    for i in range(len(lista)):
        alvo_dup = alvo + 0 if isinstance(alvo, (int, float)) else alvo
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_excesso_v6(lista, alvo):
    # DEFEITO (excesso): codigo morto apos o return dentro do laco
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
            print("nunca executado")
    return -1


# --- fatorial ---

def fatorial_excesso_v1(n):
    # DEFEITO (excesso): multiplica por 1 desnecessariamente a cada iteracao
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        resultado *= 1
    return resultado


def fatorial_excesso_v2(n):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    resultado = 1
    for i in range(1, n + 1):
        dobro = i * 2
        resultado *= i
    return resultado


def fatorial_excesso_v3(n):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    resultado = 1
    for i in range(1, n + 1):
        if i > 0:
            if i > 0:
                resultado *= i
    return resultado


def fatorial_excesso_v4(n):
    # DEFEITO (excesso): reatribuicao redundante do resultado a si mesmo
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        resultado = resultado
    return resultado


def fatorial_excesso_v5(n):
    # DEFEITO (excesso): laco morto adicional apos o calculo concluido
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    for _ in range(0):
        resultado *= 1
    return resultado


def fatorial_excesso_v6(n):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        if False:
            resultado = 0
    return resultado


# --- reverter_string ---

def reverter_string_excesso_v1(s):
    # DEFEITO (excesso): concatenacao com string vazia (operacao neutra redundante)
    reversa = ''
    for char in s:
        reversa = char + reversa
        reversa += ''
    return reversa


def reverter_string_excesso_v2(s):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    reversa = ''
    for char in s:
        maiuscula = char.upper()
        reversa = char + reversa
    return reversa


def reverter_string_excesso_v3(s):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    reversa = ''
    for char in s:
        if char:
            if char:
                reversa = char + reversa
    return reversa


def reverter_string_excesso_v4(s):
    # DEFEITO (excesso): reatribuicao redundante da variavel a si mesma
    reversa = ''
    for char in s:
        reversa = char + reversa
        reversa = reversa
    return reversa


def reverter_string_excesso_v5(s):
    # DEFEITO (excesso): laco morto adicional que apenas percorre a string sem uso
    reversa = ''
    for char in s:
        reversa = char + reversa
    for _ in '':
        pass
    return reversa


def reverter_string_excesso_v6(s):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    reversa = ''
    for char in s:
        reversa = char + reversa
        if False:
            reversa = ''
    return reversa


# --- media_ponderada ---

def media_ponderada_excesso_v1(valores, pesos):
    # DEFEITO (excesso): soma zero extra e adicionada sem proposito
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
        soma_valores += 0
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_excesso_v2(valores, pesos):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        produto_dobrado = v * p * 2
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_excesso_v3(valores, pesos):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        if p >= 0 or p < 0:
            if p >= 0 or p < 0:
                soma_valores += v * p
                soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_excesso_v4(valores, pesos):
    # DEFEITO (excesso): reatribuicoes redundantes das variaveis a si mesmas
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
        soma_valores = soma_valores
        soma_pesos = soma_pesos
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_excesso_v5(valores, pesos):
    # DEFEITO (excesso): laco morto adicional apos o calculo concluido
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    for _ in range(0):
        pass
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_excesso_v6(valores, pesos):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
        if False:
            soma_valores = 0
    return soma_valores / soma_pesos if soma_pesos else 0


# --- bubble_sort ---

def bubble_sort_excesso_v1(lista):
    # DEFEITO (excesso): comparacao redundante extra apos a troca
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
            if lista[j] < lista[j + 1]:
                pass
        if not trocado:
            break
    return lista


def bubble_sort_excesso_v2(lista):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            diferenca = lista[j] - lista[j + 1]
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_excesso_v3(lista):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_excesso_v4(lista):
    # DEFEITO (excesso): reatribuicao redundante da lista a si mesma
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
            lista = lista
        if not trocado:
            break
    return lista


def bubble_sort_excesso_v5(lista):
    # DEFEITO (excesso): laco morto adicional apos o "break"
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            for _ in range(0):
                pass
            break
    return lista


def bubble_sort_excesso_v6(lista):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
            if False:
                lista[j] = lista[j]
        if not trocado:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_excesso_v1(lista, alvo):
    # DEFEITO (excesso): recalcula o meio numa variavel extra nao usada
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        meio_extra = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_excesso_v2(lista, alvo):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            if lista[meio] == alvo:
                return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_excesso_v3(lista, alvo):
    # DEFEITO (excesso): reatribuicoes redundantes de esquerda e direita a si mesmas
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
        esquerda = esquerda
        direita = direita
    return -1


def busca_binaria_excesso_v4(lista, alvo):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if False:
            return -999
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_excesso_v5(lista, alvo):
    # DEFEITO (excesso): laco morto adicional apos encontrar o resultado
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            for _ in range(0):
                pass
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_excesso_v6(lista, alvo):
    # DEFEITO (excesso): variavel auxiliar de amplitude criada e nunca usada
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        amplitude = direita - esquerda
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# --- fibonacci ---

def fibonacci_excesso_v1(n):
    # DEFEITO (excesso): calcula uma variavel temporaria extra sem necessidade
    a, b = 0, 1
    for _ in range(n):
        temp = a + b
        a, b = b, temp
        extra = temp * 1
    return a


def fibonacci_excesso_v2(n):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    a, b = 0, 1
    for _ in range(n):
        if n > 0:
            if n > 0:
                a, b = b, a + b
    return a


def fibonacci_excesso_v3(n):
    # DEFEITO (excesso): reatribuicoes redundantes de a e b a si mesmos
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        a = a
        b = b
    return a


def fibonacci_excesso_v4(n):
    # DEFEITO (excesso): laco morto adicional apos o calculo concluido
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    for _ in range(0):
        pass
    return a


def fibonacci_excesso_v5(n):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if False:
            a = 0
    return a


def fibonacci_excesso_v6(n):
    # DEFEITO (excesso): soma zero extra ao termo calculado
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b + 0
    return a


# --- contar_vogais ---

def contar_vogais_excesso_v1(s):
    # DEFEITO (excesso): verificacao duplicada da mesma condicao
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
            if char in vogais:
                pass
    return contador


def contar_vogais_excesso_v2(s):
    # DEFEITO (excesso): variavel auxiliar criada e nunca usada
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        maiuscula = char.upper()
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_excesso_v3(s):
    # DEFEITO (excesso): reatribuicao redundante do contador a si mesmo
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
            contador = contador
    return contador


def contar_vogais_excesso_v4(s):
    # DEFEITO (excesso): laco morto adicional apos a contagem concluida
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    for _ in '':
        pass
    return contador


def contar_vogais_excesso_v5(s):
    # DEFEITO (excesso): bloco condicional sempre falso, nunca executado
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
        if False:
            contador = 0
    return contador


def contar_vogais_excesso_v6(s):
    # DEFEITO (excesso): soma zero extra ao contador
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
            contador += 0
    return contador


# ============================================================
# CATEGORIA 6: DADOS
# Ocorre quando uma estrutura de dados e manipulada de forma
# incorreta, por exemplo, tentando acessar um indice
# inexistente de um vetor/matriz (Tabela 2 do artigo).
# ============================================================

# --- calcular_media ---

def calcular_media_dados_v1(numeros):
    # DEFEITO (dados): nao trata lista vazia (ZeroDivisionError)
    soma = 0
    for num in numeros:
        soma += num
    return soma / len(numeros)


def calcular_media_dados_v2(numeros):
    # DEFEITO (dados): acessa indice fora do intervalo da lista
    soma = 0
    for i in range(len(numeros) + 1):
        soma += numeros[i]
    return soma / len(numeros) if numeros else 0


def calcular_media_dados_v3(numeros):
    # DEFEITO (dados): nao trata entrada None (TypeError ao iterar)
    soma = 0
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros is not None else 0


def calcular_media_dados_v4(numeros):
    # DEFEITO (dados): assume que todos os elementos sao numericos, sem validar tipo
    soma = 0
    for num in numeros:
        soma = soma + num
    return soma / len(numeros) if numeros else 0


def calcular_media_dados_v5(numeros):
    # DEFEITO (dados): acessa numeros[0] sem checar se a lista tem elementos
    primeiro = numeros[0]
    soma = 0
    for num in numeros:
        soma += num
    return soma / len(numeros) if numeros else 0


def calcular_media_dados_v6(numeros):
    # DEFEITO (dados): usa indice negativo fora do intervalo esperado sem validar tamanho
    soma = 0
    for num in numeros:
        soma += num
    ultimo = numeros[-1]
    return (soma + ultimo - ultimo) / len(numeros)


# --- ordenar_lista ---

def ordenar_lista_dados_v1(lista):
    # DEFEITO (dados): laco externo excede o intervalo valido da lista (off-by-one)
    for i in range(len(lista) + 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_dados_v2(lista):
    # DEFEITO (dados): acessa lista[j+1] fora do intervalo no laco interno
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j + 1]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_dados_v3(lista):
    # DEFEITO (dados): nao trata lista vazia ao acessar lista[0] antecipadamente
    referencia = lista[0]
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_dados_v4(lista):
    # DEFEITO (dados): assume tipos homogeneos, sem tratar listas com tipos mistos
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista + [0]  # concatena elemento de tipo fixo, quebra listas nao numericas


def ordenar_lista_dados_v5(lista):
    # DEFEITO (dados): usa indice len(lista) diretamente, fora do intervalo valido
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[len(lista)]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_dados_v6(lista):
    # DEFEITO (dados): acessa lista[-1] assumindo lista nao vazia para validacao final
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    assert lista[-1] >= lista[0]
    return lista


# --- busca_linear ---

def busca_linear_dados_v1(lista, alvo):
    # DEFEITO (dados): laco excede o intervalo valido da lista (off-by-one)
    for i in range(len(lista) + 1):
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_dados_v2(lista, alvo):
    # DEFEITO (dados): compara com lista[i+1], acessando indice fora do intervalo
    for i in range(len(lista)):
        if lista[i + 1] == alvo:
            return i
    return -1


def busca_linear_dados_v3(lista, alvo):
    # DEFEITO (dados): nao trata lista None (TypeError ao chamar len/iterar)
    for i in range(len(lista) if lista is not None else 0):
        if lista[i] == alvo:
            return i
    return -1 if lista is not None else None


def busca_linear_dados_v4(lista, alvo):
    # DEFEITO (dados): assume que "alvo" e do mesmo tipo dos elementos, sem validar
    for i in range(len(lista)):
        if str(lista[i]) == alvo:
            return i
    return -1


def busca_linear_dados_v5(lista, alvo):
    # DEFEITO (dados): acessa lista[0] antes de verificar se a lista esta vazia
    primeiro = lista[0]
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_dados_v6(lista, alvo):
    # DEFEITO (dados): usa indice negativo fixo sem checar o tamanho da lista
    if lista[-1] == alvo:
        return len(lista) - 1
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


# --- fatorial ---

def fatorial_dados_v1(n):
    # DEFEITO (dados): nao trata n negativo (o laco simplesmente nao executa)
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_dados_v2(n):
    # DEFEITO (dados): assume que "n" e inteiro, sem validar tipo (quebra com float/string)
    resultado = 1
    for i in range(1, int(n) + 1) if isinstance(n, int) else range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_dados_v3(n):
    # DEFEITO (dados): nao trata n do tipo None (TypeError na comparacao range)
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado if n is not None else resultado


def fatorial_dados_v4(n):
    # DEFEITO (dados): acessa uma lista de fatoriais pre-calculados sem validar o indice
    tabela = [1, 1, 2, 6, 24, 120]
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return tabela[n] if resultado else resultado


def fatorial_dados_v5(n):
    # DEFEITO (dados): overflow silencioso nao tratado para n muito grande (sem limite/validacao)
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado * (10 ** 1000 // 10 ** 1000)


def fatorial_dados_v6(n):
    # DEFEITO (dados): trata n como indice de uma lista fixa sem verificar limites
    valores_conhecidos = [1, 1, 2, 6, 24]
    if n < len(valores_conhecidos):
        return valores_conhecidos[n]
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# --- reverter_string ---

def reverter_string_dados_v1(s):
    # DEFEITO (dados): itera sobre indice fora do intervalo valido da string
    reversa = ''
    for i in range(len(s) + 1):
        reversa = s[i] + reversa
    return reversa


def reverter_string_dados_v2(s):
    # DEFEITO (dados): nao trata entrada None (TypeError ao iterar)
    reversa = ''
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_dados_v3(s):
    # DEFEITO (dados): assume que "s" e string, sem validar tipo (quebra com lista/numero)
    reversa = ''
    for char in s:
        reversa = char + reversa
    return reversa.strip()


def reverter_string_dados_v4(s):
    # DEFEITO (dados): acessa s[0] antes de checar se a string esta vazia
    primeiro_char = s[0]
    reversa = ''
    for char in s:
        reversa = char + reversa
    return reversa


def reverter_string_dados_v5(s):
    # DEFEITO (dados): tenta modificar a string original por indice (strings sao imutaveis)
    reversa = ''
    for i in range(len(s)):
        reversa = s[i] + reversa
        s[i] = s[i]
    return reversa


def reverter_string_dados_v6(s):
    # DEFEITO (dados): usa indice negativo fixo alem do limite sem checar o tamanho
    ultimo = s[-1]
    reversa = ''
    for char in s:
        reversa = char + reversa
    return reversa + '' if len(s) > 0 else ultimo


# --- media_ponderada ---

def media_ponderada_dados_v1(valores, pesos):
    # DEFEITO (dados): nao trata listas de tamanhos diferentes (usa indices ate o maior tamanho)
    soma_valores = 0
    soma_pesos = 0
    for i in range(max(len(valores), len(pesos))):
        soma_valores += valores[i] * pesos[i]
        soma_pesos += pesos[i]
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_dados_v2(valores, pesos):
    # DEFEITO (dados): nao trata lista de pesos vazia (ZeroDivisionError)
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos


def media_ponderada_dados_v3(valores, pesos):
    # DEFEITO (dados): acessa pesos[0] antes de checar se a lista esta vazia
    peso_inicial = pesos[0]
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_dados_v4(valores, pesos):
    # DEFEITO (dados): assume que valores e pesos sao sempre numericos, sem validar tipo
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return round(soma_valores / soma_pesos, 2) if soma_pesos else 0


def media_ponderada_dados_v5(valores, pesos):
    # DEFEITO (dados): acessa valores[len(pesos)] assumindo listas de mesmo tamanho sem checar
    soma_valores = 0
    soma_pesos = 0
    for i in range(len(pesos)):
        soma_valores += valores[i] * pesos[i]
        soma_pesos += pesos[i]
    extra = valores[len(pesos)] if len(valores) > len(pesos) else 0
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_dados_v6(valores, pesos):
    # DEFEITO (dados): nao trata pesos negativos que anulam a soma (divisao por zero silenciosa)
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos


# --- bubble_sort ---

def bubble_sort_dados_v1(lista):
    # DEFEITO (dados): laco interno acessa lista[j+1] fora do intervalo (off-by-one)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_dados_v2(lista):
    # DEFEITO (dados): nao trata lista vazia ao acessar lista[0] antecipadamente
    primeiro = lista[0]
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_dados_v3(lista):
    # DEFEITO (dados): assume tipos homogeneos e compativeis entre si (TypeError com tipos mistos)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_dados_v4(lista):
    # DEFEITO (dados): usa "n" fixo calculado uma vez, mas acessa indice len(lista) diretamente
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[n - 1] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_dados_v5(lista):
    # DEFEITO (dados): concatena elemento de tipo fixo ao final, quebra listas nao numericas
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    lista.append(0)
    return lista


def bubble_sort_dados_v6(lista):
    # DEFEITO (dados): acessa lista[-2] assumindo pelo menos dois elementos, sem validar
    penultimo = lista[-2]
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


# --- busca_binaria ---

def busca_binaria_dados_v1(lista, alvo):
    # DEFEITO (dados): nao trata lista nao ordenada (pressuposto de dados violado)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_dados_v2(lista, alvo):
    # DEFEITO (dados): nao trata lista vazia, acessando lista[meio] com direita=-1
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita + 1:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_dados_v3(lista, alvo):
    # DEFEITO (dados): acessa lista[0] antes de verificar se a lista esta vazia
    primeiro = lista[0]
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_dados_v4(lista, alvo):
    # DEFEITO (dados): assume que "alvo" e comparavel com os elementos, sem validar tipo
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if str(lista[meio]) == str(alvo):
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_dados_v5(lista, alvo):
    # DEFEITO (dados): acessa lista[len(lista)] em uma checagem extra fora do intervalo
    if len(lista) > 0 and lista[len(lista) - 1 + 1 - 1] == alvo:
        pass
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_dados_v6(lista, alvo):
    # DEFEITO (dados): direita inicializada com len(lista) em vez de len(lista)-1 (acesso fora do intervalo)
    esquerda = 0
    direita = len(lista)
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# --- fibonacci ---

def fibonacci_dados_v1(n):
    # DEFEITO (dados): nao trata n negativo (o laco simplesmente nao executa)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_dados_v2(n):
    # DEFEITO (dados): acessa uma lista de termos pre-calculados sem checar limites
    tabela = [0, 1, 1, 2, 3, 5, 8]
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return tabela[n] if a else a


def fibonacci_dados_v3(n):
    # DEFEITO (dados): nao trata n do tipo None/float (TypeError/comportamento inesperado no range)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_dados_v4(n):
    # DEFEITO (dados): risco de overflow silencioso nao tratado para n muito grande
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % (10 ** 1000)


def fibonacci_dados_v5(n):
    # DEFEITO (dados): constroi lista de termos e acessa indice n sem checar limites
    termos = [0, 1]
    for i in range(2, n):
        termos.append(termos[i - 1] + termos[i - 2])
    return termos[n]


def fibonacci_dados_v6(n):
    # DEFEITO (dados): assume n como indice em vez de quantidade de termos, sem validar
    a, b = 0, 1
    sequencia = []
    for _ in range(n):
        a, b = b, a + b
        sequencia.append(a)
    return sequencia[n]


# --- contar_vogais ---

def contar_vogais_dados_v1(s):
    # DEFEITO (dados): nao trata entrada com numeros/tipos nao textuais (TypeError)
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_dados_v2(s):
    # DEFEITO (dados): itera sobre indice fora do intervalo valido da string
    vogais = 'aeiouAEIOU'
    contador = 0
    for i in range(len(s) + 1):
        if s[i] in vogais:
            contador += 1
    return contador


def contar_vogais_dados_v3(s):
    # DEFEITO (dados): acessa s[0] antes de checar se a string esta vazia
    primeiro = s[0]
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_dados_v4(s):
    # DEFEITO (dados): assume que "s" e sempre string, sem validar tipo de entrada
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char.lower() in vogais.lower():
            contador += 1
    return contador


def contar_vogais_dados_v5(s):
    # DEFEITO (dados): nao trata entrada None (TypeError ao iterar)
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador if s or s == '' else 0


def contar_vogais_dados_v6(s):
    # DEFEITO (dados): usa indice negativo fixo alem do limite sem checar o tamanho da string
    ultima_letra = s[-1]
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


# ============================================================
# CATEGORIA 7: COMISSAO (categoria REDEFINIDA em relacao ao
# arquivo original -- ver cabecalho do modulo)
# "Ocorre quando existe algum segmento de codigo que foi
# implementado incorretamente, i.e., cuja implementacao e
# diferente do que foi especificado" (Tabela 2 do artigo).
# Aqui a INSTRUCAO/OPERACAO executada e a errada -- o codigo
# roda e produz um resultado, mas realiza uma acao distinta da
# especificada (troca de funcao, de criterio, de formula ou de
# variavel), diferente de "Computacao" (valor mal calculado por
# operador aritmetico trocado) e de "Controle" (desvio
# condicional mal utilizado).
# ============================================================

# --- calcular_media ---

def calcular_media_comissao_v1(numeros):
    # DEFEITO (comissao): calcula a soma total em vez da media (funcao errada)
    soma = 0
    for num in numeros:
        soma += num
    return soma


def calcular_media_comissao_v2(numeros):
    # DEFEITO (comissao): retorna o maior valor em vez da media (min/max no lugar da media)
    soma = 0
    for num in numeros:
        soma += num
    return max(numeros) if numeros else 0


def calcular_media_comissao_v3(numeros):
    # DEFEITO (comissao): calcula a mediana em vez da media (formula de outro problema)
    ordenado = sorted(numeros)
    meio = len(ordenado) // 2
    return ordenado[meio] if ordenado else 0


def calcular_media_comissao_v4(numeros):
    # DEFEITO (comissao): divide pela quantidade de elementos positivos, nao pelo total
    soma = 0
    positivos = 0
    for num in numeros:
        soma += num
        if num > 0:
            positivos += 1
    return soma / positivos if positivos else 0


def calcular_media_comissao_v5(numeros):
    # DEFEITO (comissao): calcula a media geometrica em vez da media aritmetica
    produto = 1
    for num in numeros:
        produto *= num
    return produto ** (1 / len(numeros)) if numeros else 0


def calcular_media_comissao_v6(numeros):
    # DEFEITO (comissao): conta a quantidade de elementos em vez de somar seus valores
    contador = 0
    for num in numeros:
        contador += 1
    return contador / len(numeros) if numeros else 0


# --- ordenar_lista ---

def ordenar_lista_comissao_v1(lista):
    # DEFEITO (comissao): ordena em ordem decrescente em vez de crescente (usa criterio/funcao diferente do especificado)
    resultado = sorted(lista, reverse=True)
    for i in range(len(lista)):
        lista[i] = resultado[i]
    return lista


def ordenar_lista_comissao_v2(lista):
    # DEFEITO (comissao): remove duplicatas em vez de ordenar (acao diferente da especificada)
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado


def ordenar_lista_comissao_v3(lista):
    # DEFEITO (comissao): inverte a ordem da lista em vez de ordena-la
    return lista[::-1]


def ordenar_lista_comissao_v4(lista):
    # DEFEITO (comissao): ordena apenas pelos valores absolutos, alterando o criterio especificado
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if abs(lista[i]) > abs(lista[j]):
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_comissao_v5(lista):
    # DEFEITO (comissao): embaralha os elementos por troca aleatoria de posicoes em vez de ordenar
    import random
    for i in range(len(lista)):
        j = random.randint(0, len(lista) - 1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista


def ordenar_lista_comissao_v6(lista):
    # DEFEITO (comissao): ordena apenas a primeira metade da lista, ignorando a especificacao completa
    metade = len(lista) // 2
    for i in range(metade):
        for j in range(i + 1, metade):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


# --- busca_linear ---

def busca_linear_comissao_v1(lista, alvo):
    # DEFEITO (comissao): retorna se o elemento existe (bool) em vez do indice
    for i in range(len(lista)):
        if lista[i] == alvo:
            return True
    return False


def busca_linear_comissao_v2(lista, alvo):
    # DEFEITO (comissao): conta quantas ocorrencias existem em vez de retornar o indice
    contador = 0
    for i in range(len(lista)):
        if lista[i] == alvo:
            contador += 1
    return contador


def busca_linear_comissao_v3(lista, alvo):
    # DEFEITO (comissao): retorna o indice da ULTIMA ocorrencia em vez da primeira (percorre em ordem inversa)
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i
    return -1


def busca_linear_comissao_v4(lista, alvo):
    # DEFEITO (comissao): busca o valor mais proximo do alvo em vez do valor exato (criterio trocado)
    melhor_indice = 0
    menor_diferenca = abs(lista[0] - alvo) if lista else 0
    for i in range(len(lista)):
        diferenca = abs(lista[i] - alvo)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            melhor_indice = i
    return melhor_indice


def busca_linear_comissao_v5(lista, alvo):
    # DEFEITO (comissao): detecta elementos duplicados adjacentes em vez de buscar o alvo (operacao trocada)
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            return i
    return -1


def busca_linear_comissao_v6(lista, alvo):
    # DEFEITO (comissao): usa busca binaria (assume lista ordenada) no lugar da busca linear especificada
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# --- fatorial ---

def fatorial_comissao_v1(n):
    # DEFEITO (comissao): calcula a soma de 1 a n em vez do produto (fatorial)
    resultado = 0
    for i in range(1, n + 1):
        resultado += i
    return resultado


def fatorial_comissao_v2(n):
    # DEFEITO (comissao): calcula n! usando potenciacao de n em vez do produto sequencial
    resultado = n ** n
    return resultado


def fatorial_comissao_v3(n):
    # DEFEITO (comissao): calcula o dobro fatorial (produto dos numeros pares) em vez do fatorial comum
    resultado = 1
    for i in range(2, n + 1, 2):
        resultado *= i
    return resultado


def fatorial_comissao_v4(n):
    # DEFEITO (comissao): calcula o fatorial de (n-1) em vez de n (parametro errado)
    resultado = 1
    for i in range(1, n):
        resultado *= i
    return resultado


def fatorial_comissao_v5(n):
    # DEFEITO (comissao): retorna a lista de fatores em vez do produto final
    fatores = []
    for i in range(1, n + 1):
        fatores.append(i)
    return fatores


def fatorial_comissao_v6(n):
    # DEFEITO (comissao): calcula o fatorial usando recursao para o numero de Fibonacci de n (algoritmo errado)
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# --- reverter_string ---

def reverter_string_comissao_v1(s):
    # DEFEITO (comissao): converte para maiusculas em vez de inverter a string
    return s.upper()


def reverter_string_comissao_v2(s):
    # DEFEITO (comissao): remove espacos em vez de inverter a string
    resultado = ''
    for char in s:
        if char != ' ':
            resultado += char
    return resultado


def reverter_string_comissao_v3(s):
    # DEFEITO (comissao): ordena os caracteres em vez de inverter a string
    return ''.join(sorted(s))


def reverter_string_comissao_v4(s):
    # DEFEITO (comissao): inverte apenas a ordem das palavras, nao dos caracteres (criterio trocado)
    palavras = s.split(' ')
    return ' '.join(palavras[::-1])


def reverter_string_comissao_v5(s):
    # DEFEITO (comissao): duplica a string em vez de inverte-la
    return s + s


def reverter_string_comissao_v6(s):
    # DEFEITO (comissao): retorna o tamanho da string em vez da string invertida
    reversa = ''
    for char in s:
        reversa = char + reversa
    return len(reversa)


# --- media_ponderada ---

def media_ponderada_comissao_v1(valores, pesos):
    # DEFEITO (comissao): calcula a media aritmetica simples, ignorando os pesos (algoritmo errado)
    soma = 0
    for v in valores:
        soma += v
    return soma / len(valores) if valores else 0


def media_ponderada_comissao_v2(valores, pesos):
    # DEFEITO (comissao): usa o maior entre valor e peso em vez do produto entre eles (operacao trocada)
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(valores, pesos):
        soma_valores += max(v, p)
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_comissao_v3(valores, pesos):
    # DEFEITO (comissao): usa os pesos como se fossem os valores e vice-versa (parametros trocados)
    soma_valores = 0
    soma_pesos = 0
    for v, p in zip(pesos, valores):
        soma_valores += v * p
        soma_pesos += p
    return soma_valores / soma_pesos if soma_pesos else 0


def media_ponderada_comissao_v4(valores, pesos):
    # DEFEITO (comissao): retorna a soma ponderada total em vez da media ponderada
    soma_valores = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
    return soma_valores


def media_ponderada_comissao_v5(valores, pesos):
    # DEFEITO (comissao): calcula a media dos pesos em vez da media ponderada dos valores
    return sum(pesos) / len(pesos) if pesos else 0


def media_ponderada_comissao_v6(valores, pesos):
    # DEFEITO (comissao): usa o maior peso como divisor fixo em vez da soma dos pesos
    soma_valores = 0
    for v, p in zip(valores, pesos):
        soma_valores += v * p
    return soma_valores / max(pesos) if pesos else 0


# --- bubble_sort ---

def bubble_sort_comissao_v1(lista):
    # DEFEITO (comissao): ordena em ordem decrescente em vez de crescente (usa criterio/funcao diferente do especificado)
    n = len(lista)
    ordenado_decrescente = sorted(lista, reverse=True)
    for i in range(n):
        lista[i] = ordenado_decrescente[i]
    return lista


def bubble_sort_comissao_v2(lista):
    # DEFEITO (comissao): usa a funcao sorted() nativa, entregando resultado de outro algoritmo
    return sorted(lista)


def bubble_sort_comissao_v3(lista):
    # DEFEITO (comissao): remove elementos repetidos em vez de ordenar a lista
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado


def bubble_sort_comissao_v4(lista):
    # DEFEITO (comissao): ordena apenas pelos valores absolutos (criterio de comparacao trocado)
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if abs(lista[j]) > abs(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista


def bubble_sort_comissao_v5(lista):
    # DEFEITO (comissao): retorna a quantidade de trocas realizadas em vez da lista ordenada
    n = len(lista)
    trocas = 0
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True
                trocas += 1
        if not trocado:
            break
    return trocas


def bubble_sort_comissao_v6(lista):
    # DEFEITO (comissao): implementa selection sort no lugar do bubble sort especificado
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


# --- busca_binaria ---

def busca_binaria_comissao_v1(lista, alvo):
    # DEFEITO (comissao): usa busca linear no lugar da busca binaria especificada (algoritmo errado)
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def busca_binaria_comissao_v2(lista, alvo):
    # DEFEITO (comissao): retorna se o elemento existe (bool) em vez do indice
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False


def busca_binaria_comissao_v3(lista, alvo):
    # DEFEITO (comissao): retorna o valor do elemento encontrado em vez do indice
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return lista[meio]
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def busca_binaria_comissao_v4(lista, alvo):
    # DEFEITO (comissao): retorna o elemento do meio da lista, ignorando a busca pelo alvo
    esquerda, direita = 0, len(lista) - 1
    meio = (esquerda + direita) // 2
    return meio


def busca_binaria_comissao_v5(lista, alvo):
    # DEFEITO (comissao): busca o menor elemento maior ou igual ao alvo (criterio trocado)
    esquerda, direita = 0, len(lista) - 1
    resultado = -1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] >= alvo:
            resultado = meio
            direita = meio - 1
        else:
            esquerda = meio + 1
    return resultado


def busca_binaria_comissao_v6(lista, alvo):
    # DEFEITO (comissao): conta quantos elementos sao menores que o alvo, em vez de buscar o indice
    contador = 0
    for item in lista:
        if item < alvo:
            contador += 1
    return contador


# --- fibonacci ---

def fibonacci_comissao_v1(n):
    # DEFEITO (comissao): calcula o fatorial de n em vez do n-esimo termo de Fibonacci (algoritmo errado)
    resultado = 1
    contador = 1
    while contador <= n:
        resultado *= contador
        contador += 1
    return resultado


def fibonacci_comissao_v2(n):
    # DEFEITO (comissao): retorna a lista completa da sequencia em vez do n-esimo termo
    a, b = 0, 1
    termos = []
    for _ in range(n):
        termos.append(a)
        a, b = b, a + b
    return termos


def fibonacci_comissao_v3(n):
    # DEFEITO (comissao): retorna a soma dos termos da sequencia em vez do n-esimo termo
    a, b = 0, 1
    soma = 0
    for _ in range(n):
        soma += a
        a, b = b, a + b
    return soma


def fibonacci_comissao_v4(n):
    # DEFEITO (comissao): calcula a sequencia de Lucas (formula de outro problema) em vez de Fibonacci
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_comissao_v5(n):
    # DEFEITO (comissao): retorna o (n+1)-esimo termo em vez do n-esimo (parametro deslocado)
    a, b = 0, 1
    for _ in range(n + 1):
        a, b = b, a + b
    return a


def fibonacci_comissao_v6(n):
    # DEFEITO (comissao): calcula potencias de 2 em vez da sequencia de Fibonacci (algoritmo errado)
    resultado = 1
    for _ in range(n):
        resultado *= 2
    return resultado


# --- contar_vogais ---

def contar_vogais_comissao_v1(s):
    # DEFEITO (comissao): conta consoantes em vez de vogais (criterio invertido por completo)
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in s:
        if char.isalpha() and char not in vogais:
            contador += 1
    return contador


def contar_vogais_comissao_v2(s):
    # DEFEITO (comissao): retorna a lista das vogais encontradas em vez da contagem
    vogais = 'aeiouAEIOU'
    encontradas = []
    for char in s:
        if char in vogais:
            encontradas.append(char)
    return encontradas


def contar_vogais_comissao_v3(s):
    # DEFEITO (comissao): conta o total de caracteres da string, nao apenas as vogais
    contador = 0
    for char in s:
        contador += 1
    return contador


def contar_vogais_comissao_v4(s):
    # DEFEITO (comissao): conta apenas vogais minusculas, tratando isso como a especificacao completa
    vogais = 'aeiou'
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


def contar_vogais_comissao_v5(s):
    # DEFEITO (comissao): conta quantas vogais DISTINTAS aparecem, em vez do total de ocorrencias
    vogais = 'aeiouAEIOU'
    encontradas = set()
    for char in s:
        if char in vogais:
            encontradas.add(char.lower())
    return len(encontradas)


def contar_vogais_comissao_v6(s):
    # DEFEITO (comissao): conta o numero de palavras da string em vez do numero de vogais
    return len(s.split())
