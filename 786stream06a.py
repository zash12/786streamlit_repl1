import streamlit as st
import io
import sys

st.title("Python REPL in Streamlit")
st.write("A simple Python REPL (Read-Eval-Print Loop) built with Streamlit.")

# Code input area
code_input = st.text_area("Enter Python code:", height=150, placeholder="Type your Python code here...")

# Button to execute the code
if st.button("Run Code"):
    # Redirect stdout to capture print() outputs
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # Execute the user-provided code
        exec(code_input)

        # Capture the output from the executed code
        output = sys.stdout.getvalue()
        
        # Check if the last expression has a return value (for function calls, etc.)
        if output.strip() == "":
            output = "Code executed successfully with no output."
        
        # Display the captured output
        st.text_area("Results:", value=output, height=150, disabled=True)
        
    except Exception as e:
        # Capture and display errors
        st.text_area("Results:", value=f"Error: {e}", height=150, disabled=True)
    finally:
        # Restore stdout
        sys.stdout = old_stdout
