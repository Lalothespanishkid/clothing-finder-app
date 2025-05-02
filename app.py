
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse
import webbrowser

# Optional: Replace with your own OpenAI and Amazon API keys if needed
# openai.api_key = "YOUR_OPENAI_API_KEY"

# Placeholder for visual tagging (can integrate CLIP, BLIP or a pre-trained model)
def get_visual_tags(image):
    # For now, just use a placeholder tag
    return ["black crop top", "ribbed"]

# Perform a Google Search for Amazon links (can be replaced with Amazon PA API)
def search_amazon_with_tags(tags):
    query = "+".join(tags) + "+site:amazon.com"
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    return search_url

# Streamlit UI
st.title("🛍️ Clothing Finder from Image")
st.write("Upload an image of clothing and find similar items on Amazon.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Step 1: Tag the image
    with st.spinner('Analyzing image...'):
        tags = get_visual_tags(image)
    st.success(f"Detected Tags: {', '.join(tags)}")

    # Step 2: Search Amazon
    search_link = search_amazon_with_tags(tags)
    st.markdown(f"### [🔍 View Similar Clothing on Amazon]({search_link})")

    if st.button("Open in Browser"):
        webbrowser.open_new_tab(search_link)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
