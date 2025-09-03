# Literature Review: Research Software Metadata

## Project Description

This is a Python script to automate the search and retrieval of academic articles for a literature review on the topic of **research software metadata**. It uses the Elsevier Scopus API to fetch relevant publications based on a customizable search query.

## What It Does

The script `scopus.py` performs the following tasks:
1.  Connects to the Scopus API using a secure API key.
2.  Executes a search for articles related to "research software metadata" (or your custom query).
3.  Retrieves key details for each article, including:
    *   Title
    *   Author(s)
    *   Journal/Publication Name
    *   Publication Date
    *   DOI (Digital Object Identifier)
4.  Prints a formatted list of the results to the console.

## Prerequisites

Before you can run this script, you need to have:

1.  **A Scopus API Key**: You must have a valid API key from Elsevier.
    *   **How to get it:** You typically need to have a subscription to Scopus through your university or institution. Visit the [Elsevier Developer Portal](https://dev.elsevier.com/) to register and obtain an API key.

2.  **Python 3.x**: Make sure Python is installed on your system.

3.  **Python `requests` library**: This is used to make the HTTP request to the API.
    *   Install it using pip: `pip install requests`

## Setup & Usage

### 1. Set Your API Key as an Environment Variable

For security, **do not hardcode your API key** into the script. Instead, set it as an environment variable.

**On macOS/Linux (Terminal):**
```bash
export SCOPUS_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
