def leia():
    with open("chat.txt", "r") as f:
        return f.read()

def buscar_resposta(pergunta):
    arquivo='bot.txt'
    respostas = {}
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                perg= linha.strip().split("=")[0]
                resp= linha.strip().split("=")[1]
                respostas[perg] = resp
    except FileNotFoundError:
        pass
    return respostas.get(pergunta, 'Não entendi sua questão')