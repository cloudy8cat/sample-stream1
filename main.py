import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Dataframe')
df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np 
import pandas as pd 
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df)

st.write('Display Image')

if st.checkbox('Show Image'):

    img = Image.open("cat.jpg")
    st.image(img, caption='cat', use_column_width=True)

st.write('Inteructive wegets')

option = st.selectbox(
    'あなたが好きな数字を入れてください。',
    list(range(1, 11))
)
'あなたの好きな数字は ', option, 'です。'

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味:', text

condition = st.slider('あなたの調子は?', 0, 100, 50)
'コンディション: ', condition

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの調子は?', 0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション: ', condition

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander = st.expander('問い合わせ')
expander.write('問い合わせの回答を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答を書く')


import streamlit as st
import time  # タイムスリープに必要

# プログレスバーの説明
st.write('プログレスバーの表示')

'Start'  # ステータス表示

# プレースホルダーを準備
latest_iteration = st.empty()  # テキストプレースホルダー
bar = st.progress(0)  # プログレスバー

# プログレスバーのループ処理
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')  # 最新の進行状況を表示
    bar.progress(i + 1)  # プログレスバーを更新
    time.sleep(0.1)  # 0.1秒待機

# 完了メッセージ
st.write("Done!")
