import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def calcular_frecuencias(texto):
    return dict(Counter(texto))


def construir_arbol(frecuencias):
    heap = [Node(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        nuevo = Node(None, nodo1.freq + nodo2.freq)
        nuevo.left = nodo1
        nuevo.right = nodo2
        heapq.heappush(heap, nuevo)

    return heap[0]  


def generar_codigos(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return
    if nodo.char is not None:
        codigos[nodo.char] = codigo_actual
    generar_codigos(nodo.left, codigo_actual + "0", codigos)
    generar_codigos(nodo.right, codigo_actual + "1", codigos)
    return codigos


def codificar_texto(texto, codigos):
    return "".join(codigos[char] for char in texto)


def decodificar_texto(codificado, raiz):
    resultado = ""
    nodo = raiz
    for bit in codificado:
        nodo = nodo.left if bit == "0" else nodo.right
        if nodo.char is not None:
            resultado += nodo.char
            nodo = raiz
    return resultado


def calcular_eficiencia(original, codificado):
    original_bits = len(original) * 8  
    comprimido_bits = len(codificado)
    if original_bits == 0:
        return 0
    return (1 - (comprimido_bits / original_bits)) * 100

