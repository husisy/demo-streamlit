import pathlib
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector

st.title('just for fun')

def is_valid_int_str(x):
    try:
        int(x)
        ret = True
    except:
        ret = False
    return ret


tmp0 = '**Random seed** (input empty to randomize)'
seed = st.session_state.get('seed', None)
if (seed is None) or (not is_valid_int_str(seed)):
    seed = int(np.random.default_rng().integers(int(1e18)))
else:
    seed = int(seed)
np_rng = np.random.default_rng(seed)
st.text_input(tmp0, str(seed), key='seed')


# https://fonts.google.com/noto/specimen/Noto+Sans+SC
font_path = pathlib.Path('NotoSansSC-Regular.otf')

def hf_draw_figure(text):
    text = [x.strip() for x in text.split(',')]
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
text_input = st.session_state.get('text_input', default_value)
hf_draw_figure(text_input)


collector = FeedbackCollector(
    component_name="demo-streamlit",
    email=st.secrets.trubrics.email, # Store your Trubrics credentials in st.secrets:
    password=st.secrets.trubrics.password, # https://blog.streamlit.io/secrets-in-sharing-apps/
)

collector.st_feedback(
    feedback_type="thumbs",
    model='none',
    metadata=dict(seed=seed, text=text_input),
    open_feedback_label="[Optional] Provide additional feedback",
)
