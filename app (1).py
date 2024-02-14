import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image_yt = Image.open('youtube-logo-small.png')
st.image(image_yt, width = 80)


st.title("YouTube Data")

# Clean up the data
df = pd.read_csv("Global YouTube Statistics.csv", encoding='unicode_escape')
df = df.dropna()
df.drop(101, axis = 0, inplace = True)

# Sort by top subbed
df_top_subbed = df.head(10)
df_top_subbed = df_top_subbed.sort_values(by="subscribers", ascending=False)

st.dataframe(df.head(5))

st.subheader("Overview")
m1, m2 = st.columns((1,1))
m1.metric(label ='Number of Channels', value = df.shape[0])
m2.metric(label ='Avg Subs', value = df["subscribers"].mean())

st.subheader("Top Channels")
st.bar_chart(data=df_top_subbed, x="Youtuber", y="subscribers", color="#FF0000", use_container_width=True)

group_by_year = df.groupby(['created_year']).size()

st.subheader("Channels by Create Year")
st.line_chart(group_by_year)

st.subheader("Channels by Location")
st.map(data=df, latitude="Latitude", longitude="Longitude", color="#FF0000", use_container_width=True)
