import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

# ----------------------------
# Model
# ----------------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

# ----------------------------
# Pydantic Schema
# ----------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# ----------------------------
# Prompt
# ----------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert movie information extractor.

Extract structured movie data from the paragraph.

{format_instructions}
"""),
    ("human", "{paragraph}")
])

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🎬 Movie Info Extractor (AI Powered)")

paragraph = st.text_area("Enter movie paragraph:")

if st.button("Extract Movie Info"):
    if paragraph.strip():

        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)

        # Parse output
        movie: Movie = parser.parse(response.content)

        st.subheader("📌 Structured Output")

        st.json(movie.model_dump())

        st.subheader("🎞️ Movie Details")

        st.write("**Title:**", movie.title)
        st.write("**Year:**", movie.release_year)
        st.write("**Genre:**", movie.genre)
        st.write("**Director:**", movie.director)
        st.write("**Cast:**", movie.cast)
        st.write("**Rating:**", movie.rating)
        st.write("**Summary:**", movie.summary)

    else:
        st.warning("Please enter a paragraph.")