import os
import gradio as gr
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama3-8b-8192",  # Change to other Groq-supported models if needed
)

# Tavily Search Tool
search = TavilySearchResults(tavily_api_key=tavily_api_key)

# Prompt with memory placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an SEO assistant that uses the latest Google trends (2025) "
               "and live search to generate accurate SEO insights."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Add memory
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# Chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# Gradio function
def seo_chat(query):
    # Optionally enrich query with Tavily search
    try:
        search_results = search.run(query)
    except Exception:
        search_results = "⚠️ Tavily search failed, continuing with LLM only."

    full_query = f"{query}\n\nUse these latest trends & news for context:\n{search_results}"
    response = chain.run(input=full_query)
    return response

# Gradio GUI
with gr.Blocks() as demo:
    gr.Markdown("# 🔎 Conversational SEO Assistant (Groq + Tavily + Memory)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask me about SEO, trends, or strategies...")
    clear = gr.Button("Clear Chat")

    def respond(user_message, chat_history):
        bot_message = seo_chat(user_message)
        chat_history.append((user_message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
