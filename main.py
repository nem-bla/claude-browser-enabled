import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.anthropic import Claude

print("Loading assistant...")

st.title("Claude Sonneet 3.5 - The Assistant")
st.caption("Claude Sonneet 3.5 is a conversational assistant that can help you with a variety of tasks. You can ask Claude questions, get information, and even have a conversation with him. Claude is powered by the PHI library, which is a Python library for building conversational agents.")

anthropic_api_key = st.text_input("Enter your Anthropic API key", type="password")

if anthropic_api_key:
    assistant = Assistant(
    llm=Claude(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        temperature=0.9,
        api_key=anthropic_api_key, tools=[DuckDuckGo()]), show_tool_calls=True)
    

query = st.text_input("Ask Claude a question", type="default")

if query:
    response = assistant.run(query, stream=False)
    st.write(response)