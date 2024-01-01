# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita CNN Indonesia", page_icon="📺")

    col1, col2 = st.columns(2)

    with col1:

        st.image("assets/banner.png", use_column_width=True)

    with col2:
        st.subheader("News Classification: Aplikasi Kategori untuk Berita")
        st.caption("Berita umumnya dikategorikan menjadi beberapa jenis kategori seperti olahraga, ekonomi, hiburan dan kategori lainnya. Dengan news classification ini kita dapat menemukan jenis kategori berita yang sesuai dengan isi berita tersebut.")

    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                if text == "edukasi":
                    st.info(text, icon="🧑‍🏫")
                    url = "https://www.google.com/search?q=berita+edukasi+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait edukasi 🔎 [Berita edukasi hari ini](%s)'  %url)
                elif text == "olahraga":
                    st.info(text, icon="🚣")
                    url = "https://www.google.com/search?q=berita+olahraga+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait olahraga 🔎 [Berita olahraga hari ini](%s)'  %url)
                elif text == "ekonomi":
                    st.info(text, icon="💸")
                    url = "https://www.google.com/search?q=berita+ekonomi+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait ekonomi 🔎 [Berita ekonomi hari ini](%s)'  %url)
                elif text == "hiburan":
                    st.info(text, icon="🎥")
                    url = "https://www.google.com/search?q=berita+hiburan+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait hiburan 🔎 [Berita hiburan hari ini](%s)'  %url)
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu', icon='🤧')


if __name__ == "__main__":
    main()
