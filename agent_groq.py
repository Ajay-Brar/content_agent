import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

# --- STEP 1: SET YOUR API KEYS ---
os.environ["GROQ_API_KEY"] = "  Put Your API KEY HERE"
os.environ["USER_AGENT"] = "MyContentAgent"


# --- STEP 2: EXTRACT CONTENT FROM URL ---
def extract_content(url):
    """Loads and extracts the main text content from a blog URL."""
    print(f"Loading content from: {url}...")
    try:
        loader = WebBaseLoader(url)
        data = loader.load()
        if data:
            print("Content loaded successfully.")
            return data[0].page_content
        else:
            print("No data found at URL.")
            return None
    except Exception as e:
        print(f"Error loading content: {e}")
        return None

# --- STEP 3: SPLIT TEXT (IF NEEDED) ---
def split_text(long_text, chunk_size=4000):
    """Splits long text into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(long_text)
    return chunks

# --- STEP 4: DEFINE YOUR "BRAIN" (THE GROQ/LLAMA 3 LLM) ---
def get_llm():
    """Initializes and returns the Groq Llama 3 model."""
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  
        temperature=0.7
    )
    return llm

# --- STEP 5: CREATE THE "AGENT" LOGIC WITH A PROMPT (MODERN WAY) ---
def get_repurposing_chain(llm):
    """Creates the LangChain chain with our prompt."""
    
    prompt_template = """
    You are an expert content repurposing AI. You are given a piece of text from a blog post.

    Your task is to generate the following three items based on the content:
    
    1.  **LinkedIn Post:** A professional post (under 250 words) that shares the main idea and ends with an engaging question. Include 3 relevant hashtags.
    2.  **Tweet Thread:** A 3-tweet thread to share the content. Add a strong hook to the first tweet. Use emojis and hashtags.
    3.  **Key Insights:** A 5-bullet-point summary of the key takeaways.

    Here is the content:
    "{text}"
    
    YOUR RESPONSE (in markdown):
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    
    # This is the new "LCEL" way. It replaces LLMChain.
    repurposing_chain = prompt | llm | StrOutputParser()
    
    return repurposing_chain

# --- STEP 6: RUN YOUR AGENT! ---
def main():
    blog_url = "https://lilianweng.github.io/posts/2023-06-23-agent/" 
    
    # 1. Extract content
    content = extract_content(blog_url)
    
    if not content:
        print("Failed to extract content. Exiting.")
        return

    # 2. Split
    content_chunk = content[:6000]
    print(f"Using first {len(content_chunk)} characters of content.")

    # 3. Initialize LLM and Chain
    llm = get_llm()
    repurposing_chain = get_repurposing_chain(llm)

    # 4. Repurpose
    print("Repurposing content with Groq/Llama 3... (this will be fast!)")
    try:
        # The .invoke call is the same
        response = repurposing_chain.invoke({"text": content_chunk})
        
        # 5. Print the result (Simpler, response is now just a string)
        print("\n--- 🚀 YOUR REPURPOSED CONTENT ---")
        print(response) # <-- CHANGED: No more ['text']
        
    except Exception as e:
        print(f"An error occurred while invoking the chain: {e}")

if __name__ == "__main__":
    main()