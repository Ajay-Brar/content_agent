# Content Agent (AI Repurposing Tool)

An AI-powered automation tool designed to take long-form content (like blog posts) and repurpose it into engaging social media content. It uses **LangChain**, **BeautifulSoup**, and the **Groq API** (Llama 3 model) to generate professional LinkedIn posts, Twitter/X threads, and key summary insights.

## Features

* **Content Extraction:** Automatically scrapes and extracts text from a given URL using `WebBaseLoader`.
* **AI-Powered Repurposing:** Leverages the Groq Llama 3 model to understand context and generate high-quality text.
* **Multi-Platform Output:** Generates three distinct formats in one go:
    * **LinkedIn Post:** Professional tone with hashtags.
    * **Tweet Thread:** A sequence of 3 tweets with hooks and emojis.
    * **Key Insights:** A bulleted summary of takeaways.
* **Fast Inference:** Uses Groq's high-speed API for near-instant results.

## Prerequisites

* Python 3.x
* A **Groq API Key** (You can get one from the [Groq Console](https://console.groq.com/)).

## Installation

1.  **Clone the repository** (or download the source files).

2.  **Install Dependencies**
    You can install the strict dependencies using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    
    Alternatively, you can install the core packages manually:
    ```bash
    pip install langchain langchain-groq langchain-community langchain-text-splitters beautifulsoup4
    ```

## Configuration

Before running the script, you must add your API key.

1.  Open `agent_groq.py` in your text editor.
2.  Locate **Step 1** (around line 9) and paste your Groq API key:
    ```python
    os.environ["GROQ_API_KEY"] = "YOUR_ACTUAL_API_KEY_HERE"
    ```

## Usage

1.  **Set the Target URL**
    By default, the script fetches a specific article about AI Agents. To change this, modify the `blog_url` variable in the `main()` function (around line 63) of `agent_groq.py`:
    ```python
    blog_url = "[https://your-target-url.com/blog-post](https://your-target-url.com/blog-post)"
    ```

2.  **Run the Agent**
    Execute the script from your terminal:
    ```bash
    python agent_groq.py
    ```

3.  **View Results**
    The script will print the repurposed content directly to your terminal console under the header `--- 🚀 YOUR REPURPOSED CONTENT ---`.

## Project Structure

* **`agent_groq.py`**: The main script containing the logic for loading content, initializing the LLM, and running the repurposing chain.
* **`requirements.txt`**: A list of all python dependencies required to run the project.

## Disclaimer
This tool uses web scraping to extract content. Ensure you have the right to process the content you are targeting and use the API responsibly.
