# --- BLOCK 1: The Data (Variables, Dictionaries, and Lists) ---
client_request = {
    "project_name": "Bakery Website Redesign",
    "client": "Sweet Treats Bakery",
    "budget": 5000,
    "requirements": [
        {"id": "REQ-1", "feature": "Mobile-friendly design", "can_we_do_it": True},
        {"id": "REQ-2", "feature": "Online shopping cart", "can_we_do_it": True},
        {"id": "REQ-3", "feature": "Custom drone delivery system", "can_we_do_it": False},
        {"id": "REQ-4", "feature": "Contact us form", "can_we_do_it": True}
    ]
}

# --- BLOCK 2: The Function (Defining the action) ---
def analyze_project(project_data):
    print(f"--- Analyzing Request for: {project_data.get('project_name')} ---")
    
    # Grab the list of requirements from the data
    req_list = project_data.get("requirements")
    
    # Set up some empty counters to keep track of our score
    approved_count = 0
    rejected_count = 0
    
    # --- BLOCK 3: The Loop (Going through the list) ---
    for req in req_list:
        
        # Extract the specific details for the current item we are looking at
        req_id = req.get("id")
        feature_name = req.get("feature")
        can_do = req.get("can_we_do_it")
        
        # --- BLOCK 4: The Logic (Making a decision) ---
        if can_do:
            print(f"✅ YES: We can build the '{feature_name}' ({req_id})")
            approved_count += 1
        else:
            print(f"❌ NO: We cannot build the '{feature_name}' ({req_id})")
            rejected_count += 1
            
    print(f"Final Count: We can do {approved_count} things. We can't do {rejected_count} things.")
    
    # Send a final summary back to whoever asked for it
    return {"approved": approved_count, "rejected": rejected_count}

# --- BLOCK 5: Running the code ---
final_summary = analyze_project(client_request)