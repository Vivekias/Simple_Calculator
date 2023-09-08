import streamlit as st
import pandas as pd

def main():
    st.header('Simple Calculator')
    st.image('cal.png')
    st.info('Do mathematics caluculation which makes your work faster')
    st.caption('Select Your Operation Which You Want To Apply: ')
    df={'Operation':['Addition','Substraction','Multiply','Divide','Square','Square-root']}
    opr=st.selectbox('Operations',pd.DataFrame(df))
    if opr=='Addition' or opr=='Substraction' or opr=='Multiply' or opr=='Divide':
        num1=st.number_input("Enter your first number: ",0)
        num2=st.number_input("Enter your second number: ",0)
    else:
        num3=st.number_input("Enter your number: ",0)
    ok=st.button('Apply Operation')
    if ok:
        if opr=='Addition':
            result=num1+num2
            st.success(f'Sum of {num1} & {num2} is = {result}')
        elif opr=='Substraction':
            result=num1-num2
            st.success(f'Substraction of {num1} & {num2} is = {result}')
        elif opr=='Multiply':
            result=num1*num2
            st.success(f'Multiplication of {num1} & {num2} is = {result}')
        elif opr=='Divide':
            result=num1/num2
            st.success(f'Division of {num1} & {num2} is = {result}')
        elif opr=='Square':
            result=num3**2
            st.success(f'Square of {num3} is = {result}')
        else:
            result=num3**0.5
            st.success(f'Square-root of {num3} is = {result}')
        st.caption('Thanks For Using!')
        st.caption('Created by Vivek Kumar Singh')
        st.balloons()

if __name__=='__main__':
    main()
