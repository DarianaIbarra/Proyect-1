# Before we start, remember to activate your conda environment.
## Write 'conda create --name myenv numpy pandas scipy matplotlib' into your terminal
## Then activate the environment: 'conda activate myenv'
## Remember to check that your Python interpreter is correct

# First step: Import the libraries we're going to use (PANDAS, NUMPY, MATPLOTLIB)
import pandas as pd
import numpy as np
import matplotlib as plt

# Second step: We're going to read our Resources.csv and test to see if we can see it.
SNP_file = pd.read_csv('../Resources/Template.csv')    #You should always open the Data_Extraction_Code 
                                                       #folder to have a relative path similar to this one
SNP_file.head()

# Third step: Now let's create a second dataframe (to keep from editing the original)
SNP_editable = SNP_file
SNP_editable.head()

#Fourth step: Let's merge the dataframe and use SNP ID as our merge.
# Let's read our second .csv file
Our_SNP_List = pd.read_csv('../Resources/AA_SNP_Extraction.csv')
Our_SNP_List.head()

# And...

# MERGE!
merge_data = pd.merge(Our_SNP_List, SNP_file, on="SNP ID")
merge_data.head()