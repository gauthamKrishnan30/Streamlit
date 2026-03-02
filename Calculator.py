import streamlit as st
st.title("CALCULATOR")

menu=st.sidebar.selectbox("Select Options",["Calculator","About"])

if menu == "Calculator":
    st.header("Perform Arimethic Operations For Two Numbers!!")

    st.write(""" 
             - Addition '+'
            - Subtraction '-'
            - Multiplication '*'
            - Division '/'
            - Modulus '%'
            """)
    col1,col2,col3=st.columns(3)
    output=0
    with col1:
        num1=st.number_input("Enter your first number",step=1)
    with col2:
            operation=st.selectbox("Select Operator",["+","-","*","/","%"])
    with col3:
        num2=st.number_input("Enter your second number",step=1)
    if st.button("Calculate"):
        if operation =="+":
            output=num1+num2
            if output>0:
                st.success(output)
            elif output<0:
                st.warning(output)
            else:
                st.error("Output is Zero")
        elif operation =="-":
            output=num1-num2
            if output>0:
                st.success(output)
            elif output<0:
                st.warning(output)
            else:
                st.error("Output is Zero")
        elif operation =="*":
            output=num1*num2
            if output>0:
                st.success(output)
            elif output<0:
                st.warning(output)
            else:
                st.error("Output is Zero")
        elif operation =="/":
            if num2==0:
                st.error("Zero Division Error")
            else:
                output=num1/num2
                if output>0:
                    st.success(output)
                elif output<0:
                    st.warning(output)
                else:
                    st.error("Output is Zero")
        elif operation =="%":
            if num2==0:
                st.error("Zero Division Error")
            else:
                output=num1%num2
                if output>0:
                    st.success(output)
                elif output<0:
                    st.warning(output)
                else:
                    st.error("Output is Zero")
elif menu == "About":
    st.header(" +   -   *    /   %   ")
    st.text("It is simple calculator which takes two operands has input and performs the operations. This calculator cannot take 3 or more operands has input.")
    st.info("**NOTE**: The first number is Operand 1 and the second number is Operand 2. The result depends on the selected operator and the order of operands")
    st.image("arithmeticoperators.png",width=700)
    st.success("Display the output in green if the output value is a positive number")
    st.warning("Display the output in brwon if the output value is a negative number")
    st.error("Display the output in red if the output value is Zero or Zero division Error")
