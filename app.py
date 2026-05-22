import streamlit as st
st.title("About Japan")

st.set_page_config(page_title="Japan Geography", page_icon="🇯🇵🗻", layout="wide")

with st.container():
     st.subheader("Hi, in this website, I'm gonna give you overview of Japan's prefectures and some major cities.")
     st.write("Let's get started!")

st.image ("https://i1-c.pinimg.com/1200x/fd/7b/ec/fd7becf818dc6a4be682b5dc77a5b1e3.jpg")

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
         st.header("Prefectures")
         st.write("##")
         st.write(
                   """"
                    In Japan, the nation is split into 47 prefectures—think of them as mini-governments within the 
                    country. They cover everything from the neon skyline of Tokyo to the snowy peaks of Nagano. 
                    Together, they paint a rich picture of Japan’s diversity.""" )
         st.write("""
                   Here’s a list of all 47 prefectures in Japan:

Hokkaido,
Aomori,
Iwate,
Miyagi,
Akita,
Yamagata,
Fukushima,
Ibaraki,
Tochigi,
Gunma,
Saitama,
Chiba,
Tokyo,
Kanagawa,
Niigata,
Toyama,
Ishikawa,
Fukui,
Yamanashi,
Nagano,
Gifu,
Shizuoka,
Aichi,
Mie,
Shiga,
Kyoto,
Osaka,
Hyogo,
Nara,
Wakayama,
Tottori,
Shimane,
Okayama,
Hiroshima,
Yamaguchi,
Tokushima,
Kagawa,
Ehime,
Kochi,
Fukuoka,
Saga,
Nagasaki,
Kumamoto,
Oita,
Miyazaki,
Kagoshima,
Okinawa""")
