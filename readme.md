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