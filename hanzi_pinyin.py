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

print(pinyin)
