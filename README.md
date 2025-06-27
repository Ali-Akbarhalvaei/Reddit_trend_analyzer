# InstAgent v0.2: Reddit Trend Analyzer

This repository contains a functional prototype of InstAgent, a Python-based tool designed to identify and analyze internet trends. This version uses Reddit as a data source and a Large Language Model (LLM) for analysis.

The agent performs a complete, automated workflow:

1.  **Trend Discovery:** It connects to the Reddit API to fetch the current top trending posts from the `r/popular` subreddit.
2.  **Virality Analysis:** It uses the Google Gemini API to analyze the title of each trend and generate a structured JSON output containing a "virality score," an explanation, and relevant hashtags.
3.  **Report Generation:** It orchestrates this workflow for multiple trends and saves the consolidated findings into a single, timestamped JSON report file.

This project serves as the foundational prototype for a more advanced AI-powered content creation assistant.

## Technology Stack

* **Language:** Python 3.9+
* **Core Libraries:**
    * `requests` (for fetching Reddit data)
    * `google-generativeai` (for LLM analysis)
    * `python-dotenv` (for managing API keys)
    * `tenacity` (for resilient API requests)

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/instagram-agent.git](https://github.com/your-username/instagram-agent.git)
    cd instagram-agent
    ```
2.  **Set up the environment:**
    Create a Python virtual environment and install the required dependencies.
3.  **Configure API Keys:**
    Create a `.env` file in the root directory and add your `GOOGLE_API_KEY`, or set it as a system environment variable.
4.  **Run the agent:**
    ```bash
    python main.py
    ```
5.  Check the root folder for your `trend_report_[timestamp].json` file.

## Current Status

* The project is a complete, functional application.
* The Reddit fetching module (`reddit_trends.py`) is functional.
* The LLM analysis module (`llm.py`) is functional and includes robust error handling.
* The main orchestrator script (`main.py`) successfully connects these modules and generates a final report.
