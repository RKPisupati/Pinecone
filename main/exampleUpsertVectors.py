import time
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone( api_key="YOUR-API-KEY" )

index = pc.Index("my-index")

index.upsert(
  vectors=[
    {"id": "A", "metadata": {"buoyStation": 45609}, "values": [0.1, 0.1, 0.1 ]},
    {"id": "B", "metadata": {"buoyStation": 45609}, "values": [0.3, 0.1, 0.1 ]},
    {"id": "C", "metadata": {"buoyStation": 45609}, "values": [0.5, 0.1, 0.1 ]},
    {"id": "D", "metadata": {"buoyStation": 45402}, "values": [0.7, 0.1, 0.1 ]},
    {"id": "E", "metadata": {"buoyStation": 45402}, "values": [0.9, 0.1, 0.1 ]}
  ]
)

time.sleep(5)

results = index.fetch(["A", "B", "C", "D", "E"])

print( results )