import streamlit as st
import random
from PIL import Image

#文字
st.title("しりとり")

image = Image.open('タイトルなし.png')
st.image(image, width=200)

with st.form(key='form'):
    name = st.text_input('名前')

    slct = st.radio('ごくしゃのこと好き？',('好き','普通','嫌い'))

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'あなた{name}っていうのね！')
        st.text(f'となりの{name}っ{name}っ♪')
        print(name,slct)

# セッション初期化
if "used_hiragana" not in st.session_state:
    st.session_state.used_hiragana = ["しりとり"]
if "hiragana_last" not in st.session_state:
    st.session_state.hiragana_last = "しりとり"
if "words" not in st.session_state:
    st.session_state.words = {'あひる','いじわる','うなる','えくあどる','おこる',
    'かさばる','きりんびーる','くすぐる','ける','こおる',
    'さる','しる','すとーる','せーる','そーる',
    'たいむとんねる','ちらかる','つくる','てーる','とーる',
    'なぐる','にげる','ぬる','ねじる','のる',
    'はれる','ひっぱる','ふくらむ','へる','ほる',
    'まる','みる','むーどる','めもる','もる',
    'やせる','ゆにばーさる','よくばる',
    'らむさーる','りにゅーある','るーる','るごーる','るのわーる',
    'るーぶる','れんたるさいくる','ろーる','わびる',}

st.title("しりとり")

with st.form(key='ketu'):
    hiragana_now = st.text_input('しりとり')
    submit_bt = st.form_submit_button('送信')

    if submit_bt and hiragana_now:
        last = st.session_state.hiragana_last
        used = st.session_state.used_hiragana
        words = st.session_state.words

        # 「ー」で終わる場合は一つ前の文字を採用
        last_char = last[-2] if last[-1] == "ー" else last[-1]

        if hiragana_now[0] != last_char:
            st.error("AI: 最初の文字が間違っていますよ。私の勝ちです。")
        elif hiragana_now in used:
            st.error("AI: その単語は既に使われていますよ。私の勝ちです。")
        elif hiragana_now[-1] == "ん":
            st.error("AI: それは「ん」で終わる単語ですよ。私の勝ちです。")
        else:
            # ユーザーの単語を追加
            used.append(hiragana_now)
            st.session_state.hiragana_last = hiragana_now

            # AIのターン
            last_char = hiragana_now[-2] if hiragana_now[-1] == "ー" else hiragana_now[-1]
            found = False
            for word in list(words):
                if word.startswith(last_char):
                    st.success(f"AI: {word}")
                    used.append(word)
                    words.remove(word)
                    st.session_state.hiragana_last = word
                    found = True
                    break
            if not found:
                st.info("AI: 思いつきません。私の負けです。")

# 使用済み単語を表示
st.write("これまでの単語:", " → ".join(st.session_state.used_hiragana))
