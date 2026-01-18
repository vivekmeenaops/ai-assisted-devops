from google import genai  # Use the new unified SDK
import os

# Set your API key
os.environ["GOOGLE_API_KEY"] = "xxxxxxxxxxx"

# The client automatically picks up GOOGLE_API_KEY from environment
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use a 2026-stable model name
MODEL_ID = "gemini-2.0-flash-lite" 

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. 
Just share the dockerfile without any explanation or markdown code blocks.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    try:
        # New SDK uses client.models.generate_content
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=PROMPT.format(language=language)
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    language = input("Enter the programming language (e.g., Python, Node.js): ")
    dockerfile = generate_dockerfile(language)
    
    print("\n--- Generated Dockerfile ---")
    print(dockerfile.strip())
    print("--- End of Output ---")