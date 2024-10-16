import csv
import webbrowser

# File paths
csv_file = 'recipients.csv'  # Path to your CSV file with email and first names
body_template_file = 'sampletemplate.txt'  # Path to your text file with the email body

# Subject of the email
subject = 'Your Subject Goes here'

# Load the email body template
with open(body_template_file, 'r') as file:
    body_template = file.read()

# Function to create a mailto link
def generate_mailto_link(to_email, first_name, body):
    # Customize the email body with the first name
    personalized_body = body.replace("[Name]", first_name)

    # URL-encode subject and body for use in the mailto link
    subject_encoded = subject.replace(" ", "%20")
    body_encoded = personalized_body.replace("\n", "%0A").replace(" ", "%20")

    # Create the mailto link
    mailto_link = f"mailto:{to_email}?subject={subject_encoded}&body={body_encoded}&cc=ccaddress@email.com"
    
    # Open the default mail client with the mailto link
    webbrowser.open(mailto_link)

# Read the CSV file and create mailto links
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['Email']
        first_name = row['Name']
        generate_mailto_link(email, first_name, body_template)

        # Wait for user input to continue
        input("Press Enter to move to the next entry...")
