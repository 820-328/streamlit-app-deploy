import streamlit as st

st.set_page_config(page_title="サンプル: かんたんWebアプリ", page_icon="✅")

st.title("サンプル: かんたんWebアプリ")
st.write("##### 機能①: 文字数カウント")
st.write("入力したテキストの文字数をカウントします。")
st.write("##### 機能②: BMI計算")
st.write("身長と体重からBMIを計算します。")

selected_item = st.radio(
    "使いたい機能を選んでください：",
    ["文字数カウント", "BMI計算"]
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数を知りたいテキストを入力してください")
    if st.button("計算"):
        st.divider()
        if input_message:
            st.write(f"文字数: **{len(input_message)}**")
        else:
            st.error("テキストを入力してください。")
else:
    height = st.text_input(label="身長（cm）を入力してください")
    weight = st.text_input(label="体重（kg）を入力してください")
    if st.button("計算"):
        st.divider()
        if height and weight:
            try:
                h = float(height) / 100
                bmi = round(float(weight) / (h ** 2), 1)
                st.write(f"BMI: **{bmi}**")
            except ValueError:
                st.error("数値で入力してください。")
        else:
            st.error("身長と体重の両方を入力してください。")