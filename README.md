# LangChain Agent 

This project implements a Python-based LangChain agent that utilizes various tools to provide information based on natural language queries. The agent is exposed over a single FastAPI endpoint and can be interacted with using Postman.

## Features

- **Query Database**: Queries the Northwind database.
- **Search Internet**: Performs general internet searches.
- **Get Weather**: Retrieves weather information.
- **Get IP Info**: Obtains IP-related information.
- **Get Pokémon Info**: Fetches details about Pokémon.
- **Get Movie Info**: Retrieves movie information.

## Tools Integrated

1. **query_db**: Queries the Northwind database.
2. **search_internet**: Performs general internet searches.
3. **get_weather**: Retrieves weather information.
4. **get_ip_info**: Obtains IP-related information.
5. **get_pokemon_info**: Fetches details about Pokémon.
6. **get_movie_info**: Retrieves movie information.

## FastAPI Endpoint

The agent is exposed over a single FastAPI endpoint where you can input a natural language query using Postman. The agent automatically selects the appropriate tool based on the query and responds with accurate information.

### Endpoint

```
POST /query
```

### Request

**Body**:

```json
{
  "query": "Your natural language query here"
}
```

### Response

**Body**:

```json
{
  "response": "The agent's response based on your query"
}
```

## Setup and Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/Theedon/AfriChain.git
   cd AfriChain
   ```

2. **Install dependencies**:
   Ensure you have [Poetry](https://python-poetry.org/) installed.

   ```sh
   poetry install
   ```

3. **Set environment variables**:
   Create a `.env` file in the root of your project and add the necessary environment variables:

   ```env
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key
    HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_api_token
    HF_TOKEN=your_hf_token
    LANGCHAIN_API_KEY=your_langchain_api_key
    MISTRAL_API_KEY=your_mistral_api_key
    TOGETHER_API_KEY=your_together_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
    OMDB_API_KEY=your_omdb_api_key
    TMDB_API_KEY=your_tmdb_api_key
    TAVILY_API_KEY=your_tavily_api_key

   ```

4. **Run the application**:
   Use Poetry to run the FastAPI application with Uvicorn, enabling hot reloading.
   ```sh
   poetry run africhain
   ```

## Usage

You can interact with the agent using Postman. Send a POST request to `http://0.0.0.0:8000/query` with a JSON body containing your query.

## Deployment

The project is deployed on render as a service at [this url](https://africhain.onrender.com)
