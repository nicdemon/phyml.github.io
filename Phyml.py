import os
import pandas as pd
import streamlit as st

from runPhyML import RunPhyML

st.set_page_config(
    page_title = "PhyML",
)

with open('DESCRIPTION.md','r') as desc:
    content = desc.readlines()
    content = ' '.join([str(elem) for elem in content])
    st.markdown(content)