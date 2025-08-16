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

words ={'あひる','いじわる','うなる','えくあどる','おこる',
'かさばる','きりんびーる','くすぐる','ける','こおる',
'さる','しる','すとーる','せーる','そーる',
'たいむとんねる','ちらかる','つくる','てーる','とーる',
'なぐる','にげる','ぬる','ねじる','のる',
'はれる','ひっぱる','ふくらむ','へる','ほる',
'まる','みる','むーどる','めもる','もる',
'やせる','ゆにばーさる','よくばる',
'らむさーる','りにゅーある','るーる','るごーる','るのわーる',
'るーぶる','れんたるさいくる','ろーる','わびる',}

hiragana_last = "しりとり"
used_hiragana = []
used_hiragana.append(hiragana_last)

with st.form(key='ketu'):
    hiragana_now = st.text_input('しりとり')
    submit_bt = st.form_submit_button('送信')
    if submit_bt:
        if hiragana_now[0] != hiragana_last[-1]:
            if hiragana_now[-1] == "ー":
                if hiragana_now[0] != hiragana_last[-2]:
                    used_hiragana.append(hiragana_now)
                    hiragana_last = hiragana_now
            else:
                st.text("AI: 最初の文字が間違っていますよ。私の勝ちです。")
        elif hiragana_now in used_hiragana:
            st.text("AI: その単語は既に使われていますよ。私の勝ちです。")
        elif hiragana_now[-1] == "ん":
            st.text("AI: それは「ん」で終わる単語ですよ。私の勝ちです。")
        else:
            used_hiragana.append(hiragana_now)
            hiragana_last = hiragana_now
            #AIのターン
            found = False
            line = False
            if hiragana_now[-1] == "ー":
                for word in words:
                    if word.startswith(hiragana_last[-2]):
                        st.text(f"AI:{word}")
                        line = True
                        found = True
                        words.remove(word)
                        used_hiragana.append(word)
                        hiragana_last = word
            else:
                if not line:
                    for word in words:
                        if word.startswith(hiragana_last[-1]):
                            st.text(f"AI:{word}")
                            found = True
                            words.remove(word)
                            used_hiragana.append(word)
                            hiragana_last = word
            if not found:
                st.text("AI: 思いつきません。私の負けです。")