import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gold_Price_Analysis")
st.title("GOLD PRICE ANALYSIS")
file=st.file_uploader("Upload the gold price file as CSV",type=['CSV'])
menu=st.sidebar.selectbox("Select Option",["Home","Dataset Preview","Custom Preview"])
if file:
    df=pd.read_csv(file)

   
    if menu=="Home":
        st.header("Recent Market Value")
        recentDate=df["Date"].iloc[-1]
        st.info(f"Market Value As Per: ' {recentDate} '")

        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.subheader("Open Prize")
            openprize=df["Open"].iloc[-1]
            st.info(openprize)
        with col2:
            st.subheader("Max Prize")
            maxprize=df["High"].iloc[-1]
            st.info(maxprize)
        with col3:
            st.subheader("Min Prize")
            minprize=df["Low"].iloc[-1]
            st.info(minprize)
        with col4:
            st.subheader("Close Prize")
            closeprize=df["Close"].iloc[-1]
            st.info(closeprize)

        st.header("Gold Value Growth")
        growth= closeprize-openprize
        if growth >0:
            st.success(f"📈 {growth}")   
        elif growth < 0:
            st.error(f"📉 {growth}")  
        elif growth==0:
            st.warning(growth)    

        st.header("Total Market Value")
        startdate=df["Date"].iloc[0] 
        st.info(f"Market Value From ' {startdate} '-' {recentDate} '")
        co1,co2,co3,co4=st.columns(4)
        with co1:
            st.subheader("Mean Close Prize")
            meanclose=np.mean(df["Close"])
            st.info(meanclose)
        with co2:
            st.subheader("Volatility Movement")
            Volatility=np.std(df["Volatility_20"])
            st.info(Volatility)
        with co3:
            st.subheader("Maximum Close Prize")
            maxclose=np.max(df["Close"])
            st.info(maxclose)
        with co4:
            st.subheader("Minimum Close Prize")
            minclose=np.min(df["Close"])
            st.info(minclose)
        
        st.header("Yearly Close Price Average")
        year_avg = df.groupby("Year")["Close"].mean()
        st.write(year_avg)

    if menu=="Dataset Preview":
        df["Date"]=pd.to_datetime(df["Date"])
        st.title("Dataset Preview")
        min_year=int(df["Year"].min())
        max_year=int(df["Year"].max())

        year_range=st.slider("Filter Year Range",min_year,max_year,(min_year,max_year))
        filtering_dataset=df[(df["Year"]>=year_range[0])&(df["Year"]<=year_range[1])]
        st.dataframe(filtering_dataset)

        st.subheader("Graphical Representation")

        cl1,cl2=st.columns(2)
        with cl1:
            chart=st.selectbox("Select Chart Type ",["Line Chart","Bar Chart","Histogram"])
        with cl2:
            sel_col=st.selectbox("Select Column ",["Open","Max","Min","Close"])
        
        if chart=="Line Chart":
            if sel_col=="Open":
                st.line_chart(df["Open"])
            elif sel_col=="Max":
                st.line_chart(df["High"])
            elif sel_col=="Min":
                st.line_chart(df["Low"])
            elif sel_col=="Close":
                st.line_chart(df["Close"])

        elif chart=="Bar Chart":
            if sel_col=="Open":
                st.bar_chart(df["Open"])
            elif sel_col=="Max":
                st.bar_chart(df["High"])
            elif sel_col=="Min":
                st.bar_chart(df["Low"])
            elif sel_col=="Close":
                st.bar_chart(df["Close"])

        elif chart=="Histogram":
            if sel_col=="Open":
                fig,ax=plt.subplots()
                ax.hist(df["Open"],bins=50)
            elif sel_col=="Max":
                fig,ax=plt.subplots()
                ax.hist(df["High"],bins=50)
            elif sel_col=="Min":
                fig,ax=plt.subplots()
                ax.hist(df["Low"],bins=50)
            elif sel_col=="Close":
                fig,ax=plt.subplots()
                ax.hist(df["Close"],bins=50)
            st.pyplot(fig)

        st.info("To download the data click the below button")
        download=filtering_dataset.to_csv(index=False).encode('utf-8')
        st.download_button(" Download Data",
                           download,
                           "Filtered_Data.CSV"
                           "text/csv")
        
    
    if menu=="Custom Preview":
        st.title("Custom Stats")
        filtered_data=df
        c1,c2=st.columns(2)
        with c1:
            filter1=st.selectbox("Select Option",["None","Date","Month","Year"])
        with c2:
            filter2=st.selectbox("Select Option",["None","Max","Min","Close","Open"])

        if "show_data" not in st.session_state:
            st.session_state.show_data = False

        st.text("Show/Hide")
        if st.button("Filter"):
            
            st.session_state.show_data = not st.session_state.show_data


        if st.session_state.show_data:

            if filter1=="None" and filter2=="None":
                st.markdown("FULL DATASET:")
                df["Date"]=pd.to_datetime(df["Date"])
                filtered_data=df
                st.dataframe(df)

            elif filter1=="None" and filter2=="Max":
                fil_data=pd.DataFrame(df[["Date","High"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="None" and filter2=="Min":
                fil_data=pd.DataFrame(df[["Date","Low"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="None" and filter2=="Close":
                fil_data=pd.DataFrame(df[["Date","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="None" and filter2=="Open":
                fil_data=pd.DataFrame(df[["Date","Open"]])
                filtered_data=fil_data
                st.dataframe(fil_data)
            
            if filter1=="Date" and filter2=="None":
                fil_data=pd.DataFrame(df[["Date","Open","High","Low","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Date" and filter2=="Max":
                fil_data=pd.DataFrame(df[["Date","High"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Date" and filter2=="Min":
                fil_data=pd.DataFrame(df[["Date","Low"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Date" and filter2=="Close":
                fil_data=pd.DataFrame(df[["Date","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Date" and filter2=="Open":
                fil_data=pd.DataFrame(df[["Date","Open"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            if filter1=="Month" and filter2=="None":
                fil_data=pd.DataFrame(df[["Date","Open","High","Low","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Month" and filter2=="Max":
                fil_data=pd.DataFrame(df[["Month","High"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Month" and filter2=="Min":
                fil_data=pd.DataFrame(df[["Month","Low"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Month" and filter2=="Close":
                fil_data=pd.DataFrame(df[["Month","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Month" and filter2=="Open":
                fil_data=pd.DataFrame(df[["Month","Open"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            if filter1=="Year" and filter2=="None":
                fil_data=pd.DataFrame(df[["Date","Open","High","Low","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Year" and filter2=="Max":
                fil_data=pd.DataFrame(df[["Year","High"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Year" and filter2=="Min":
                fil_data=pd.DataFrame(df[["Year","Low"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Year" and filter2=="Close":
                fil_data=pd.DataFrame(df[["Year","Close"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

            elif filter1=="Year" and filter2=="Open":
                fil_data=pd.DataFrame(df[["Year","Open"]])
                filtered_data=fil_data
                st.dataframe(fil_data)

        st.subheader("Graphical Representation") 
        chart2=st.selectbox("Select Chart Type ",["Line Chart","Bar Chart","Histogram"])

        if chart2=="Line Chart":
            if filter1=="Date":
                if filter2=="None":
                    st.line_chart(df["Close"])
                elif filter2=="Open":
                    st.line_chart(df["Open"])
                elif filter2=="Max":
                    st.line_chart(df["High"])
                elif filter2=="Min":
                    st.line_chart(df["Low"])
                elif filter2=="Close":
                    st.line_chart(df["Close"])
            
            elif filter1=="Month":
                if filter2=="None":
                    st.line_chart(df["Close"])
                elif filter2=="Open":
                    st.line_chart(df["Open"])
                elif filter2=="Max":
                    st.line_chart(df["High"])
                elif filter2=="Min":
                    st.line_chart(df["Low"])
                elif filter2=="Close":
                    st.line_chart(df["Close"])

            elif filter1=="Month":
                if filter2=="None":
                    st.line_chart(df["Close"])
                elif filter2=="Open":
                    st.line_chart(df["Open"])
                elif filter2=="Max":
                    st.line_chart(df["High"])
                elif filter2=="Min":
                    st.line_chart(df["Low"])
                elif filter2=="Close":
                    st.line_chart(df["Close"])
        

        if chart2=="Bar Chart":
            if filter1=="Date":
                if filter2=="None":
                    st.bar_chart(df["Close"])
                elif filter2=="Open":
                    st.bar_chart(df["Open"])
                elif filter2=="Max":
                    st.bar_chart(df["High"])
                elif filter2=="Min":
                    st.bar_chart(df["Low"])
                elif filter2=="Close":
                    st.bar_chart(df["Close"])
            
            elif filter1=="Month":
                if filter2=="None":
                    st.bar_chart(df["Close"])
                elif filter2=="Open":
                    st.bar_chart(df["Open"])
                elif filter2=="Max":
                    st.bar_chart(df["High"])
                elif filter2=="Min":
                    st.bar_chart(df["Low"])
                elif filter2=="Close":
                    st.bar_chart(df["Close"])

            elif filter1=="Month":
                if filter2=="None":
                    st.bar_chart(df["Close"])
                elif filter2=="Open":
                    st.bar_chart(df["Open"])
                elif filter2=="Max":
                    st.bar_chart(df["High"])
                elif filter2=="Min":
                    st.bar_chart(df["Low"])
                elif filter2=="Close":
                    st.bar_chart(df["Close"])

        if chart2=="Histogram":
            if filter1=="Date":
                if filter2=="None":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Close"],bins=50)
                elif filter2=="Open":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Open"],bins=50)
                elif filter2=="Max":
                    fig1,ax=plt.subplots()
                    ax.hist(df["High"],bins=50)
                elif filter2=="Min":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Low"],bins=50)
                elif filter2=="Close":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Close"],bins=50)
                st.pyplot(fig1)
            
            elif filter1=="Month":
                if filter2=="None":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Close"],bins=50)
                elif filter2=="Open":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Open"],bins=50)
                elif filter2=="Max":
                    fig1,ax=plt.subplots()
                    ax.hist(df["High"],bins=50)
                elif filter2=="Min":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Low"],bins=50)
                elif filter2=="Close":
                    fig1,ax=plt.subplots()
                    ax.hist(df["Close"],bins=50)
                st.pyplot(fig1)

            elif filter1=="Year":
                if filter2=="None":
                    fig1,ax=plt.subplots()
                    ax.hist2d(df["Close"],bins=50)
                elif filter2=="Open":
                    fig1,ax=plt.subplots()
                    ax.hist2d(df["Open"],bins=50)
                elif filter2=="Max":
                    fig1,ax=plt.subplots()
                    ax.hist2d(df["High"],bins=50)
                elif filter2=="Min":
                    fig1,ax=plt.subplots()
                    ax.hist2d(df["Low"],bins=50)
                elif filter2=="Close":
                    fig1,ax=plt.subplots()
                    ax.hist2d(df["Close"],bins=50)
                st.pyplot(fig1)
            
        st.info("To download the data click the below button")
        download1=filtered_data.to_csv(index=False).encode('utf-8')
        st.download_button(" Download Data",
                           download1,
                           "Filtered_Data.CSV"
                           "text/csv")
                


else:
    st.error("Upload the file")