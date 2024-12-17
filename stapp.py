import streamlit as st
import json
from .linkedinapi_MA import Linkedin

# Streamlit UI
st.title("LinkedIn Data Extractor")

st.write("Display LinkedIn profile, posts, and contact information.")

# Input fields for LinkedIn credentials
email = st.text_input("Enter LinkedIn Email:")
password = st.text_input("Enter LinkedIn Password:", type="password")

# Input field for LinkedIn profile username
username = st.text_input("Enter Target Profile Username:")

if st.button("Fetch Data"):
    if email and password and username:
        st.write("Fetching data...")
        try:
            # Authenticate LinkedIn
            api = Linkedin(email, password)

            # Fetch profile data
            profile = api.get_profile(username)
            posts = api.get_profile_posts(username, post_count=20)
            contact_info = api.get_profile_contact_info(username)

            # Display profile data attractively using Markdown
            st.markdown("## 👤 Profile Overview")
            profile_picture = profile.get('displayPictureUrl', '') + profile.get('img_400_400', '')
            if profile_picture:
                st.image(profile_picture, width=150)
            st.markdown(f"""
**Name:** {profile.get('firstName', 'N/A')} {profile.get('lastName', 'N/A')}  
**Headline:** {profile.get('headline', 'N/A')}  
**Location:** {profile.get('geoLocationName', 'N/A')}  
**Industry:** {profile.get('industryName', 'N/A')}  

**Summary:**  
{profile.get('summary', 'No summary available.')}
""")

            # Display experience
            st.markdown("### 💼 Experience")
            experience = profile.get("experience", [])
            if experience:
                for exp in experience:
                    st.markdown(f"""
- **Title:** {exp.get('title', 'N/A')}  
- **Company:** {exp.get('companyName', 'N/A')}  
- **Start Date:** {exp.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A')}  
""")
            else:
                st.write("No experience details available.")

            # Display education
            st.markdown("### 🎓 Education")
            education = profile.get("education", [])
            if education:
                for edu in education:
                    st.markdown(f"""
- **School:** {edu.get('schoolName', 'N/A')}  
- **Degree:** {edu.get('degreeName', 'N/A')}  
- **Field of Study:** {edu.get('fieldOfStudy', 'N/A')}  
- **Start Year:** {edu.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A')}  
- **End Year:** {edu.get('timePeriod', {}).get('endDate', {}).get('year', 'N/A')}  
""")
            else:
                st.write("No education details available.")

            # Display skills
            st.markdown("### 🛠 Skills")
            skills = profile.get("skills", [])
            if skills:
                st.write(", ".join(skill.get("name", "") for skill in skills))
            else:
                st.write("No skills listed.")

            # Display raw JSON data
            st.markdown("### 📄 Raw Profile Data")
            st.json(profile)

            # Display posts and contact info
            st.markdown("### 📝 Posts Data")
            st.json(posts)

            st.markdown("### 📞 Contact Info")
            st.json(contact_info)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter all fields: email, password, and target username.")
