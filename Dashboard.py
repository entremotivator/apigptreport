import streamlit as st
import pandas as pd
import plotly


# Setup data
df = pd.read_csv("iris.data",
                 header=None,
                 names=["Sepal Length", "Sepal Width",
                        "Petal Length", "Petal Width", "Species"])


# Make page
st.title("🚀 GPT Report Card 📊")

  st.markdown("### TruLens Dashboard\n\n🔍 Track Language Models (LLM) and agents with detailed metrics and self-improvement skills.\n\n"
                "✨ **Key Features:**\n"
                "1. Real-time performance metrics 📈\n"
                "2. Personalized improvement suggestions 🌟\n"
                "3. Historical analysis for continuous learning 🔄\n"
                "4. User-friendly interface for easy navigation 🖥️")
st.image("img.png")
