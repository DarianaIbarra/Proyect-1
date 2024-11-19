# In order to extract SNP Data, we're going to need to follow three different codes. The overall steps are:

# 1. Data extraction from python
## The program will need to follow the template (.../Resources/Template.csv) in order to work. 
## We'll extract the data from that and form a new .csv and merge it with the RENTREZ Template
## Once we have the RENTREZ template, we can move on to the R code.

# 2. RENTREZ and NCBI Extraction
## We'll form a loop for RENTREZ and use it to obtain each line of data that we need for the
## RENTREZ.csv file. Once we obtain all the information from RENTREZ and output it into a .csv file

# 3. Python 2: Electric boogaloo
## Once we have our RENTREZ file, we jump back to our next bit of coding. We're actually going to
## do three different things with that data:

###### 3(a). NCBI API
####### We'll jump back to our python script to use the NCBI Datasets v2 REST API
####### https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/data-reports/gene/

###### 3(b). STRING ID API
####### We'll filter the SNPs by their Functional Consequence Class (FXN) and use the UniProtKB 
####### STRING ID ( https://rest.uniprot.org/docs/?urls.primaryName=idmapping#/uniprotkb  )
####### Once we get the STRING ID, we'll use pandas to get the unique ID and generate another .csv
####### file. 

###### 3(c). GeneHancer
####### Using our RENTREZ file, we'll obtain the SNP ID, Chromosome position and ID of each polymorphism. 
####### Then we'll export a .bed file and BOOM: bed intersect baby!