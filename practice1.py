import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


st.title("俺のサウナ")

#画像の表示
st.write("Display Image")
img = Image.open('sauna2.jpg')
st.image(img, caption="let's go to sauna", use_column_width=True)


#プログレスバーの表示 0.1秒ごと
'Start!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

"Welcome!!"


#map お店の場所の緯度と経度を入れれば出てくる。
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.map(df)

#インタラクティブ　動的な変化を起こす
#チェックボックスが入ると画像が表示する

if st.checkbox('サウナに持っていくお勧めグッズ'):
    img2 =Image.open('saunaglass.jpg')
    st.image(img2, caption="JINSが発売している120度に耐えられるサウナ用メガネ", use_column_width=True)

#1～10の数字をつくる
#list(range(1,11))

#セレクトボックスに指定した数字がoptionに入る
option=st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたが好きな数字は、', option, 'です。'

#テキスト入力の方法
text = st.sidebar.text_input('あなたのお気に入りのサウナを教えて下さい')
'あなたのお気に入りサウナ：',text

#スライダー
condition = st.sidebar.slider("あなたの今日の調子は？",0, 100, 50)
'コンディション:', condition