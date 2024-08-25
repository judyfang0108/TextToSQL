from langchain.llms import GooglePalm
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.callbacks import get_openai_callback
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Wrapper for the embeddings
class MyEmbeddings(HuggingFaceEmbeddings):
    def __call__(self, input):
        return super().__call__(input)

def get_db_chain(model_choice):
    # Create connection with the database
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    # Set up the database connection
    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        #sample_rows_in_table_info=3,
    )
    print(db.table_info)

    if model_choice == "Google Gemini":
        # Set up the LLM with the Google Gemini model
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
    elif model_choice == "ChatGPT-4o":
        llm= ChatOpenAI(model_name="gpt-4o", temperature=0)
    
    # Create SQLDatabaseToolkit
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Create the SQL agent executor
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    
    return agent_executor

def execute_query(query, model_choice):
    # Get the SQL agent executor
    agent_executor = get_db_chain(model_choice)

    # Execute the query using the agent and log the callback
    with get_openai_callback() as cb:
        res = agent_executor.run(query)
        print("SQL Query Result:")
        print(res)
        print("")
        print(cb)
    return res


# # Example query
# query = "How many clients are there in the database?"
# execute_query(query)
