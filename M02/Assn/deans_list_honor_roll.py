# Kezrae Shields
#deans_list_honor_roll.py
#Description: This program accepts student names and GPAs, then determines if the student qualifies 
#for the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25).

def main():
    while True:
        # Get student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()
        
        # Check if user wants to quit
        if last_name.upper() == "ZZZ":
            print("Exiting program...")
            break
        
        # Get student's first name
        first_name = input("Enter student's first name: ").strip()
        
        # Get student's GPA 
        while True:
            try:
                gpa = float(input("Enter student's GPA: "))
                if 0.0 <= gpa <= 4.0:
                    break
                else:
                    print("Error: GPA must be between 0.0 and 4.0.")
            except ValueError:
                print("Error: Please enter a valid numeric GPA.")
        
        # Check qualifications
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} did not qualify for Dean's List or Honor Roll.")
        
        print("-" * 40)  # Separator for readability

# Run the program
if __name__ == "__main__":
    main()
