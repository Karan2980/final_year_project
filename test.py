import google.generativeai as genai

genai.configure(api_key='IzaSyDr--ZyCgJI-uR8791UtZk9tkbACKABH38')

models = genai.list_models()
for model in models:
    print(f"Model Name: {model.name}")
    print(f"Supported Methods: {model.supported_generation_methods}")
