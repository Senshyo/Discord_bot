def get_response(user_message):
    msg = user_message.lower()

    if msg == "":
        return "Você é bem queito x-x"
    elif "oi" in msg:
        return "olá"
    elif "como você está?" in msg or "como voce esta?" in msg:
        return "Estou bem, obrigado por perguntar!"
    elif "python" in msg:
        return "Python é uma linguagem de programação poderosa e versátil!"
    elif "github" in msg:
        return "GitHub é uma plataforma popular para hospedagem de código-fonte e colaboração em projetos de software!"
    elif "adeus" in msg:
        return "Adeus!"
    elif "lukita" in msg:
        return "lurguita"
    else:
        return "Desculpe, não entendi. Poderia repetir de outra forma?"