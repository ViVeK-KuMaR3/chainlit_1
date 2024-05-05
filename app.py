import os
from typing import List

from dotenv import load_dotenv

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import (
    ConversationalRetrievalChain,
)
from langchain.chat_models import ChatOpenAI

from langchain.docstore.document import Document
from langchain.memory import ChatMessageHistory, ConversationBufferMemory

import chainlit as cl

print("all_ok")




load_dotenv()

OPEN_API_KEY=os.getenv('OPEN_API_KEY')

os.environ['OPENAI_API_KEY']=OPEN_API_KEY
