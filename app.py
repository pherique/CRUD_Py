import streamlit as st;

st.title("Cadastro de Clientes");

with st.form(key="include_cliente"):
   input_name = st.text_input(label= "Nome do Cliente");
   input_email = st.text_input(label= "Email do Cliente");
   input_telefone = st.text_input(label= "Telefone do Cliente");
   input_age = st.number_input(label= "Idade do Cliente:", format="%d", min_value=0, max_value=120, step=1); 
   input_occupation = st.selectbox(label="Ocupação do Cliente", options=["Estudante", "Empregado", "Autônomo", "Aposentado"]); 
   input_button_submit = st.form_submit_button(label="Cadastrar Cliente");
   
if input_button_submit:
   st.write(f'Nome:{input_name}');
   st.write(f'Email:{input_email}');
   st.write(f'Telefone:{input_telefone}');
   st.write(f'Idade:{input_age}');
   st.write(f'Ocupação:{input_occupation}');