
#How to run the application 
Once you are in the environment having all the dependencies and packages. 
You need to provide your own OPENAI API KEY to interact with the LLM.
Command: streamlit run main.py


#sample sas code for conversion

/* This code creates a simple data set with two variables, age and height. */

DATA simple_data;

/* Define the variables. */

age = 20;
height = 72;

/* Create the data set. */

RUN;

/* This code prints the data set to the console. */

PROC PRINT DATA = simple_data;
RUN;