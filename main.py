import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

def connect_db():
    connection = sqlite3.connect("mydb.db")
    return connection 

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS student(name text, password text, roll int primary key, branch text)')
    conn.commit()
    conn.close()

def addrecord(data):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO student(name, password,roll,branch) values (?,?,?,?)', data)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError :
        print("an error")


def view_record():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('select *from student')
    result = cur.fetchall()
    return result

def display():
    data = view_record()
    st.write(data)


def signup():
    st.title("Sign up")
    name = st.text_input("Enter Your Username")
    roll = st.number_input("Enter Your Roll Number", min_value=0, step=None)
    branch = st.selectbox("select your Branch", options=['CSE','AIML','IT','IOT','ECE','ME'])
    pswd = st.text_input("Password", type='password')
    repswd = st.text_input("Re-Enter password",type='password')
    btn = st.button("submit")

    if btn :
        if pswd != repswd :
            st.error("password do not match")
        else:

            addrecord((name,roll,branch,pswd))
            st.success("successfully registered")
        

create_table()

with st.sidebar:
    selected = option_menu('select from here', ['SignUp','Display All Record'])

if selected == "Display All Record":
    display()


signup()
