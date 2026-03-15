def consultar_status_pedido(pedido_id: int):
    pedidos = {
        1029: "Em separação",
        2040: "Enviado",
        3001: "Entregue"
    }
    return pedidos.get(pedido_id, "Pedido não encontrado")

def gerar_boleto(email: str):
    return f"Boleto gerado e enviado para {email}"

def agendar_consulta(data: str, hora: str):
    return f"Consulta agendada para {data} às {hora}"

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def divisao(a,b):
    return a / b

def celsius_para_fahrenheit(a):
    return (a*1.8) + 32

def fahrenheit_para_celsius(a):
    return (a-32) / 1.8

def buscar_produto(nome_produto: str):
    produtos = {
        "placa de video": 4500,
        "memória ram": 2800,
        "controle": 300
    }

    preco = produtos.get(nome_produto.lower())

    if preco is not None:
        return preco
    
    return "Produto não encontrado"

def verificar_estoque(nome_produto: str):
    estoque = {
        "placa de video":15,
        "memória ram":10,
        "controle":50
    }

    quantidade = estoque.get(nome_produto.lower())

    if quantidade is not None:
        return f"Temos {quantidade} unidade(s) de {nome_produto} em estoque"
    return "produto não encontrado"

eventos = []

def criar_evento(titulo: str, data: str):
    eventos.append(f"{titulo} - {data}")
    return f"Evento '{titulo}' criado para {data}"

def listar_eventos():
    if not eventos:
        return "Nenhum evento cadastrado."
    return "\n".join(eventos)

def buscar_clima(cidade: str):
    clima = {
    "sao paulo": "19°C e ensolarado",
    "bauru": "28°C e nublado",
    "belem": "38°C e ensolarado"
}
    resultado = clima.get(cidade.lower())

    if resultado is not None:
        return f"O clima em {cidade} está {resultado}"
    return "Cidade não encontrada"