import os
import openai
import deepl
import json
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
auth_key = os.getenv("DEEPL_API_KEY")

deepl_check = os.getenv("deepl_check")
openai_check = os.getenv("openai_check")

source_language = os.getenv("source_language")
target_language = os.getenv("target_language")

def get_query() -> str:
    """Join the arguments into a query string."""
    return " ".join(map(str, sys.argv[1:]))

input_text = get_query()

json_output = {
    "items": []
}


# OpenAI Translation
if openai_check == '1':
    prompt_text = f"Please translate from {source_language} to {target_language}: {input_text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_text,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    openai_text = response.choices[0].text.strip()

    openai_output = {
        "type": "default",
        "subtitle": "OpenAI",
        "title": openai_text,
        "arg": openai_text,
        'icon': {
            'path': "./assets/openai.png"
        }
    }
    json_output["items"].append(openai_output)

# DeepL Translation
if deepl_check == '1':
    deepl_translator = deepl.Translator(auth_key) 
    deepl_result = deepl_translator.translate_text([input_text], target_lang=target_language) 
    deepl_text = deepl_result[0].text

    deepl_output = {
        "type": "default",
        "subtitle": "DeepL",
        "title": deepl_text,
        "arg": deepl_text,
        'icon': {
            'path': "./assets/deepl.png"
        }
    }
    json_output["items"].append(deepl_output)

# Check if no translation method selected
if not json_output["items"]:
    no_selection_output = {
        "type": "default",
        "title": "Please select at least one translation method",
        "subtitle": "",
        "arg": "",
        'icon': {
            'path': "./icon.png"
        }
    }
    json_output["items"].append(no_selection_output)

# Write the dictionary to file as JSON
print(json.dumps(json_output))
