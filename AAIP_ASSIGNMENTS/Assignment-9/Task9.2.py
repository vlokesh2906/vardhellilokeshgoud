# Define a class to represent a student from SRU
class sru_student:
    # Constructor method to initialize student attributes
    def __init__(self, name, roll_no, hostel_status):
        # Store the student's name
        self.name = name
        # Store the student's roll number
        self.roll_no = roll_no
        # Store whether student lives in hostel (True/False)
        self.hostel_status = hostel_status
        # Initialize base fee amount in rupees
        self.fee = 50000
    
    # Method to update fee based on hostel status
    def fee_update(self):
        # Check if student is staying in hostel
        if self.hostel_status:
            # Add hostel charges to base fee
            self.fee += 15000
        else:
            # Keep base fee for day scholar students
            self.fee = self.fee
    
    # Method to print all student details
    def display_details(self):
        # Print student name
        print(f"Name: {self.name}")
        # Print student roll number
        print(f"Roll No: {self.roll_no}")
        # Print hostel status in readable format
        print(f"Hostel Status: {'Hosteler' if self.hostel_status else 'Day Scholar'}")
        # Print total fee amount
        print(f"Total Fee: Rs. {self.fee}")


# Create first student object who is a hosteler
student1 = sru_student("Vinay", "A001", True)
# Update fee for first student
student1.fee_update()
# Display first student's details
student1.display_details()

# Print separator for readability
print("\n" + "="*40 + "\n")

# Create second student object who is a day scholar
student2 = sru_student("Vyshu", "A002", False)
# Update fee for second student
student2.fee_update()
# Display second student's details
student2.display_details()
