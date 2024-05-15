# Alfred Translate-It 

An Alfred 5 workflow to translate text using OpenAI, DeepL, Google, Bing, Baidu and Youdao. This workflow also supports [Universal Actions](https://www.alfredapp.com/universal-actions/).


## Requirements
- [Alfred PowerPack](https://www.alfredapp.com/powerpack/)
- Python3 (system shipped Python3 not recommended, use other sources like, [Homebrew](https://brew.sh/) or [pyenv](https://github.com/pyenv/pyenv) installed Python3)
- Google translation is free and unlimited and requires no dependency, but may fail in mainland China. 
- OpenAI Translation requires [OpenAI API](https://platform.openai.com/)
- DeepL Translation requires [DeepL API](https://www.deepl.com/pro-api)
- Other translation services require [translators](https://github.com/UlionTse/translators) library, install via:
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
- Type anything after keyword `trans` to translate, it will auto-detect the source language.
- Then select any result and `⏎` to copy text to your clipboard
- `⌘ + ⏎` to view large text (useful if results are long)
- For universal control, simply select any text and search for `translate`.
- Set up basic language configs (base target and keyword) in case you want to add a second translation target, which might be beneficial for bidirectional translation or multilingual support.

![](https://i.imgur.com/ANXHurD.png)
![](https://i.imgur.com/yQu85NR.png)
![](https://i.imgur.com/tpAXeBo.png)

## Thanks
- Open-source project [UlionTse/translators](https://github.com/UlionTse/translators), a library which aims to bring free, multiple, enjoyable translation to individuals and students in Python.
- Inspired by a [discussion](https://github.com/tisfeng/Easydict/issues/78) in a great macapp [tisfeng/easydict](https://github.com/tisfeng/easydict)
- [py-googletrans](https://www.github.com/ssut/py-googletrans)

**Any suggestions are welcome!**

# Please consider buying me a coffee if you find this workflow helpful
<a href="https://www.buymeacoffee.com/yinan" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>