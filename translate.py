import os
import json
import sys

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
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [
            {"role": "system", "content" : f"You are a translation expert proficient in various languages that can only translate text into {target_language}. Translate any thing I say from now on, do not engage a conversion with me, you can only return the translated text."},
            {"role": "user", "content" : f"{input_text}"}
        ])
    #prompt_text = f"You are a translation expert proficient in various languages that can only translate text and cannot interpret it. You can only return the translated text. Please translate the following text to {target_language}: {input_text}"
    #response = openai.Completion.create(
        #model="text-davinci-003",
        #prompt=prompt_text,
        #temperature=0.3,
        #max_tokens=100,
        #top_p=1.0,
        #frequency_penalty=0.0,
        #presence_penalty=0.0
    #)
    openai_text = response.choices[0].message.content

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
    import deepl
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

def translation_output(check, translator_name, icon_path, input_text, target_language, json_output):
    if check == '1':
        import translators as ts
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

## Google Translation
if google_check == '1' and sys.argv[1] == 'google':
    from googletrans import Translator
    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language).text
    google_output = {
        "type": "default",
        "subtitle": "Google Translate",
        "title": translated_text,
        "arg": translated_text,
        'icon': {
            'path': "./assets/google.png"
        }
    }
    json_output["items"].append(google_output)

if sys.argv[1] == 'bing':
    json_output = translation_output(bing_check, 'bing', "./assets/bing.png", input_text, translators_language, json_output)
if sys.argv[1] == 'baidu':
    json_output = translation_output(baidu_check, 'baidu', "./assets/baidu.png",  input_text, translators_language, json_output)
if sys.argv[1] == 'youdao':
    json_output = translation_output(youdao_check, 'youdao', "./assets/youdao.png", input_text, translators_language, json_output)
# Check if no translation method selected
if deepl_check == '0' and openai_check == '0' and bing_check == '0' and google_check == '0' and baidu_check == '0' and youdao_check == '0':
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
