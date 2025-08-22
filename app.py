import streamlit as st
import random
from PIL import Image
from janome.tokenizer import Tokenizer
import pykakasi

tokenizer = Tokenizer()
kks = pykakasi.kakasi()

#文字
st.title("ごくしゃ")

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
    st.session_state.words = {
        'あげる','あらわる','ある',
        'いる','いじる','いれる',
        'うつる','うねる','うける',
        'える','えらぶ','おさめる',
        'おちる','おどる','かける',
        'かざる','かぶる','きる',
        'きゃらめる','きゃんせる','くだる',
        'くれる','くねる','こぼれる',
        'こする','こだわる','ささる',
        'さける','さまよう','しめる',
        'しる','しまる','すべる',
        'すわる','すする','せめる',
        'せーる','せまる','そそる',
        'そだてる','そろえる','たべる',
        'たどる','たくわえる','ちゃんねる',
        'ちぢる','ちかよる','つづける',
        'つつむ','つかまる','てる',
        'てらす','ていする','とる',
        'とどける','とりぷる','ないちんげーる',
        'なげる','なる','にげる',
        'にらむ','にぎる','ぬる',
        'ぬーどる','ぬすまれる','ねる',
        'ねじる','ねばる','のぼる',
        'のる','のぞむ','はしる',
        'はれる','はさむ','ひかる',
        'ひっぱる','ひろげる','ふる',
        'ふくらむ','ふせる','へる',
        'へいほうめーとる','へだてる','ほる',
        'ほめる','ほーる','まわる',
        'まもる','まねる','みる',
        'みがく','みつける','むすぶ',
        'むかえる','むしる','めもる',
        'めざめる','めぐる','もどる',
        'もる','もえる','やせる',
        'やめる','やりとげる','よる',
        'よびかける','よくばる','わびる',
        'わたる','わかる','らむさーる',
        'らいばる','らんどせる','りにゅーある',
        'りある','りさいくる','るーる',
        'るごーる','るのわーる','れんたる',
        'れべる','れーる','ろーる',
        'ろけっと','ろる','がんばる',
        'がる','がーる','ぎゅうじる',
        'ぎゃる','ぎゃんぶる','ぐりる',
        'ぐるぐる','ぐれる','げーとぼーる',
        'げんじぼたる','げーとる','ごーる',
        'ござる','ごねる','ざる',
        'ざいる','ざんする','じれる',
        'じぇる','じぐそーぱずる','ずれる',
        'ずる','ずっこける','ぜんじる',
        'ぜっする','ぜっぷ','ぞんじる',
        'ぞんじあげる','ぞくする','だぶる',
        'だんぼーる','だんべる',
        'ぢご','づら','づけ',
        'でる','でかける','でまわる',
        'どーる','どなる','どりる',
        'ばずる','ばける','ばーる',
        'びにーる','びる','びーる',
        'ぶつける','ぶらさげる','ぶれる',
        'べんずる','べる','べーる',
        'ぼける','ぼーる','ぼとる',
        'ぱられる','ぱくる','ぱずる',
        'ぴーる','ぴる','ぴすとる',
        'ぷーる','ぷーどる','ぷれる',
        'ぺだる','ぺっとぼとる','ぺんてる',
        'ぽにーてーる','ぽーる','ぽーたぶる'
    }

def in_dictionary(word: str) -> bool:
    tokens = list(tokenizer.tokenize(word))
    return len(tokens) == 1 and tokens[0].surface == word

st.title("しりとり  V4.2")
st.text("ひらがなで入力してください。")

with st.form(key='ketu'):
    iuput_moji = st.text_input('しりとり')
    cache = kks.convert(iuput_moji)
    hiragana_now = "".join([r['hira'] for r in cache])
    submit_bt = st.form_submit_button('送信')

    if submit_bt and hiragana_now:
        if in_dictionary(iuput_moji):
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
                used.append(iuput_moji)
                st.session_state.hiragana_last = hiragana_now

                # AIのターン
                last_char = hiragana_now[-2] if hiragana_now[-1] == "ー" else hiragana_now[-1]
                found = False
                for word in list(words):
                    if word.startswith(last_char):
                        if not word in used:
                            st.success(f"AI: {word}")
                            used.append(word)
                            words.remove(word)
                            st.session_state.hiragana_last = word
                            found = True
                            break
                if not found:
                    st.info("AI: 思いつきません。私の負けです。")
        else:
            st.error("AI: そんな単語ほんとにあるんですか？")

    # 使用済み単語を表示
    st.write("これまでの単語:", " → ".join(st.session_state.used_hiragana))