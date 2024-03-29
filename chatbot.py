import openai
import os

def send_message(message, history):
    history.append({
        "role": "user",
        "content": message
    })

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history
    )

    return response['choices'][0]['message']['content']

def main():
    # Aqui verificamos se a variável de ambiente OPENAI_API_KEY está definida
    # Se não estiver, o programa termina com uma mensagem de erro
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        return

    # Configuramos a chave da API OpenAI
    openai.api_key = api_key

    # Inicializamos o histórico de conversa
    history = [
        {
            "role": "system",
            "content": "Hello! I'm a chatbot. How can I help you today?"
        }
    ]

    while True:
        try:
            message = input("You: ")
        except EOFError:
            break
        response = send_message(message, history)
        print(f"Bot: {response}")
        history.append({
            "role": "system",
            "content": response
        })

if __name__ == "__main__":
    main()
