import logging
import sys
import os

from llama_index.readers.obsidian import ObsidianReader
from llama_index.core import VectorStoreIndex
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

dir_path = Path('/mnt/c/Users/pegui/Documents/Obsidian-Vault')

documents = ObsidianReader(
    dir_path
).load_data()


index = VectorStoreIndex.from_documents(
    documents
) # initialize index

# # set Logging to DEBUG for more detailed outputs
# query_engine = index.as_query_engine()
# res = query_engine.query("What is the 4th amendment")

# print(res.response)