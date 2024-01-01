# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="News Category Application | News Classification CNN Indonesia", page_icon="📺")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("News Classification: Category Application for News")
        st.caption("News is generally categorized into several types such as sports, economy, entertainment, and other categories. With this news classification, we can find the type of news category that corresponds to the content of the news.")

    news_text = st.text_area(
        "Enter News Content", key="input_text", height=250)

    if st.button("Find Category"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Show Result'):
                st.write('The news you entered belongs to the category: ')
                if text == "education":
                    st.info(text, icon="🧑‍🏫")
                    url = "https://www.google.com/search?q=education+news+today"
                    st.write(
                        'Read the latest news related to education 🔎 [Education news today](%s)' % url)
                elif text == "sports":
                    st.info(text, icon="🚣")
                    url = "https://www.google.com/search?q=sports+news+today"
                    st.write(
                        'Read the latest news related to sports 🔎 [Sports news today](%s)' % url)
                elif text == "economy":
                    st.info(text, icon="💸")
                    url = "https://www.google.com/search?q=economy+news+today"
                    st.write(
                        'Read the latest news related to the economy 🔎 [Economy news today](%s)' % url)
                elif text == "entertainment":
                    st.info(text, icon="🎥")
                    url = "https://www.google.com/search?q=entertainment+news+today"
                    st.write(
                        'Read the latest news related to entertainment 🔎 [Entertainment news today](%s)' % url)
        else:
            time.sleep(.5)
            st.toast('Please enter text first', icon='🤧')


if __name__ == "__main__":
    main()
