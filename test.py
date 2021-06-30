import streamlit as st
import pandas as p
import base64
import io


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def get_excel_download_link(df):
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="product_plan_output_agg.xlsx">product_plan_output_agg.xlsx</a>'
    return linko


st.header("Hello")
df = p.DataFrame([["AAAAAAAAAAAAAA"]*15]*100000)
#st.markdown(get_table_download_link(df), unsafe_allow_html=True)
st.markdown(get_excel_download_link(df), unsafe_allow_html=True)
