import streamlit as st
import os

def intro():

    st.write("# Machine Learning-Assisted Software Reuse Prediction and Analysis")
    st.sidebar.header("About")

    st.markdown(
        """
        This tool supplements RQ3 of the PhD thesis titled above.

        ### Author
        
        Matthew Yeow Yit Hang

        ### Supervisor

        - Chong Chun Yong
        - Lim Mei Kuan

        ### Features

        - Predict reuse of an existing Java GitHub project.
        - Provide suggestions on how to improve reuse.
        - Provide rankings of analysed Maven repositories based on tags.


    """
    )

intro()

if st.button('Download JAVA'):
    #os.system("wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz")
    #os.system("tar zxvf openjdk-11+28_linux-x64_bin.tar.gz")
    os.system("export JAVA_HOME=jdk-11")
    os.system("export PATH=$PATH:$JAVA_HOME/bin")
    os.system("echo $JAVA_HOME")
    os.system("echo $PATH")

	
