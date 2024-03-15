# import module
import streamlit as st

# Header
st.header("HEADER: MY header")

# Subheader
st.subheader("SUBHEADER: My subheader")

# Title
st.title("TITLE: Hello world !!!")

# Text
st.text("TEXT: Hello world !!!")

# Markdown
st.markdown("### My markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
