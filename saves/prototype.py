import random as rnd

def greetings(): 
    return [
    "Eae mano, qual a boa?",
    "Coé pae, quanto tempo!",
    "Yurrrr",
    "Manda as ideia ai pae",
    "Eae doido",
    "Bom dia mano, como vai?",
    "Salvee!",
    "Yo yo!",
    "Eai, tranquilo?",
    "Olá, tudo certo?",
    "Boa noite mano",
    "Boa tarde cria"
]

def palavras_chaves_usuario():
    user_response_greetings = ["eae","salve","salvee","bom dia","boa tarde","boa noite","oiee","oi","olá","ola","eai", "tudo bem?"]
    user_smalltalk = ["","","","","","","","","","","","","","",]
    user_end = ["sair","tchau","flw","flww","até mais","ate mais","Sair", "Tchau", "Flw", "Flww", "Até mais", "Ate mais", 
           "ate", "até", "adeus", "bye", "bye bye", "falou", "falou falou", "falou falou!", "exit", "end",]
    return  user_response_greetings, user_smalltalk, user_end

def resposta_chatbot():
    chatbot_response_greetings = ["Eu to bem mano e ocê?","Tudo na paz aqui, como que vai?","Como ta a vida?","Qual seu nome?","Quantos anos você tem?","O que você quer pae?"]
    chatbot_smalltalk = ["Isso parece interessante, me conte mais!","Hmmmmm, sinistro isso ai ein!","Tem que ver isso ai","Fala mais sobre isso","Continue me contando","Continue falando, acho que estou compreendendo!","Que bom! Me conte mais",]
    chatbot_end = ["Blzz entãoo, falou!",
           "A gente se ve por aí!",
           "Depois nois se fala",
           "Vlw pae, até",
           "Boa sorte ai mano",
           "Até um outro dia",
           "Falou falou!"
           ]
    return chatbot_response_greetings, chatbot_smalltalk, chatbot_end

def chatbot(): #isso traz as lista de palavras e frases das funçoes 
    user_response_greetings, user_smalltalk, user_end = palavras_chaves_usuario()
    chatbot_response_greetings, chatbot_smalltalk, chatbot_end = resposta_chatbot()

    print("Chatbot:", rnd.choice(greetings()))

    while True: # Loop principal do chat
        user_input = input("Você: ").lower() # Pega o input do usuário e converte para minúsculas

        # Verifica se o usuário quer sair
        if any(keyword in user_input for keyword in user_end):
            print("ChatBot:", rnd.choice(chatbot_end))
            break # Sai do loop e encerra o chat

        # Verifica se o input do usuário contém uma saudação
        elif any(keyword in user_input for keyword in user_response_greetings):
            print("ChatBot:", rnd.choice(chatbot_response_greetings))
        
        elif any(keyword in user_input for keyword in user_smalltalk):
            print("ChatBot: ", rnd.choice(chatbot_smalltalk))
            # Aqui você pode adicionar mais lógica para smalltalk ou outros tópicos
chatbot()