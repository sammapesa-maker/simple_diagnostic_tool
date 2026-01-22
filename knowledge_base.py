# knowledge_base.py

# -------------------
# Symptoms (snake_case)
# -------------------
symptoms = [
    "fever", "cough", "fatigue", "headache", "sore_throat", "chest_pain",
    "nausea", "vomiting", "diarrhea", "shortness_of_breath", "muscle_aches",
    "runny_nose", "loss_of_appetite", "night_sweats", "weight_loss",
    "wheezing", "abdominal_pain", "dizziness", "skin_rash", "joint_pain",
]

# -------------------
# Findings: symptom -> findings
# -------------------
findings = {
    "fever": ["elevated_temperature"],
    "cough": ["lung_inflammation", "upper_airway_inflammation"],
    "fatigue": ["systemic_inflammation"],
    "headache": ["systemic_inflammation", "neurological_signs"],
    "sore_throat": ["upper_airway_inflammation"],
    "chest_pain": ["chest_wall_tenderness", "lung_inflammation"],
    "nausea": ["gastrointestinal_irritation"],
    "vomiting": ["gastrointestinal_irritation", "dehydration"],
    "diarrhea": ["gastrointestinal_irritation", "dehydration"],
    "shortness_of_breath": ["hypoxia", "lung_inflammation"],
    "muscle_aches": ["muscle_inflammation", "systemic_inflammation"],
    "runny_nose": ["upper_airway_inflammation"],
    "loss_of_appetite": ["systemic_inflammation", "gastrointestinal_irritation"],
    "night_sweats": ["systemic_inflammation"],
    "weight_loss": ["systemic_inflammation"],
    "wheezing": ["airway_obstruction"],
    "abdominal_pain": ["gastrointestinal_irritation"],
    "dizziness": ["neurological_signs", "hypotension"],
    "skin_rash": ["dermatological_signs"],
    "joint_pain": ["musculoskeletal_inflammation"]
}

# -------------------
# Conditions: finding -> conditions
# -------------------
conditions = {
    "elevated_temperature": ["viral_infection", "bacterial_infection"],
    "lung_inflammation": ["respiratory_infection", "pneumonitis"],
    "upper_airway_inflammation": ["respiratory_infection", "allergic_reaction"],
    "systemic_inflammation": ["inflammatory_response", "viral_infection"],
    "chest_wall_tenderness": ["musculoskeletal_condition"],
    "gastrointestinal_irritation": ["gastrointestinal_infection", "food_poisoning"],
    "dehydration": ["gastrointestinal_infection"],
    "hypoxia": ["respiratory_infection", "cardiac_condition"],
    "muscle_inflammation": ["inflammatory_response", "autoimmune_disorder"],
    "neurological_signs": ["neurological_disorder"],
    "hypotension": ["cardiac_condition", "dehydration"],
    "dermatological_signs": ["allergic_reaction", "autoimmune_disorder"],
    "airway_obstruction": ["asthma_exacerbation", "allergic_reaction"],
    "musculoskeletal_inflammation": ["rheumatoid_arthritis", "autoimmune_disorder"]
}

# -------------------
# Diseases: condition -> diseases
# -------------------
diseases = {
    "viral_infection": ["influenza", "covid_19", "dengue"],
    "bacterial_infection": ["pneumonia", "tuberculosis", "strep_throat"],
    "respiratory_infection": ["acute_bronchitis", "covid_19", "pneumonia", "whooping_cough"],
    "inflammatory_response": ["influenza", "covid_19", "lupus"],
    "gastrointestinal_infection": ["viral_gastroenteritis", "food_poisoning", "salmonella_infection"],
    "food_poisoning": ["salmonella_infection", "e_coli_infection"],
    "musculoskeletal_condition": ["muscle_strain", "fibromyalgia"],
    "pneumonitis": ["covid_19", "chemical_pneumonitis"],
    "cardiac_condition": ["congestive_heart_failure", "myocarditis"],
    "neurological_disorder": ["migraine", "meningitis"],
    "allergic_reaction": ["asthma_exacerbation", "eczema", "allergic_rhinitis"],
    "autoimmune_disorder": ["lupus", "rheumatoid_arthritis", "dermatomyositis"],
    "asthma_exacerbation": ["asthma_exacerbation"],
    "rheumatoid_arthritis": ["rheumatoid_arthritis"],
    "dermatomyositis": ["dermatomyositis"],
    "fibromyalgia": ["fibromyalgia"],
    "influenza": ["influenza"],
    "covid_19": ["covid_19"],
    "dengue": ["dengue"],
    "pneumonia": ["pneumonia"],
    "tuberculosis": ["tuberculosis"],
    "strep_throat": ["strep_throat"],
    "viral_gastroenteritis": ["viral_gastroenteritis"],
    "salmonella_infection": ["salmonella_infection"],
    "e_coli_infection": ["e_coli_infection"],
    "acute_bronchitis": ["acute_bronchitis"],
    "whooping_cough": ["whooping_cough"],
    "chemical_pneumonitis": ["chemical_pneumonitis"],
    "congestive_heart_failure": ["congestive_heart_failure"],
    "myocarditis": ["myocarditis"],
    "migraine": ["migraine"],
    "meningitis": ["meningitis"],
    "eczema": ["eczema"],
    "allergic_rhinitis": ["allergic_rhinitis"]
}