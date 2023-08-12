def escrever(x):
    with open("chat.txt", "w") as f:
        f.write(x)

def pergunta_resposta(pergunta, resposta):
    arquivo='bot.txt'
    with open(arquivo, 'a', encoding='utf-8') as f:
        f.write(f"{pergunta}={resposta}\n")