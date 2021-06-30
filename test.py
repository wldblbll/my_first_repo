import streamlit as st
import pandas as p
import base64


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href


st.header("Hello")
df = p.DataFrame([["AAAAAAAAAAAAAA"]*15]*100000)
st.markdown(get_table_download_link(df), unsafe_allow_html=True)
