# FitGirlsTracker API 💪🌸

A backend API built with **Django** and **Django REST Framework** for the FitGirlsTracker app.  
This project is a **capstone version** focused on **frontend-only consumption**, designed specifically for women who want a personalized and community-driven way to discover and track workouts.

---

## 🚀 Project Overview

The **FitGirlsTracker API** provides the backend for a fitness tracker application.  
It allows users to create accounts, discover expert-created workout routines, track their progress, and engage with the fitness community.

---

## 👩‍🦰 Users

There are two types of users:

1. **Normal Users**  
   - Discover workouts.  
   - Save workouts.  
   - Track their progress (completed/in-progress routines).  

2. **Experts (Certified Trainers)**  
   - Post their own workout routines.  
   - Upload a certificate to verify their expertise (required before posting).  

---

## 💪 Workouts

- Experts can post workout routines such as:  
  *“Booty Blast”*, *“Yoga for Beginners”*, or *“Arm Toning”*.  

Each workout includes:
- **Goal**: abs, booty, arms, or full-body.  
- **Difficulty**: beginner, intermediate, or advanced.  
- **Description**: a detailed explanation of the workout.  

Normal users can:
- Browse workouts.  
- Filter workouts by goal.  
- View workout details.  

---

## 📅 Progress Tracking

- Users can log workouts they’ve done.  
- Mark workouts as **completed** or **in-progress**.  
- Each user has a **history of workouts**, like a personal fitness diary.  

---

## 💬 Community Features (Social)

- Users can **like workouts** they enjoy.  
- Users can **comment under workouts** to:  
  - Ask questions.  
  - Share feedback.  
  - Encourage others.  

This makes the app feel more like a **supportive community** rather than just a tracker.  

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL (recommended) or SQLite (for dev)  
- **Auth**: Django Authentication & JWT (for API access)  

---

## 📌 Current Scope

This README covers the project **up to the Comments feature**.  
The next steps (Certificates, Admin verification, Nutrition, etc.) will be added later.  

---
