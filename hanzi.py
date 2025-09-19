import polars as pl
from read_cedict import read_cedict

def hanzi_to_pinyin(text:str, marks:bool=True):
        
    hanzi = read_cedict()

    text = text

    tones_dict = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'u': ['ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ']
        }

    priority = "aeiouüv"

    pinyin = ''
    for char in text:
        trad = hanzi.filter(pl.col('traditional') == char).get_column('pinyin')
        simpl = hanzi.filter(pl.col('simplified') == char).get_column('pinyin')
        if simpl.shape[0] > 0:
            pinyin += simpl[0].lower() + ' '
        elif trad.shape[0] > 0:
            pinyin += trad[0].lower() + ' '
        else:
            pinyin += char

    pinyin_tones = ''
    for row in pinyin.split(sep='\n'):
        pinyin_tones += '\n'
        for word in row.split():
            pref_vowel = ''
            for char in priority[::-1]:
                if word.find(char) != -1:
                    pref_vowel = char
            if word[-1] == '5':
                pinyin_tones += word[:-1]
            elif word[-1] == '4':
                with_tone = word[:-1].replace(pref_vowel, tones_dict[pref_vowel][3], 1)
                pinyin_tones += with_tone + ' '
            elif word[-1] == '3':
                with_tone = word[:-1].replace(pref_vowel, tones_dict[pref_vowel][2], 1)
                pinyin_tones += with_tone + ' '
            elif word[-1] == '2':
                with_tone = word[:-1].replace(pref_vowel, tones_dict[pref_vowel][1], 1)
                pinyin_tones += with_tone + ' '
            elif word[-1] == '1':
                with_tone = word[:-1].replace(pref_vowel, tones_dict[pref_vowel][0], 1)
                pinyin_tones += with_tone + ' '
            else:
                pinyin_tones += word + ' '

    if marks:
        print(pinyin_tones)
        return pinyin_tones
    else:
        print(pinyin)
        return pinyin