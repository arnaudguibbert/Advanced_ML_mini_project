# Description

This project aims at comparing two dimensionality reduction methods: Locally Linear Embedding and one of its variant Modified Locally Linear Embedding. The performances of these algorithms are assessed on email data set. A full description about the way the evaluation was performed is available in the report.pdf file. 

# Folder organization

The project is divided in two folders: 
 * Data folder where you will find the data set and its documentation.

 * src folder where you will find all the python files used to produce the results tackled in the report. 

 More precisely the src folder contains three python files:
 * utils.py : this file is containing all the useful functions/classes that are used to assess LLE and MLLE preformances. The prupose of each function/class is widely detailed in this file. 

 * run.py : this file is a script that will automatically reproduce the report results/graphs (some results may be slightly different as it was chosen to not use any seed). All the graphs will be stored in the figures folder and the time data performances will be stored into the data_time folder. Going through the first lines of this file will be allow you to choose some parameters for the evaluation of LLE and MLLE.  

* crop.py : it will simply crop the pdf files generated during the experiments

In addition src folder contains two subfolder:

* data : it contains all the datas acquired during the experiments. 

* figures : it contains all the figures acquired during th experiments. 

# Reproduce results

As it was tackled in the previous part, reproducing the results can be easily done by simply running the run.py file. The right parameters are already entered in the run.py file. Feel free to change them if you want. However be careful the time execution is quite high: for default parameters time execution is around 20 hours depending on your computational ressources. The terminal will print logs to give insights on the progression. 
