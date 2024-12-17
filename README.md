# LinkedIn Data Extractor

This Streamlit application fetches and displays LinkedIn profile data, posts, and contact information for a given user. The data is presented in an attractive, human-readable format while also providing raw JSON details for transparency.

# For trial you can visit- https://linkedinscrape.streamlit.app/

---

## Features
- **Profile Overview**: Displays key LinkedIn profile details, including name, headline, location, industry, and profile picture.
- **Experience**: Lists the user’s work experience with details like title, company, and start year.
- **Education**: Shows education history, including school name, degree, field of study, and years attended.
- **Skills**: Highlights the user’s skills in a clean, concise format.
- **Posts Data**: Fetches and displays up to 20 posts associated with the LinkedIn user.
- **Contact Information**: Provides user contact details (if available).
- **Raw JSON**: Displays raw JSON data for profile, posts, and contact information for further analysis.

---

## Requirements
- Python 3.x
- Streamlit
- `linkedinapi_MA` library (custom LinkedIn scraping API)

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure Streamlit is installed:
   ```bash
   pip install streamlit
   ```

3. Add the `linkedinapi_MA` module to the project directory.

---

## How to Run

1. Launch the Streamlit app:
   ```bash
   streamlit run stapp.py
   ```

2. Open the Streamlit app in your browser (default: `http://localhost:8501`).

3. Input the following details:
   - **LinkedIn Email**: Your LinkedIn login email.
   - **LinkedIn Password**: Your LinkedIn password.
   - **Target Profile Username**: Public LinkedIn profile ID 

4. Click **Fetch Data** to retrieve and display the LinkedIn data.

---

## Output

### 1. Profile Overview
- **Profile Picture**: Displays the user's profile picture.
- **Name**: First and last name.
- **Headline**: User's professional headline.
- **Location**: Geographic location of the user.
- **Summary**: User's professional summary.

### 2. Experience
Lists the user's work experience with:
- **Title**: Job title.
- **Company**: Name of the company.
- **Start Date**: Year the position started.

### 3. Education
Displays educational background with:
- **School Name**: Institution name.
- **Degree**: Degree pursued.
- **Field of Study**: Field of study or specialization.
- **Years Attended**: Start and end years.

### 4. Skills
A comma-separated list of the user's listed skills.

### 5. Posts Data
Displays up to 20 recent posts made by the user.

### 6. Contact Info
Provides contact details, including:
- **Email** (if available).
- **Phone Numbers** (if available).

### 7. Raw JSON Data
Displays raw JSON responses for:
- Profile data
- Posts data
- Contact information

---

## Example Input
- **LinkedIn Email**: `example@gmail.com`
- **LinkedIn Password**: `example_password`
- **Target Profile Username**: `elonmsuassda`

---

## Example Output
The app will display:
1. Profile picture and key details.
2. Experience, education, skills, and posts data in a clean format.
3. Raw JSON data for further use or debugging.

---

## Notes
- **Privacy**: Ensure you are using a LinkedIn test account or have permission to access profile data.
- **Data Availability**: Some fields, like contact information, depend on the target profile’s privacy settings.

---

## Disclaimer
This application is for educational purposes only. Scraping LinkedIn data may violate LinkedIn's terms of service. Use responsibly.
