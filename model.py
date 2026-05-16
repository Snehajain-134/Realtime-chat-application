try:
    import google.generativeai as genai
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "The google.generativeai package is not installed. "
        "Install it using: python -m pip install google-generativeai"
    ) from e

genai.configure(
    api_key="AIzaSyB55gwIdxjJQrNJ5DqDo0TT7qnd_SlIwXQ"
)

models = genai.list_models()

for model in models:
    print(model.name)