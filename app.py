import pathlib
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

st.title('just for fun')


def hf_set_seed():
    try:
        seed = int(st.session_state['input_seed'])
    except:
        seed = int(np.random.default_rng().integers(int(1e18)))
    st.session_state['seed'] = str(seed)
    st.session_state['np_rng'] = np.random.default_rng(seed)
tmp0 = 'Set random seed (input empty to randomize)'
tmp1 = st.session_state.get('seed', None)
if tmp1 is None:
    tmp1 = str(np.random.default_rng().integers(int(1e18)))
    st.session_state['np_rng'] = np.random.default_rng(int(tmp1))
st.text_input(tmp0, tmp1, key='input_seed', on_change=hf_set_seed)


# https://fonts.google.com/noto/specimen/Noto+Sans+SC
font_path = pathlib.Path('NotoSansSC-Regular.otf')

def hf_draw_figure(text):
    text = [x.strip() for x in text.split(',')]
    np_rng = st.session_state['np_rng']
    fig,ax = plt.subplots()
    for text_i in text:
        pos_x,pos_y = np_rng.uniform(0, 1, size=(2))
        rotation = np_rng.uniform(-180, 180)
        color = np_rng.uniform(0, 1, size=(3))
        fontsize=  np_rng.uniform(20, 100)
        ax.text(pos_x, pos_y, text_i, rotation=rotation, color=color, fontsize=fontsize, font=font_path)
    ax.axis('off')
    st.pyplot(fig)

default_value = 'Doge, 鼠鼠我呀, 瘫, 屯屯鼠本鼠, Kokomi'
st.text_input('keywords', default_value, key='text_input')
tmp0 = st.session_state.get('text_input', default_value)
hf_draw_figure(tmp0)
