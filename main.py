# Main module or module 3: For displaying the interface to user and ask him his symptoms and give results
import mod1 
import mod2 # imported both of these modules as we will need this in this file to carry out there respective functions.

def show_symptoms(): #this will display all the symptoms to user

    symptoms = mod2.get_symptoms() 
    print()
    print("List of Symptoms Available")
    print()

    k=1
    for x in symptoms:
        print(f'{k}. {x}')
        k = k + 1
    print()
    return symptoms

def show_results(results): #This will show predicted deseases based on the data

    check_results = []
    for result in results:
        if result.get('matched symptom') and len(result['matched symptom']) > 0:
            check_results.append(result)

    if len(check_results)== 0: #This is if user doesnt select any symptom(For error handling)
        print()
        print('\Error: Please enter valid number for symptom')
        return
    
    print()
    print("Predicted Results")
    
    j = 1
    for result in check_results:
        disease_name = result["Disease"]

        disease_details = mod1.disease_database.get(disease_name, {})
        description = disease_details.get("description")
        
        print(f'{j}. Disease: {disease_name}')
        print(f'   Description: {description}')
        print()
        j = j + 1
        
    print()
    print('NOTE: THIS IS FOR EDUCATIONAL PURSPOSE ONLY. \nAlways consult your healthcare provider')
    print()

def main():
    print()
    print("Disease Prediction System")
    print()
    print("Welcome! This system predicts possible conditions.")
    
    while True:
        all_symptoms= show_symptoms()
        
        print('Enter symptoms separated by commas (e.g., 2,7,14).')
        print()
        user_input = input('Enter the numbers assigned to your symptoms: ')
        
        selected_symptom= [] 
        
        for item in user_input.split(','):
            item = item.strip()
            if not item:
                continue
            
            numb = int(item)
            
            if numb >= 1 and numb <= len(all_symptoms): # This is to check if user enterd valid number and not more than provided.
                symptom = all_symptoms[numb - 1]
                selected_symptom.append(symptom)
        
        results = mod2.pred_dis(selected_symptom)
        show_results(results)

        print()
        choose = input('Do you want to check for another symptoms? (yes/no): ') #this portion i added so that user have option if they want to run programm more and want to exit.
        if choose!= 'yes':
            print()
            print('Thank you for using the system!')
            break
        print()
main()