"""
    ATENÇÃO – CÓDIGO EDUCACIONAL (NÃO UTILIZAR EM PRODUÇÃO)

    Este código foi desenvolvido exclusivamente para fins didáticos,
    no contexto da disciplina Tecnologias e Programação Integrada.

    O objetivo é demonstrar o uso de LLMs/SLMs com tool calling, permitindo
    que um modelo de linguagem decida qual função Python executar a
    partir de uma entrada em linguagem natural.

    IMPORTANTE:
    - Este código NÃO possui guardrails de segurança.
    - Não há validação robusta de entrada.
    - Não há controle de permissões ou autenticação.
    - Não há proteção contra uso indevido, chamadas indevidas ou escrita não autorizada.
    - NÃO deve ser executado em ambientes de produção.

    Antes de qualquer uso real, seria necessário implementar:
    - Validações de entrada
    - Controle de acesso
    - Limitação de escopo das tools
    - Logs, auditoria e monitoramento
    - Tratamento de erros e exceções
    - Políticas de segurança e compliance

    Autor: Prof. Victor

"""
import os
import json
from openai import OpenAI
from tools import consultar_status_pedido, gerar_boleto, agendar_consulta, somar, multiplicar, subtrair, divisao
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "consultar_status_pedido",
            "description": "Consulta o status de um pedido",
            "parameters": {
                "type": "object",
                "properties": {
                    "pedido_id": {
                        "type": "integer",
                        "description": "ID do pedido"
                    }
                },
                "required": ["pedido_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtrair",
            "description": "subtrair dois numeros",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "primeiro numero da subtração"
                    },
                    "b": {
                        "type": "integer",
                        "description": "segundo numero da subtração"
                    }
                },
                "required": ["a","b"]
            }
        }
    },
        {
        "type": "function",
        "function": {
            "name": "divisao",
            "description": "dividir dois numeros",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "primeiro numero da dividir"
                    },
                    "b": {
                        "type": "integer",
                        "description": "segundo numero da dividir"
                    }
                },
                "required": ["a","b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "somar dois numeros",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "primeiro numero da soma"
                    },
                    "b": {
                        "type": "integer",
                        "description": "segundo numero da soma"
                    }
                },
                "required": ["a","b"]
            }
        }
    },
      {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "multiplicação dois numeros",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "primeiro numero da multiplicação"
                    },
                    "b": {
                        "type": "integer",
                        "description": "segundo numero da multiplicação"
                    }
                },
                "required": ["a","b"]
            }
        }
    },
          {
        "type": "function",
        "function": {
            "name": "subtrair",
            "description": "subtrair dois numeros",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "primeiro numero da subtração"
                    },
                    "b": {
                        "type": "integer",
                        "description": "segundo numero da subtração"
                    }
                },
                "required": ["a","b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "gerar_boleto",
            "description": "Gera um boleto para o cliente",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "Email do cliente"
                    }
                },
                "required": ["email"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "agendar_consulta",
            "description": "Agenda uma consulta",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {"type": "string"},
                    "hora": {"type": "string"}
                },
                "required": ["data", "hora"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        if tool_name == "consultar_status_pedido":
            return consultar_status_pedido(**args)

        if tool_name == "gerar_boleto":
            return gerar_boleto(**args)

        if tool_name == "agendar_consulta":
            return agendar_consulta(**args)
        
        if tool_name == "somar":
            return somar(**args)
        
        if tool_name == "multiplicar":
            return multiplicar(**args)
        
        if tool_name == "subtrair":
            return subtrair(**args)
        
        if tool_name == "dividir":
            return divisao(**args)
        

    return message.content


print(perguntar("dividir 26 por 4"))