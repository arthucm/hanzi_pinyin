import polars as pl
import re

def read_cedict(source:str='hanzi_pinyin/cedict_ts.u8'):
    extracted_data = []
    regex = re.compile(r'(.+?)\s+\[(.*?)\]\s+\/(.*?)\/')

    with open(source) as file:

        for row in file:
            if row.startswith('#'):
                continue
        
            match = regex.match(row.strip())
            if match:
                characters = match.group(1).strip()
                pinyin = match.group(2).strip()
                meaning = match.group(3).strip()

                chars_list = characters.split()

                extracted_data.append({
                    'chars':chars_list,
                    'pinyin':pinyin,
                    'mean':meaning
                })
        
        df = pl.DataFrame(extracted_data)

        df = pl.DataFrame(extracted_data)
        df = \
        df.with_columns([
            pl.col('chars').list.get(0).alias('traditional'),
            pl.col('chars').list.get(1).alias('simplified')
        ])
        df.drop_in_place('chars')
        df = df.select(['traditional', 'simplified', 'pinyin', 'mean'])
        
        return df