Core LangChain Packages
1. langchain

Main framework for building AI applications.

It helps you:

connect LLMs
create chatbots
build RAG systems
use memory
create AI agents
chain prompts together

Example:

from langchain.prompts import PromptTemplate

Think of it as the main AI framework.

2. langchain-core

Contains the core building blocks of LangChain.

Includes:

prompts
messages
output parsers
runnable chains
base interfaces

Usually installed automatically, but included explicitly for compatibility.

Example:

from langchain_core.messages import HumanMessage
3. langchain-community

Contains integrations contributed by the community.

Used for:

vector databases
document loaders
tools
embeddings
third-party integrations

Example:

from langchain_community.document_loaders import TextLoader

Useful for advanced projects like RAG.

Groq Packages
4. langchain-groq

LangChain integration for Groq models.

Lets you use Groq models easily inside LangChain.

Example:

from langchain_groq import ChatGroq

Without this package, LangChain cannot directly communicate with Groq.

5. groq

Official Python SDK from Groq.

Used when calling Groq APIs directly without LangChain.

Example:

from groq import Groq
Google Gemini Packages
6. langchain-google-genai

LangChain integration for Google Gemini.

Allows LangChain to use Gemini models.

Example:

from langchain_google_genai import ChatGoogleGenerativeAI
7. google-generativeai

Official Gemini SDK from Google.

Used for direct Gemini API calls.

Example:

import google.generativeai as genai
Mistral Packages
8. langchain-mistralai

LangChain integration for Mistral AI.

Lets LangChain work with Mistral models.

Example:

from langchain_mistralai import ChatMistralAI
9. mistralai

Official SDK for Mistral AI.

Used for direct API access.

Example:

from mistralai import Mistral
Utility Packages
10. python-dotenv

Loads environment variables from .env.

Without it:

load_dotenv()

your API keys won't automatically load.

Example .env:

GROQ_API_KEY=xxxx
11. pydantic

Used for:

data validation
structured outputs
schema definitions

Very important in:

FastAPI
LangChain
AI agents

Example:

from pydantic import BaseModel
12. tiktoken

Tokenizer library from OpenAI.

Used to:

count tokens
estimate API cost
split text correctly

Example:

import tiktoken

Very important for:

RAG
chunking
prompt optimization