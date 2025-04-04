import streamlit as st
import streamlit.components.v1 as components

meta_tags = """
<head>
    <meta property="og:title" content="PaperRound: AI News Curator">
    <meta property="og:description" content="Stay updated with AI-powered news summarization. Get concise, comprehensive, and smart news with PaperRound.io.">
    <meta property="og:image" content="https://og-image.vercel.app/PaperRound.png">
    <meta property="og:url" content="https://your-streamlit-app-url.streamlit.app/">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="PaperRound: AI News Curator">
    <meta name="twitter:description" content="AI-powered news summarization. Get concise, comprehensive news updates.">
    <meta name="twitter:image" content="https://og-image.vercel.app/PaperRound.png">
</head>
"""

# Inject into Streamlit
components.html(meta_tags, height=0)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
