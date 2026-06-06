from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

# Pydantic Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt (FIXED)
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert movie information extractor.

Extract structured movie data from the paragraph.

{format_instructions}
"""),
    ("human", "{paragraph}")
])

# Input
paragraph = input("Give your paragraph: ")

# Format prompt
final_prompt = prompt.invoke({
    "paragraph": paragraph,
    "format_instructions": parser.get_format_instructions()
})

# LLM call
response = model.invoke(final_prompt)

# Parse output into Pydantic object
movie: Movie = parser.parse(response.content)

# Print structured result
print(movie)
print(movie.model_dump())