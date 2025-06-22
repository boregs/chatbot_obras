import pandas as pd
import django as django
import random as rnd

mensagem_intro_primeira_vez = "Olá, sou o ObrasBot, um assistente virtual para ajudar você a encontrar informações sobre as obras e suas pendencias. Como posso ajudar hoje?"
mensagem_intro_retorno = ["Olá novamente! Vejo que precisa do meu serviço de novo!. Como posso ajudar hoje?", "Opa opa!, Precisa dos meus serviços de novo? Estou aqui para ajudar! Do que você precisa?"]

#codigo para gerar uma mesnagem do zap com botões de opções
def gerar_resposta_chatbot(pergunta):
    pergunta = pergunta.lower()

    if "menu" in pergunta or "opções" in pergunta:
        # Sinaliza que uma mensagem com botões deve ser enviada
        return {
            "type": "quick_reply",
            "text": (mensagem_intro_primeira_vez),
            "buttons": [
                {"title": "Serviços", "payload": "servicos"},
                {"title": "Suporte", "payload": "suporte"},
                {"title": "Falar com Atendente", "payload": "atendente"}
            ]
        }
    elif "servicos" in pergunta:
        return "Oferecemos desenvolvimento web, consultoria de IA e automação."
    elif "suporte" in pergunta:
        return "Por favor, descreva seu problema e entraremos em contato."
    elif "atendente" in pergunta:
        return "Certo! Por favor, aguarde enquanto conecto você a um de nossos atendentes."
    elif "olá" in pergunta or "oi" in pergunta:
        return "Olá! Como vai você?"
    elif "como você está" in pergunta:
        return "Eu sou um programa, então não tenho sentimentos, mas obrigado por perguntar!"
    elif "seu nome" in pergunta:
        return "Meu nome é Chatbot Simples."
    elif "ajuda" in pergunta:
        return "Posso te ajudar com perguntas básicas ou apenas conversar. Que tal digitar 'menu'?"
    else:
        return "Desculpe, não entendi. Você pode reformular ou perguntar algo diferente?"

gerar_resposta_chatbot("menu")