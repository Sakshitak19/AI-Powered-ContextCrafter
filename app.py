import streamlit as st
from ollama_utils import generate_response
from news_utils import extract_text_from_links
from content_utils import generate_content

# 🔧 Page configuration
st.set_page_config(page_title="AI-Powered ContextCrafter", layout="wide")
st.title("🧠 AI-Powered ContextCrafter")

# 🚀 Sidebar mode selector
mode = st.sidebar.selectbox("Choose Mode", ["News Q&A", "Content Generator"])

# 📰 Mode 1: News Question Answering
if mode == "News Q&A":
    st.subheader("🔎 Ask Questions from News Articles")
    links = st.text_area("Paste 1–3 news article URLs (each on a new line):")
    ask = st.text_input("Ask your question about the above news:")

    if st.button("Ask"):
        if not links.strip() or not ask.strip():
            st.warning("⚠️ Please provide both links and a question.")
        else:
            with st.spinner("Extracting content and generating answer..."):
                texts = extract_text_from_links(links.splitlines())
                full_context = "\n\n".join(texts)
                prompt = f"Answer the question based on the news:\n\n{full_context}\n\nQuestion: {ask}"
                answer = generate_response(prompt)
                st.success("✅ Answer:")
                st.write(answer)

# ✍️ Mode 2: Content Generator
elif mode == "Content Generator":
    st.subheader("📝 Generate Content from Topic")
    topic = st.text_input("Enter topic (e.g. climate change, AI in education):")
    style = st.selectbox("Choose content style", ["Blog", "Essay", "Informative Article"])

    if st.button("Generate"):
        if not topic.strip():
            st.warning("⚠️ Please enter a topic.")
        else:
            with st.spinner("Crafting your content..."):
                prompt = f"Write a {style.lower()} about: {topic}"
                content = generate_content(prompt)
                st.success(f"✅ {style} on: {topic}")
                st.markdown(content)
