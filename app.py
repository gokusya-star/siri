import streamlit as st
import random
from PIL import Image

#文字
st.title("しりとり")
n = random.randint(1,100)
st.caption(n)
st.subheader("HEY BRO")
st.text("WHATS UP?")

#コード
code = '''
import streamlit as st

st.title("しりとり")
'''
st.code(code, language='python')

#画像
image = Image.open('タイトルなし.png')
st.image(image, width=200)
#動画
#video_file = open('無題の動画 ‐ Clipchampで作成 (13).mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

with st.form(key='form'):
    name = st.text_input('名前')

    slct = st.radio('好き？',('好き','普通','嫌い'))
    #slct = st.selectbox('好き？',('好き','普通','嫌い'))

    prime = st.multiselect('素数は？',('1','2','3','4','5'))

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ{slct}な{", ".join(prime)}の{name}さん')
        print(name,slct,", ".join(prime))
    #print(f'submit_btn: {submit_btn}')
    #print(f'cancel_btn: {cancel_btn}')
