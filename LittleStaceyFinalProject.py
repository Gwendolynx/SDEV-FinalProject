# Final Project: Drug Information Cheatsheet
# Stacey Little
# SDEV140-10P
# Program prompts the user for a drug name and retrieves information to display

def main():
    # Get user input
    drug = input("Please enter a drug name: ")
    drug_input = str(drug)
    # using upper helps find word matches regardless of case user enters
    drug_search = drug_input.upper()

    # uses user input to display the drug being searched
    print()
    print("Thank you. Here is information regarding " + drug + ":")
    print()

    # import csv with drug information
    import csv

    # display and format the spacing of the search results header
    with open("LittleStaceyFinalProjectdata.csv", 'r') as reader:
        header_data = [(reader.readlines()[0])]
        for row in header_data:
            header = (row[0:].strip().split(","))
            print("{: <30} {: <25} {: <15}".format(*header))


    # find the user entered drug in csv file and locate information in that row
    with open("LittleStaceyFinalProjectdata.csv", 'r') as reader:
        for row in reader.readlines()[1:]:
            columns = row.strip().split(",")

    # search for drug entered in first column (generic name)
            if drug_search in columns[0]:
                search = (row.strip().split(","))
                print("{: <30} {: <25} {: <15}".format(*search))
                print('------------------------------------------------------------------------')
    
    # search for drug entered in second column (brand name) if not in first            
            elif drug_search in columns[1]:
                search2 = (row.strip().split(","))
                print("{: <30} {: <25} {: <15}".format(*search2))
                print('------------------------------------------------------------------------')
    
def restart():
    print()
    restart_input = input(f"Would you like to search again? (y/n): ").lower()
    #restart = input(f"Would you like to search again? (y/n): ").lower()
    if restart_input == "y":
        main()
        restart()

    else:
        print(f"Thank you for using our Pharmacutical Drug Program!")
        exit()
    

# run the program and loop           
main()
restart()
