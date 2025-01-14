import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Path to your JSON credentials file
CREDS_FILE = 'gen-lang-client-0842611531-ec48614ae819.json'

def connect_to_sheets():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    return client

def get_sheet(client, sheet_url):
    # Open the spreadsheet
    sheet = client.open_by_url(sheet_url)
    return sheet

def process_goals_data(sheet):
    """Process Goals worksheet data into structured format"""
    try:
        worksheet = sheet.worksheet("Goals")
        print(f"\nProcessing Goals worksheet: {worksheet.title}")
        
        # Get first 15 rows of data
        data = worksheet.get_values('A1:Z15')
        print(f"\nRaw data preview (rows 1-15):")
        for i, row in enumerate(data):
            print(f"Row {i+1}: {row}")
            
        # Initialize structured data
        goals_data = {
            'Goals': [],
            'System': [],
            'Lens': [],
            'Roadmap': [],
            'First Steps': [],
            'Completed': []
        }
        
        current_section = None
        for row in data:
            if not any(row):  # Skip empty rows
                continue
                
            # Check for section headers
            header = row[0].strip()
            if header == 'Goals':
                current_section = 'Goals'
            elif header == 'System':
                current_section = 'System'
            elif header == 'Lens':
                current_section = 'Lens'
            elif header == 'Roadmap':
                current_section = 'Roadmap'
            elif header == 'First Step':
                current_section = 'First Steps'
            elif header == 'Completed':
                current_section = 'Completed'
                
            # Add content to appropriate section
            if current_section and row[0].strip():
                # Include all non-empty columns in details
                details = ' | '.join([x.strip() for x in row if x.strip()])
                goals_data[current_section].append({
                    'label': row[0].strip(),
                    'details': details
                })
        
        return goals_data
        
    except Exception as e:
        print(f"Error processing worksheet: {str(e)}")
        return None

if __name__ == "__main__":
    client = connect_to_sheets()
    sheet = get_sheet(client, "https://docs.google.com/spreadsheets/d/13DzZ8PHwYto4amTX25App7EZ6K0w_6i7IJWod_wHbnY/edit")
    
    goals_data = process_goals_data(sheet)
    if goals_data:
        print("\nSuccessfully processed goals data")
        # Write processed data to file
        with open('goals_data.txt', 'w') as f:
            for section, items in goals_data.items():
                if items:
                    f.write(f"{section}:\n")
                    for item in items:
                        f.write(f"- {item['label']}: {item['details']}\n")
                    f.write("\n")
        print("Goals data written to goals_data.txt")
    else:
        print("\nFailed to process spreadsheet data")