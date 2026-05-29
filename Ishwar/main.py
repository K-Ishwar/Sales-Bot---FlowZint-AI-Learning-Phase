from models import RFPAnalysis

def process_uploaded_document():
    print("--- Starting Document Processor ---")
    
    # 2. Fake data (simulating data we got from reading a PDF)
    fake_extracted_id = "DOC-9942"
    fake_feature_list = ["User Login", "Database Backup", "Payment Gateway"]
    
    try:
        # 3. Create the object 
        print(f"Creating analysis record for {fake_extracted_id}...")
        current_rfp = RFPAnalysis(fake_extracted_id, fake_feature_list)
        
        # 4. Use the object's methods
        current_rfp.analyze()
        summary = current_rfp.get_summary()
        
        print("Success!")
        print(summary)
        
    except Exception as e:
        # 5. Error handling
        print(f"SERVER ERROR: Could not process document. Details: {e}")

if __name__ == "__main__":
    process_uploaded_document()