# TextToSQL - SQL Database Q/A App

This project is a Streamlit application that allows users to query a SQL database using natural language. The application leverages powerful language models, including Google Gemini and ChatGPT-4o, to interpret user queries and retrieve relevant data from the database.

## Features

- **Model Selection**: Choose between Google Gemini and ChatGPT-4o for query processing.
- **Dynamic Querying**: Input your SQL-related questions, and the app will translate them into SQL queries, execute them, and display the results.
- **User-Friendly Interface**: The app provides a simple and intuitive interface for querying the database.

## Setup

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Required Python packages (see below)
- A SQL database (e.g., MySQL) with appropriate credentials

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required Python packages**:

   You can install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory of the project and add your API keys and database credentials:

   ```
   DB_USER=<your-database-username>
   DB_PASSWORD=<your-database-password>
   DB_HOST=<your-database-host>
   DB_NAME=<your-database-name>
   ```

   Ensure you have valid API keys for the language models you intend to use.

### Running the App

1. **Start the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the app**:

   - Use the sidebar to select a language model (Google Gemini or ChatGPT-4o).
   - Enter your natural language question related to the SQL database.
   - Click "Submit" to see the results.

## File Structure

- `app.py`: The main file for the Streamlit application, containing the UI components and query processing logic.
- `utils.py`: A utility module that handles the interaction with the SQL database and language models.
- `.env`: Contains sensitive information such as API keys and database credentials (not included in the repository).
- `requirements.txt`: Lists the required Python packages for the project.

## Usage

This application is designed for users who need to interact with SQL databases but prefer using natural language instead of writing SQL queries directly. The app is suitable for both technical and non-technical users.

### Example

To ask a question like "How many clients are there in the database?":

1. Enter the question in the text input field.
2. Select a model (e.g., Google Gemini).
3. Click "Submit".
4. The app will process the query and return the number of clients from the database.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain**: For providing the framework to integrate with various language models.
- **Streamlit**: For the easy-to-use web application framework.
