import streamlit as st
from llm import Model
from image_engine import ImageGenerator
import io

# Instantiate the models
gemini_model = Model()
image_generator = ImageGenerator()

# Streamlit interface
st.title("AI Arist🎨")
art_idea = st.text_input("Enter your drawing idea:")

if st.button("Generate Art"):
    if art_idea:
        with st.spinner("Enhancing your idea..."):
            enhanced_idea = gemini_model.enhance_idea(art_idea)
            st.write("Enhanced Idea:", enhanced_idea)
        with st.spinner("Geneating an image..."):
            image = image_generator.generate_image(enhanced_idea)
            st.image(image, caption="Generated Art")
            
            # Add a download button for the generated image
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            st.download_button(
                label="Download",
                data=img_byte_arr,
                file_name="generated_art.png",
                mime="image/png"
            )
    else:
        st.error("Please enter an art idea!")