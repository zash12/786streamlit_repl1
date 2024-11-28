import streamlit as st
import io
import sys

# Initialize session state for context and history
if "context" not in st.session_state:
    st.session_state.context = {}  # Persistent variables and functions
if "history" not in st.session_state:
    st.session_state.history = []  # Command history
if "output" not in st.session_state:
    st.session_state.output = ""  # Latest result/output

st.title("Python REPL in Streamlit")
st.write("A simple Python REPL (Read-Eval-Print Loop) built with Streamlit.")

# Layout: Create two columns: one for the code input, and one for command history
col1, col2 = st.columns([3, 2])

with col1:
    # Code input area
    code_input = st.text_area("Enter Python code:", height=300, placeholder="Type your Python code here...")

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
            
            # Handle cases where no output is generated
            if output.strip() == "":
                output = "Code executed successfully with no output."

            # Save to session state (history and output)
            st.session_state.history.append({"code": code_input, "output": output})
            st.session_state.output = output

        except Exception as e:
            # Capture and display errors
            st.session_state.output = f"Error: {e}"

        finally:
            # Restore stdout
            sys.stdout = old_stdout

        # Display the latest output in a results text area
        st.text_area("Results:", value=st.session_state.output, height=300, disabled=True)

with col2:
    # Command History Section
    with st.expander("Command History"):
        if st.session_state.history:
            for entry in st.session_state.history:
                st.code(f">>> {entry['code']}")
                st.text(entry['output'])

    # Clear History Button
    if st.button("Clear History"):
        st.session_state.history = []
        st.session_state.context = {}
        st.session_state.output = ""
        st.success("History and context cleared!")

