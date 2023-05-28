# Alfred Translate-It 

An Alfred 5 workflow to translate text from any source to any target, using OpenAI, DeepL, Google, Bing, Baidu and Youdao. This workflow also support [Universal Actions](https://www.alfredapp.com/universal-actions/).

**NOTE**: OpenAI model 'text-davinci-003' is used in translation.
Some tranlation services (e.g. OpenAI, youdao) may be slow and delay the output.

If delay is a big issue, test the speed of each translation service and choose which ones to disable. 

## Requirements
[Alfred PowerPack](https://www.alfredapp.com/powerpack/)

OpenAI Translation: [OpenAI API](https://platform.openai.com/)

DeepL Translation: [DeepL API](https://www.deepl.com/pro-api)

Other translation services: Requires [translators](https://github.com/UlionTse/translators) library, installed via:

```
# PYPI
pip install --upgrade translators

# Conda
conda install -c conda-forge translators

# Source
git clone https://github.com/UlionTse/translators.git
cd translators
python setup.py install
```

## Usage
- Set up: target language, method of translation and your APIs.
(Please check supported source language code from [DeepL API docs](https://www.deepl.com/docs-api/translate-text) and [Translators library](https://github.com/UlionTse/translators))
- Type anything followed by keyword `trans`, `⏎` to translate, it will auto-detect source language.
- Then select any result and `⏎` to copy text to your clipboard
- `⌘ + ⏎` to view large text (useful if results are long)
- For universal control, simple select any text and search `translate it`.

![](https://i.imgur.com/IPiXLF4.png)
![](https://i.imgur.com/AZZOy2w.png)
![](https://i.imgur.com/XO0Ub0K.png)
![](https://i.imgur.com/ZyaL4O3.png)
![](https://i.imgur.com/lN3CTVK.png)

You can turn off the checkbox in the configuration and only use your DeepL API.


## Thanks
- Open-source project [UlionTse/translators](https://github.com/UlionTse/translators), a library which aims to bring free, multiple, enjoyable translation to individuals and students in Python.


For redering results speed, I am thinking about rendering the results in a sequence instead of showing them all at once, but I am not sure if Alfred will allow that.
**Any suggestions are welcomed here!**
