# LinkedIn Profile and Posts Extractor

This script allows you to extract profile data, posts, and contact information for specific LinkedIn users using the `linkedinapi_MA` Python package.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Usage](#usage)
4. [Output](#output)
5. [Deployment Instructions](#deployment-instructions)
6. [Notes](#notes)

---

## Overview
This script:
- Extracts LinkedIn user profiles
- Fetches posts for a user (up to a specified count)
- Retrieves contact information (when available)
- Saves all the extracted data into JSON files

---

## Features
- Extracts user profile information
- Extracts up to 20 posts per user
- Fetches contact information for LinkedIn users
- Outputs organized JSON files for easy access

---

## Usage
1. Replace the credentials in the script:
   ```python
   api = Linkedin('your-email@example.com', 'your-password')
   ```

2. Update the `users` list with LinkedIn profile IDs:
   ```python
   users = ["profile-id-1", "profile-id-2"]
   ```
   Example LinkedIn profile ID: `maytri-shah-299834275`

3. Run the script:
   ```bash
   python script_name.py
   ```
   **Note:** The required package `linkedin_api` is already included in the repository, so no additional installation is required.

---

## Output
The script generates the following files in the `../../Output/LinkedIn_Extracts/` directory:

- `lastName_profile.json`: Contains the user's profile data
- `lastName_posts.json`: Contains the user's posts (up to 20 posts)
- `lastName_contact_info.json`: Contains the user's contact information (if available)

### Example Output Directory Structure:
```
Output/
├── LinkedIn_Extracts/
   ├── Shah_profile.json
   ├── Shah_posts.json
   └── Shah_contact_info.json
```

---

## Deployment Instructions

### Step 1: Credentials Setup
- Replace the placeholder credentials with your LinkedIn login credentials:
   ```python
   api = Linkedin('your-email@example.com', 'your-password')
   ```

### Step 2: Target User Configuration
- Add the LinkedIn profile IDs of the target users in the `users` list:
   ```python
   users = ["profile-id-1", "profile-id-2"]
   ```

### Step 3: Running the Script
- Run the script in your terminal:
   ```bash
   python script_name.py
   ```

### Step 4: Verify Output
- Check the `../../Output/LinkedIn_Extracts/` folder for output JSON files.

---

## Notes
1. **Credentials Security**: Do not use your primary LinkedIn account credentials for this script. Use a separate or test account.
2. **Output Directory**: Ensure the output directory (`../../Output/LinkedIn_Extracts/`) exists before running the script, or create it dynamically:
   ```python
   import os
   os.makedirs("../../Output/LinkedIn_Extracts/", exist_ok=True)
   ```
3. **LinkedIn API Limits**: Be mindful of LinkedIn's rate limits and usage policies to avoid account restrictions.

---

## Disclaimer
This script is for educational purposes only. Scraping LinkedIn data may violate LinkedIn's terms of service. Use responsibly.
