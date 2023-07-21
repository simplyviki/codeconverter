## How to Run the Application

Once you are in the environment with all the dependencies and packages, you need to provide your own OPENAI API KEY to interact with the LLM.

Create a new `.env` file and put the OPENAI API KEY like this:

OPENAI_API_KEY=<put your OPENAI API KEY HERE>

Command to run the application: `streamlit run main.py`

## Sample SAS Code for Conversion

```sas
/* This code creates a simple data set with two variables, age and height. */

DATA simple_data;
  /* Define the variables. */
  age = 20;
  height = 72;
  
  /* Create the data set. */
RUN;

/* This code prints the data set to the console. */
PROC PRINT DATA=simple_data;
RUN;