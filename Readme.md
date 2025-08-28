SEO Assistant — Quick Start (Step-by-Step)

Boost Your SEO Strategy with an AI-Powered Assistant: Real-Time Insights, Smart Memory, and Groq AI Expertise

Follow these simple steps to get the project running locally.

1. Prerequisites

Python 3.10+ installed

Git (optional)

Groq API key and Tavily API key

2. Clone the repo
git clone https://github.com/your-username/seo-assistant.git
cd seo-assistant


(Or just create a new folder and copy the project files into it.)

3. Install dependencies

If you have requirements.txt:

pip install -r requirements.txt


Or install minimal packages directly:

pip install gradio python-dotenv llama-index

4. Create a .env file

Create a file named .env in the project root and add your keys:

GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

5. Run the app
python app.py


Open the local Gradio URL printed in your terminal (e.g., http://127.0.0.1:7860) and start chatting.

6. How to use

Type SEO questions (e.g., keyword ideas, trends, on-page tips).

Toggle Use Tavily live search in the UI to include real search results.

Use Clear Chat to clear visible chat history (memory persists unless you reset it).

Project files (short)

app.py — main app and chat logic

requirements.txt — dependency list

.env.example — example environment file

README.md — full project documentation

Example

User: What are the latest SEO trends for 2025?
Assistant: Based on recent search results and analysis, trending SEO strategies include AI-driven content, voice-search optimization, and improving Core Web Vitals.