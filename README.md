# obsidian-rag

Creating a local RAG agent to QA with my obsidian vault. Initial thoughts are to us LlamaIndex for handling (creating/retrieving/indexing) vector embeddings of the vault, using LangChain to handle creation of prompts, then run a local open-source model (hugging face) to query.

Will likely build out a separate service for handling the data. I use obsidian vault backed up with Git - so can easily time a cron job on a separate container to pull the data, then update embeddings (data streaming pipeline)

NOTE: this breaks when there are any empty notes within the vault. Can easily prune this by removing any notes of size 0 kb, but haven't automated yet.

## Steps

1. Use llama-index obsidian reader to create vector embeddings from vault
2. Use a local vector DB to store embeddings
3. Query the DB using openai api
