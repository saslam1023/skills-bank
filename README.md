# **SkillsBank**

#### **Video Demo**  
[Video Demo](skillsbank.slammin-design.co.uk/demo/)

#### **Live Demo**  
[Live Demo](skillsbank.slammin-design.co.uk/)

---

### **Description** 
We learn in many ways, but we don't always acknowledge those skills, realise how much we know, or know how to show or share it.

SkillsBank is the platform that lets you save and track your skills journey—an investment in yourself. It shows your growth from novice to master, celebrates your achievements, and reminds you of how much you already know.

By organising your skills and progress in one place, SkillsBank solves the challenge of staying aware of your growth and makes it easier to highlight your accomplishments.

It helps you stay focused on bigger learning goals like courses, training, and career development, keeping you on track and motivated.


### **Key Features**  
- **Track Your Skills:** Record any skill, from hobbies to professional expertise.   
- **Anonymous Public Profiles:** Share your expertise without revealing personal details.  
- **Skill Discovery:** Find others with skills you're interested in and explore new learning paths.  

SkillsBank helps you understand what you enjoy, where your strengths are, and how proficient you are in different areas—you might even discover something new about yourself!

---

## **Installation**  
To run SkillsBank locally, follow these steps:

### **1. Clone the Repository**  
```bash
git clone https://github.com/saslam1023/SkillsBank.git
cd SkillsBank
```


### **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate 
```

On Windows use:
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

Create a `.env` file in the root directory and add the necessary configurations:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
MAIL_SERVER=your_mail_server
MAIL_PORT=587
MAIL_USERNAME=your_mail_username
MAIL_PASSWORD=your_mail_password
MAIL_DEFAULT_EMAIL=your_default_email
MAIL_DEFAULT_SENDER_NAME=your_sender_name
MAIL_DEFAULT_SENDER=your_sender_email
MAIL_USE_TLS=True
BRAND=SkillsBank
EMAIL_CONTACT=your_email_contact

```
**Ensure .env is added to .gitignore** to avoid accidentally committing your sensitive data to version control.

### **5. Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser (Optional, for Admin Access)**

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### **7. Run the Development Server**

```bash
python manage.py runserver
```

By default, the application will be accessible at:

```
http://127.0.0.1:8000/
```

---

## **Usage**  
Once installed, SkillsBank allows you to:

1. **Create an Account (or use anonymously to search and view profiles)**  
2. **Add and Organise Your Skills** into categories   
3. **Explore and Connect** with others through shared skills  
5. **Visualise Your Growth** over time  

_ _

---

## **Files and Structure**  
- `views.py` - Backend logic, handling requests and rendering responses
- `urls.py` - Mapping urls to corresponding views, defining routes for app
- `models.py` - Defining database structure using Django’s ORM (Object-Relational Mapping)
- `forms.py` - Managing Django forms, handling user input validation and processing
- `admin.py` - Registering models with Django’s admin panel
- `settings.py` - Setting database configuration, installed apps, email configuration, and security settings
- `.env` - Securely saving passwords and database credentials required for app
- `.gitignore` - Excluding sensitive files from being tracked by version control
- `static/` - Frontend assets (CSS, JavaScript)  
- `templates/` - HTML templates used in app 
- `README.md` - Documentation  

---

## **Design Decisions**  
- **Tech Stack:** Built with Django for a modern, scalable system.  
- **Data Storage:** User accounts and Skills data are stored securely with PostgreSQL.  
- **User Privacy:** Anonymity is prioritised, allowing users to share only what they choose.  
- **Modular Structure:** Designed to easily extend functionalities in the future.  

---

## **Challenges and Future Enhancements**  
### **Challenges Faced:**  
- Implementing a flexible skill-tracking system  
- Ensuring an intuitive, simple user experience  
- Creating a clear and consistent user interface
- Authentication system and emails to users
- Separating public and personal profiles

### **Future Enhancements:**  
- **Growth Visualisation:** - See your progress from beginner to expert.  
- **Achievement Recognition:** - Celebrate milestones in your learning journey. 
- **Detailed User Profiles:** - Detailed skills dashboard with examples.
- **AI Skill Suggestions** - Recommend next skills based on your interests  
- **Community Learning** - Connect with mentors and learners  

---

## **Contributing**  
If you would like to contribute to this project:  
- Fork this repository  
- Create a feature branch (`git checkout -b feature-name`)  
- Commit changes and open a pull request  

---

## **Acknowledgments**  
- ChatGPT for some code enhancements and refinement/clarity of text content 
- StackOverflow for resolution of technical issues with PostgreSQL
- Family and friends for testing the app
- Thanks to CS50  


---
