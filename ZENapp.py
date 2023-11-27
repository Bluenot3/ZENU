import openai
import gradio as gr

# Replace the placeholder with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the function to interact with GPT-4
def gpt4_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  # Using the specific GPT-4 model
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# Create the Gradio interface
interface = gr.Interface(
    fn=gpt4_chat,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text",
    title="GPT-4 1106 Preview Chatbot",
    description="Interact with the GPT-4 1106 Preview model. Enter a prompt and receive a response."
)

# Launch the interface
interface.launch()
