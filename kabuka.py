import pandas as pd
import altair as alt
import yfinance as yf
import streamlit as st

st.title("株価可視化アプリ")

#サイドバーの設定
st.sidebar.write("""
# GAFAvsJapan 株価
こちらは株価可視化ツールです。
以下のオプションから表示日数を指定して下さい。""")

st.sidebar.write("""
## 表示日数設定　""" )

days = st.sidebar.slider("日数",1,50,20)

st.write(f"""
### 過去 **{days}日間** の株価
""")


@st.cache
#毎回データを取得するのではなく、キャッシュでとることが出来る
def get_data(days,tickers):
    df=pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index=hist.index.strftime('%d %B %Y')
        hist=hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name="Name"
        df = pd.concat([df, hist])
    return df


try:
        st.sidebar.write("""
        ## 株価の範囲指定
        """)

        ymin, ymax = st.sidebar.slider(
            '範囲を指定してください',
            0.0, 3500.0,(0.0,3500.0)
        )

        tickers={
            'apple':'AAPL',
            'facebook':'META',
            'google':'GOOGL',
            'microsoft':'MSFT',
            'nexflix': 'NFLX',
            'amazon': 'AMZN',
            'TOTO' : '5332.T',
            'TOYOTA' : '7203.T'
        }

        df = get_data(days,tickers)

        companies = st.multiselect(
            '会社名を選択して下さい。',
            list(df.index),
            ['google','amazon','facebook','amazon']
        )

        if not companies:
            st.error("少なくても1社は選んでください")
        else:
            data = df.loc[companies]
            st.write("### 株価(USD)",data.sort_index())
            data = data.T.reset_index()
            data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )

            chart = (
                alt.Chart(data)
                .mark_line(opacity=0.8)
                .encode(
                    x="Date:T",
                    y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin,ymax])),
                    color="Name:N"
                )

            )
        st.altair_chart(chart,use_container_width=True)

except : 
    st.error('何かエラーがでているようです！')
