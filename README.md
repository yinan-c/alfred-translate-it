# Alfred Translate-This 

An Alfred 5 workflow to translate text from any source to any target, using OpenAI and DeepL API. This workflow also support [Universal Actions](https://www.alfredapp.com/universal-actions/).

## Requirements
[OpenAI API](https://platform.openai.com/) and [DeepL API](https://www.deepl.com/pro-api) and [Alfred PowerPack.](https://www.alfredapp.com/powerpack/)

## Usage
- Set up: source language, target language, method of translation and your APIs.
(Target and source language code should be following the [DeepL API docs](https://www.deepl.com/docs-api/translate-text) if you are using DeepL.)
- Type anything followed by keyword `trans`, `⏎` to translate
- Then select any result and `⏎` to copy text to your clipboard
- `⌘ + ⏎` to view large text (useful if results are long)

![](https://i.imgur.com/dVXv9Vb.png)
![](https://i.imgur.com/IQFgFhO.png)
![](https://i.imgur.com/OP3p7Ge.png)
![](https://i.imgur.com/oblAPqb.png)

NOTE: OpenAI model 'text-davinci-003' is used in translation, can be slow and costy, use at your own risk.
You can turn off the checkbox in the configuration and only use your DeepL API.

**I plan to add more translation services (google, youdao ...) in the future, any suggestions are welcomed here!**
