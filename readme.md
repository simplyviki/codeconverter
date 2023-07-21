
## How to run the application 

__Once you are in the environment having all the dependencies and packages. 
You need to provide your own OPENAI API KEY to interact with the LLM.<br/>

create a new ".env" file and put OPENAI API KEY like below:<br/>

OPENAI_API_KEY=<put your OPENAI API KEY HERE><br/>

Command to run application: streamlit run main.py<br/>


## sample sas code for conversion<br/>

/* This code creates a simple data set with two variables, age and height. */<br/>

DATA simple_data;<br/>

/* Define the variables. */<br/>

age = 20;<br/>
height = 72;<br/>

/* Create the data set. */<br/>

RUN;<br/>

/* This code prints the data set to the console. */

PROC PRINT DATA = simple_data;<br/>
RUN;<br/>