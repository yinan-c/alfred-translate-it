# Alfred Translate-It 

An Alfred 5 workflow to translate text using OpenAI, DeepL, Google, Bing, Baidu and Youdao. This workflow also support [Universal Actions](https://www.alfredapp.com/universal-actions/).

~~**NOTE**: OpenAI model 'text-davinci-003' is used in translation.~~ (changed to gpt-3.5-turbo in v1.2)

## Requirements
- [Alfred PowerPack](https://www.alfredapp.com/powerpack/)
- Google translation is free and unlimited, but may fail in mainland China. 
- OpenAI Translation: [OpenAI API](https://platform.openai.com/)
- DeepL Translation: [DeepL API](https://www.deepl.com/pro-api)
- Other translation services: Requires [translators](https://github.com/UlionTse/translators) library, installed via:
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
- Type anything after keyword `trans` to translate, it will auto-detect source language.
- Then select any result and `⏎` to copy text to your clipboard
- `⌘ + ⏎` to view large text (useful if results are long)
- For universal control, simple select any text and search for `translate`.

![](https://i.imgur.com/ANXHurD.png)
![](https://i.imgur.com/yQu85NR.png)
![](https://i.imgur.com/tpAXeBo.png)

## Thanks
- Open-source project [UlionTse/translators](https://github.com/UlionTse/translators), a library which aims to bring free, multiple, enjoyable translation to individuals and students in Python.
- Inspired by a [discussion](https://github.com/tisfeng/Easydict/issues/78) in a great macapp [tisfeng/easydict](https://github.com/tisfeng/easydict)
- [py-googletrans](https://www.github.com/ssut/py-googletrans)

~~Some tranlation services (e.g. OpenAI, youdao) may be slow and delay the output.~~
~~If delay is a big issue, test the speed of each translation service and choose which ones to disable.~~ (fixed in v 1.2)

For redering results speed, I am thinking about rendering the results in a sequence instead of showing them all at once, but I am not sure if Alfred will allow that.
> Found a workaround in in v1.2 update.

**Any suggestions are welcomed here!**
