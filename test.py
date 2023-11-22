import time
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("DateFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})


# pandasのDataFrameオプションで、
# "カラム":[データ群]　という枠を作成する

st.write(df)
st.dataframe(df) #下のように、サイズの変更などカスタム可能
st.dataframe(df,width = 100, height = 100)
st.dataframe(df.style.highlight_max(axis=0))

#ただの静的な表
st.table(df.style.highlight_max(axis=0))

#"""でマークダウンになる

df2= pd.DataFrame(
    np.random.rand(20,3),
    columns = ["a","b","c"]
)
#np.random(行,列)の行列を作るという意味
#randは正規分布をもとにした少数を作成する

st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=("lat","lon")
)
st.map(df3)

if st.checkbox("Show Image"):
    img = Image.open("_MG_6836.jpg")
    st.image(img,caption="Ryoji",use_column_width=True)

#インタラクティブ=双方向strea

options = st.selectbox(
    "数字を選択してください",
    range(1,11)
)
"あなたの好きな数字は",options,"です。"

text = st.text_input("趣味を入力")
"あなたの趣味：",text


satisfaction = st.slider("現在の満足度",0,100,50)
"満足度：",satisfaction

lc,rc = st.columns(2)
button = lc.button("右カラムに文字を表示")
if button:
    rc.write("ここに文字が表示される")

expander = st.expander("問合せ")

expander.write("1")
expander.write("2")
expander.write("3")
expander.write("4")
expander.write("5")

iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    iteration.text(f"イテレーター{i}")
    bar.progress(i + 1)
    time.sleep(0.5)
