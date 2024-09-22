import time
from pinecone import Pinecone

pc = Pinecone( api_key="YOUR-API-KEY" )

# Get python object reference to Index
index = pc.Index("my-index")

# Query the pinecone index passing a query vector
results = index.query(
    vector=[0.1, 0.11, 0.11],
    top_k=5,
    include_values=True,
    filter={
        "buoyStation": {"$eq": 45402}
    },
)

# Print the results from fetch operation
print( results )