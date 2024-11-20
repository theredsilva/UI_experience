import streamlit as st


st.text('stefano ci manchi a lezione')

def somma(num1: float, num2: float) -> float:
    a = num1 + num2
    return a 

def main():
    st.text('ciao questo front-end funziona')
    #slider
    num1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 2)
    num2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 3)
    r = somma(num1,num2)

    st.write('La somma dei due lati è:', r)

if __name__ == '__main__':
    main()


