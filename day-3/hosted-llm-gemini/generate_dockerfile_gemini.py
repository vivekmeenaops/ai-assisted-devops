import google.generativeai as genai  # Fixed import
import os

# Set your API key here
os.environ["GOOGLE_API_KEY"] = "XXXXXXXXXXX"

# Configure the Gemini model
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use a supported model name. 
# 'gemini-1.5-pro' is the standard; use 'gemini-2.0-flash' for speed.
model = genai.GenerativeModel('gemini-2.0-flash-lite') 

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. 
Just share the dockerfile without any explanation. 
Do not include markdown code blocks (like ```dockerfile).
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    try:
        response = model.generate_content(PROMPT.format(language=language))
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    language = input("Enter the programming language (e.g., Python, Node.js, Go): ")
    dockerfile = generate_dockerfile(language)
    
    print("\n--- Start of Dockerfile ---")
    print(dockerfile.strip())
    print("--- End of Dockerfile ---\n")