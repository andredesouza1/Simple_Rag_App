# Used for testing code and ideas

student_info = """
Alexandra Thompson, a 19-year-old computer science sophomore with a 3.7 GPA,
is a member of the programming and chess clubs who enjoys pizza, swimming, and hiking
in her free time in hopes of working at a tech company after graduating from the University of Washington.
"""

club_info = """
The university chess club provides an outlet for students to come together and enjoy playing
the classic strategy game of chess. Members of all skill levels are welcome, from beginners learning
the rules to experienced tournament players. The club typically meets a few times per week to play casual games,
participate in tournaments, analyze famous chess matches, and improve members' skills.
"""

university_info = """
The University of Washington, founded in 1861 in Seattle, is a public research university
with over 45,000 students across three campuses in Seattle, Tacoma, and Bothell.
As the flagship institution of the six public universities in Washington state,
UW encompasses over 500 buildings and 20 million square feet of space,
including one of the largest library systems in the world.

"""


import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os
import uuid

load_dotenv()


default_ef = embedding_functions.DefaultEmbeddingFunction()




client = chromadb.PersistentClient(path="/vector_databases/test")
# client.reset()

collection = client.get_or_create_collection("test_collection", embedding_function=default_ef)
# collection.add(
#     documents = [student_info, club_info, university_info],
#     metadatas = [{"source": "student info"},{"source": "student info"},{'source':'university info'}],
#     ids = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
# )




print(collection.get(include=["metadatas"]))

print(collection.count())

collection.delete(where={"source": "student info"})

print(collection.get(include=["metadatas"]))

import datetime
current_date = datetime.datetime.now().date()
print(current_date)

print(client.list_collections())

result = client.list_collections()

print(result[0].name)