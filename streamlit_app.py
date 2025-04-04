import streamlit as st
import streamlit.components.v1 as components
# App title
st.set_page_config(page_title="🦙💬 kRISHA KA Chatbot")
meta_tags = """
<head>
    <meta property="og:title" content="PaperRound: AI News Curator">
    <meta property="og:description" content="Stay updated with AI-powered news summarization. Get concise, comprehensive, and smart news with PaperRound.io.">
    <meta property="og:image" content="https://mygenfile25.s3.ap-south-1.amazonaws.com/Leonardo_Phoenix_A_small_child_with_blue_skin_representing_Lor_0.jpg">
    <meta property="og:url" content="https://your-streamlit-app-url.streamlit.app/">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="PaperRound: AI News Curator">
    <meta name="twitter:description" content="AI-powered news summarization. Get concise, comprehensive news updates.">
    <meta name="twitter:image" content="https://mygenfile25.s3.ap-south-1.amazonaws.com/Leonardo_Phoenix_A_small_child_with_blue_skin_representing_Lor_0.jpg">
</head>
"""

# Inject into Streamlit
components.html(meta_tags, height=0)

st.title("🎈 My new app- krisha")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
