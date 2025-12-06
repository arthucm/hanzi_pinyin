# Hanzi to Pinyin Converter

## Introduction

This project simply converts mandarin characters (hanzi) to pinyin.

It is suitable if you want to practice reading, pronounciation or just being able to sing a chinese song.
___
## How to use
First, you just need to install the polars library into you computer, if you don't already have it.
In order to do it, run this snippet in your terminal: 

`pip install polars`

Then, to use it effectively, just import the hanzi_to_pinyin function from hanzi.py file and insert the desired text in it, as shown in the trial.py file.
___

## Attribution

The database used for pinyin conversion was CC-CEDICT database (cedict_ts.u8 file), under following license:
- **CC-CEDICT** by Paul Andrew Denisowski - https://cc-cedict.org/wiki/
- Licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)

No modifications were made to the database directly, it was only used for data extraction and usage.