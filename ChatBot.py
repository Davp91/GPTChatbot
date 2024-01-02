import openai
import gradio

openai.api_key = "sk-"

messages = [{"role": "system", "content": "Du er en Chatbot for Vestland Fylkeskommune som skal hjelpe folk til å finne frem på siden sin, du svarer på Nynorsk"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Vestland Fylkeskommune Chatbot Ask")

demo.launch(share=True)
