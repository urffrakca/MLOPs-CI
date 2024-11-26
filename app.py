import streamlit as st

#  streamlit UI
st.title('power calculator')
st.write('enter a no. to calculate its square, cube and 5th power')


# get user input
n = st.number_input('Ener an integer:', value=1, step=1)

# calculate results
square = n**2
cube = n**3
fifth_power = n**5

# displaying results
st.write(f'square({n}):{square}')
st.write(f'cube({n}):{cube}')
st.write(f'5th_power({n}):{cube}')