#Module 2: Collects the symptoms and matches it with the database from module 1, and predicts the disease by matching it from the same database.

import mod1 #because we need to use database

def get_symptoms():
    collected_symptoms=  [] # i am creating this empty list to store the symptoms, and currently it is empty.
    
    for dis_name,dis_details in mod1.disease_database.items():
        symptoms=dis_details['symptoms']
        for x in symptoms:
            if x not in collected_symptoms:
                collected_symptoms.append(x)
    collected_symptoms.sort()
    return collected_symptoms

def pred_dis(user_input):
    inputs_got=[] # we are creating an empty list here as well for the same reason, i.e for storage

    for dis_name, dis_details in mod1.disease_database.items():
        dis_sympt=dis_details['symptoms']
        matching_sympt=[]
        for x in user_input:
            if x in dis_sympt:
                matching_sympt.append(x)
    
        inputs_got.append({
            'Disease': dis_name,
            'matched symptom':matching_sympt,
 })
    return(inputs_got)