import importlib

try:
    genai = importlib.import_module("google.generativeai")
except ImportError:
    raise ImportError(
        "The google.generativeai package is not installed. "
        "Install it with: pip install google-generativeai"
    ) from None

genai.configure(
    api_key="AIzaSyB55gwIdxjJQrNJ5DqDo0TT7qnd_SlIwXQ"
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

response = model.generate_content(
    "Hello"
)

print(response.text)