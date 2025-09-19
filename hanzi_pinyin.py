import polars as pl
from read_cedict import read_cedict

hanzi = read_cedict()

text = """

沉迷在 你清澈的眼睛
是途經 最難忘的風景
無人可比擬 那些往昔
燦若繁星

每一個 為你做的決定
故事幾經輾轉 未落筆
一幕幕曾經 腦海放映
刻骨銘心
不想 不念 不聽
心也 不再 泛起 漣漪
天燈亮起 相聚別離
人來人往 終更替

翻山越嶺 尋一個你
不負此生 不負相遇
不負我偏向苦海去
只為渡你
踏遍荊棘 尋一個你
不遠萬里 只為朝夕
縱天下負盡 不負你

每一個 為你做的決定
故事幾經輾轉 未落筆
一幕幕曾經 腦海放映
刻骨銘心
不想 不念 不聽
心也 不再 泛起 漣漪
天燈亮起 相聚別離
人來人往 終更替

翻山越嶺 尋一個你
不負此生 不負相遇
不負我偏向苦海去
只為渡你
踏遍荊棘 尋一個你
不遠萬里 只為朝夕
縱天下負盡 不負你

翻山越嶺 尋一個你
不負此生 不負相遇
不負我偏向苦海去
只為渡你
踏遍荊棘 尋一個你
不遠萬里 只為朝夕
縱天下負盡 不負你

"""

tones_dict = {
    'a': ['ā', 'á', 'ǎ', 'à'],
    'e': ['ē', 'é', 'ě', 'è'],
    'i': ['ī', 'í', 'ǐ', 'ì'],
    'o': ['ō', 'ó', 'ǒ', 'ò'],
    'u': ['ū', 'ú', 'ǔ', 'ù'],
    'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ']
    }

vowels = tones_dict.keys()
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

print(pinyin_tones)
