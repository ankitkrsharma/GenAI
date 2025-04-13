# context_retriever.py
class ContextRetriever:
    def __init__(self, data_source):
        """
        Initialize with a data source. Could be a list, database, or any other storage.
        """
        self.data_source = data_source  # e.g. list of documents

    def get_relevant_context(self, query, k=5):
        """
        Retrieve the most relevant documents based on a query.
        Here, you could use keyword search, semantic matching, etc.
        For simplicity, let's assume you are matching query with documents' titles.
        """
        relevant_docs = []
        for doc in self.data_source:
            # Simple keyword-based matching
            if query.lower() in doc["content"].lower():
                relevant_docs.append(doc)
            if len(relevant_docs) >= k:
                break
        return relevant_docs
