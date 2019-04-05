Ex description:
The Exercise:

A cancer clinic wants to understand how four antineoplastic (e.g., anti-cancer) 
drugs are being given. Drugs A and B are chemotherapy drugs (sometimes given in combination)
 and Drugs C and D are immunotherapy drugs. 
The clinic has provided us with two datasets: 
one gives diagnoses by patient and the other dataset gives treatment dates for these patients
 for the drugs of interest. None of the patients in this cohort have died to date, 
 and no data is missing.

For each question please include:

Your code
Results of your code
Your thought process or any necessary explanation for each question 
(the hiring team will review all responses)
General Questions:

Q: When presented with a new dataset or database, what steps do you generally take to
 evaluate it prior to working with it?

A: 
(1) The first thing is to see if the data has a meaningful unique index. In this case in the
Patient_Diagnosis table the patient id is one, the Patient_Treatment doesn't have one. 
(2) Search missing data points first. In this excercise I am told that there
	Is no missing data. 
(3) Assign data type for each column, category, continuous (if so which value)

 
Based on the information provided above and the attached dataset, 
what three questions would you like to understand prior to conducting any analysis of the data?
(1) What is the number of patients with each treatment
(2) what is the number of treatments per patient
(3)

Data analysis questions:

First, the clinic would like to know the distribution of cancer types across their patients.
 Please provide the clinic with this information.(# Done)
The clinic wants to know how long it takes for patients to start therapy after being diagnosed, 
which they consider to be helpful in understanding the quality of care for the patient.
 How long after being diagnosed do patients start treatment? (# almost there)
 
 
Which treatment regimens [i.e., drug(s)] do you think would be indicated
 to be used as first-line of treatment for breast cancer? 
 What about colon cancer? (For more information between first-line and second-line treatments (applicable between chemotherapy drugs as well as chemo v immuno therapies), please reference https://www.cancer.gov/publications/dictionaries/cancer-terms?cdrid=346494)
Do the patients taking Regimen A vs. Regimen B as first-line therapy for breast cancer vary in terms of duration of therapy? Please include statistical tests and visualizations, as appropriate.
Data Format

Patient_Diagnosis
patient_id - patient identifier; each patient has a unique patient_id
diagnosis_date - date of diagnosis; YYYY-MM-DD format
diagnosis_code - an ICD9CM diagnosis code (see here for more background)

diagnosis - a diagnosis description used for reporting purposes

Patient_Treatment
patient_id
treatment_date - date of treatment; YYYY-MM-DD format
drug_code - an internal drug identifier