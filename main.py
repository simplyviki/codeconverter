import os
import subprocess

import streamlit as st
from dotenv import load_dotenv
import openai

def main():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    st.title("Code Conversion App")

    source_language = st.selectbox("Source Language", ["SAS", "Python", "Java", "C#"])
    destination_language = st.selectbox("Destination Language", ["Python", "SAS", "Java", "C#"])

    code = st.text_area("Enter the code to be converted:", max_chars=800)
    print(f'Input code: {code}')

    if st.button("Convert Code"):
        with st.spinner("Converting code..."):
            converted_code = convert_code(code, source_language, destination_language)
            if converted_code:
                st.success("Code conversion completed.")

                st.subheader("Converted Code:")
                st.code(converted_code, language=destination_language)

                st.subheader("Generate Documentation:")
                generate_documentation(converted_code, destination_language)

                st.subheader("Generate Unit Tests:")
                generate_unit_tests(converted_code, destination_language)

                st.subheader("Run and Compare:")
                run_and_compare(code, converted_code, source_language, destination_language)

def convert_code(code, source_language, destination_language):
    prompt = f"Translate the following {source_language} code to {destination_language}:\n\n{code}\n\nConverted code:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.3,
        n=1,
        stop=None,
    )
    print(f'convert_code response is:{str(response)}')
    converted_code = response.choices[0].text.strip()
    return converted_code

def generate_documentation(converted_code, destination_language):
    if not converted_code:
        st.warning("No conversion available. Convert the code first.")
        return

    documentation_prompt = f"Generate documentation for the following {destination_language} code:\n\n{converted_code}\n\nDocumentation:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=documentation_prompt,
        max_tokens=300,
        temperature=0.3,
        n=1,
        stop=None,
    )
    documentation = response.choices[0].text.strip()
    if documentation:
        st.subheader("Documentation:")
        st.code(documentation, language="markdown")
    else:
        st.warning("No documentation available.")

def generate_unit_tests(converted_code, destination_language):
    if not converted_code:
        st.warning("No conversion available. Convert the code first.")
        return

    tests_prompt = f"Generate unit tests for the following {destination_language} code:\n\n{converted_code}\n\nUnit Tests:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=tests_prompt,
        max_tokens=300,
        temperature=0.3,
        n=1,
        stop=None,
    )
    unit_tests = response.choices[0].text.strip()
    if unit_tests:
        st.subheader("Unit Tests:")
        st.code(unit_tests, language=destination_language)
    else:
        st.warning("No unit tests available.")

def run_and_compare(input_code, converted_code, source_language, destination_language):
    input_output = execute_code(input_code, source_language)
    converted_output = execute_code(converted_code, destination_language)

    st.subheader("Input Code:")
    st.code(input_code)

    st.subheader("Input Code Output:")
    st.code(input_output, language="")

    st.subheader("Converted Code:")
    st.code(converted_code, language=destination_language)

    st.subheader("Converted Code Output:")
    st.code(converted_output, language="")

    if input_output is not None and converted_output is not None:
        if input_output.strip() == converted_output.strip():
            st.write("Output Matched: The output of the input and converted code is the same.")
        else:
            st.write("Output Mismatch: The output of the input and converted code is different.")


def execute_code(code, language):
    try:
        output = ""
        if language == "Python":
            # Redirect print statements to capture the output
            exec_globals = {"__output__": ""}
            exec(code, exec_globals)
            output += str(exec_globals.get("__output__", ""))
        elif language == "Java":
            # Write the Java code to a temporary file
            java_file = "temp.java"
            with open(java_file, "w") as file:
                file.write(code)

            # Compile and run the Java code
            class_name = "Temp"
            subprocess.Popen(["javac", java_file]).wait()
            output = subprocess.Popen(["java", class_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode()

            # Remove the temporary Java file
            os.remove(java_file)
        elif language == "C#":
            # Write the C# code to a temporary file
            csharp_file = "temp.cs"
            with open(csharp_file, "w") as file:
                file.write(code)

            # Compile and run the C# code
            process = subprocess.Popen(["dotnet", "run", "-p", csharp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = process.communicate()[0].decode()

            # Remove the temporary C# file
            os.remove(csharp_file)

        return output.strip()
    except Exception as e:
        st.write("Error occurred while running the code:", str(e))
        return None

if __name__ == "__main__":
    main()
