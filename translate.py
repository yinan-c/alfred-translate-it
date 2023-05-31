import os
import openai
import deepl
import json
import sys
import translators as ts

openai.api_key = os.getenv("OPENAI_API_KEY")
auth_key = os.getenv("DEEPL_API_KEY")

deepl_check = os.getenv("deepl_check")
openai_check = os.getenv("openai_check")
bing_check = os.getenv("bing_check")
google_check = os.getenv("google_check")
baidu_check = os.getenv("baidu_check")
youdao_check = os.getenv("youdao_check")

target_language = os.getenv("target_language")
if target_language.lower() in ['en-gb', 'en-us']:
    translators_language = 'en'
else:
    translators_language = target_language

def get_query() -> str:
    """Join the arguments into a query string."""
    return " ".join(map(str, sys.argv[2:]))

input_text = get_query()

json_output = {
    "items": []
}


# OpenAI Translation
if openai_check == '1' and sys.argv[1] == 'openai':
    
    prompt_text = f"Translate the following text to {target_language}: {input_text}"
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
if deepl_check == '1' and sys.argv[1] == 'deepl':
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

def translation_output(check, translator_name, icon_path, ts, input_text, target_language, json_output):
    if check == '1':
        translated_text = ts.translate_text(input_text, to_language=target_language, translator=translator_name)
        output = {
            "type": "default",
            "subtitle": translator_name.capitalize(),
            "title": translated_text,
            "arg": translated_text,
            'icon': {
                'path': icon_path
            }
        }
        json_output["items"].append(output)
    return json_output
if sys.argv[1] == 'bing':
    json_output = translation_output(bing_check, 'bing', "./assets/bing.png", ts, input_text, translators_language, json_output)

if sys.argv[1] == 'google':
    json_output = translation_output(google_check, 'google', "./assets/google.png", ts, input_text, translators_language, json_output)
if sys.argv[1] == 'baidu':
    json_output = translation_output(baidu_check, 'baidu', "./assets/baidu.png", ts, input_text, translators_language, json_output)
if sys.argv[1] == 'youdao':
    json_output = translation_output(youdao_check, 'youdao', "./assets/youdao.png", ts, input_text, translators_language, json_output)

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
