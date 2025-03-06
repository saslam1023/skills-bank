# **SkillsBank**

#### **Video Demo**
[Video Demo](https://skillsbank.slammin-design.co.uk/demo/)

#### **Live Demo**
[Live Demo](https://skillsbank.slammin-design.co.uk/)

---

### **Description**  
We learn in many ways, but we don't always acknowledge those skills, realise how much we know, or how to show or share it.

SkillsBank is the platform that lets you save and track your skills journey — an investment in yourself. It shows your growth from novice to master, lists your achievements, and reminds you of how much you already know.

By combining your skills and progress in one place, SkillsBank solves the challenge of keeping track of your learning growth and makes it easier to highlight your accomplishments and share your unique skillset with others.

It will help to record and visualise your learning journey helping you to keep you on track and motivated.

I learned so many skills along my CS50 (and general software development) journey accumulating endless notebooks filled with all the things I learned and discovered along the way - things I didn't even plan on learning but had to, to make it to the next stage. I realised I have gained so many skills that I felt they deserved to be recognised. I also believe this would be a very useful tool for employers and job hunters.

This project is in its very early stages - still a work in progress, I am hoping to develop it further, and any advice is welcome!

We all deserve to be recognised for our unique skills - I hope SkillsBank achieves that.

### **Key Features**  
- **Track Your Skills:** Record any skill, from hobbies to professional expertise.
- **Anonymous Public Profiles:** Showcase your knowledge without exposing personal details.
- **Skill Discovery:** Find others with skills you're interested in and discover new learning paths.

SkillsBank helps you see what you enjoy, where your strengths are, and how talented you are across a range of things — you might discover a few new things about yourself! 

---

## **Installation**
To run SkillsBank on your machine locally:

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

Create a `.env` file in the root directory and add necessary configurations:

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
EMAIL_DEFAULT_SENDER=your_sender_email
MAIL_USE_TLS=True
BRAND=SkillsBank
EMAIL_CONTACT=your_email_contact

```
**Make sure .env is added to your .gitignore file** to avoid accidentally committing your sensitive data to version control.

### **5. Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser (for Admin Access)**

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### **7. Run the Development Server**

```bash
python manage.py runserver
```

The application will be accessible at the default address:

```
http://127.0.0.1:8000/
```

---

## **Usage**
After installation, SkillsBank allows you to:

1. **Register an Account (or use anonymously to search and view profiles)**
2. **Add and Organise Your Skills** into categories
3. **Explore and Connect** with others through shared skills
5. **Visualise Your Growth** over time

_

---

## **Files and Structure
- `views.py` - Backend logic, handling of request and response rendering, 
- `urls.py` - Mapping urls to views, app route definition
- `models.py` - Models for database, Profile, Skill, Category, Context
- `forms.py` - Customised Forms for Login/Registration/Forgot Password, Custom email, Simple skill form, Contact Form
- `admin.py` - Registration of models with Django admin interface
- `settings.py` - Database configuration, installed apps, email configuration, and security settings
- `.env` - Secure saving of passwords and database credentials required for app
- `.gitignore` - Exclusion of sensitive files from version control
- `static/` - Front-end files (JavaScript, CSS)
- `templates/` - HTML templates used in app
- `README.md` - Documentation

---

## **Design Decisions**
- **Tech Stack:** Built with Django as it is a scalable system with many built in features.
- **Data Storage:** User information and Skills data are stored securely with PostgreSQL.
- **User Privacy:** Anonymity is prioritised, allowing users to share only what they choose.  
- **Modular Structure:** Designed to be capable of adding functionalities with ease in the future.

---

## **Challenges and Future Enhancements**
### **Challenges Faced:**
- Having a flexible skill-tracking system
- Providing an intuitive, easy-to-use user experience
- Designing a clear and consistent user interface
- Authentication system and emails to users
- Separating public and personal profiles

### **Future Enhancements:**
- **Growth Visualisation:** - See your progress from beginner to master.
- **Achievement Recognition:** - Celebrate milestones in your learning journey. 
- **Detailed User Profiles:** - Detailed skills dashboard with examples.
- **AI Skill Suggestions** - Recommend next skills based on your interests.
- **Community Learning** - Connect with mentors and learners.

---

## **Contributing**  
If you would like to contribute to this project:  
- Fork this repository  
- Create a feature branch (`git checkout -b feature-name`)  
- Commit changes and open a pull request  

---

## **Acknowledgments**  
- ChatGPT for some code enhancements and refinement/clarity of text content
- StackOverflow in solving technical issues with PostgreSQL
- Friends and family to test the application
- Thanks to CS50 - it's been a journey!!

---
