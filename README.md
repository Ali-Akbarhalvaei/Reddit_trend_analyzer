InstAgent v0.1: Reddit Trend Analyzer
This repository contains the initial version of InstAgent, a Python-based tool designed to identify and analyze internet trends. This version focuses on using Reddit as a data source and a Large Language Model (LLM) for analysis.

The agent performs two primary functions:

Trend Discovery: It connects to the Reddit API to fetch the current top trending posts from the r/popular subreddit.

Virality Analysis: It uses the Google Gemini API to analyze the title of each trend and generate a structured JSON output containing:

A "virality score" from 0 to 10.

A brief explanation for the score.

A list of suggested hashtags.

This project serves as the foundational prototype for a more advanced AI-powered content creation assistant.

Technology Stack
Language: Python 3.9+

Core Libraries:

requests (for fetching Reddit data)

google-generativeai (for LLM analysis)

python-dotenv (for managing API keys)

tenacity (for resilient API requests)

Current Status
The Reddit fetching module (reddit_trends.py) is functional.

The LLM analysis module (llm.py) is functional and includes robust error handling and API retry logic.
