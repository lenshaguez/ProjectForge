import streamlit as st
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(page_title="ProjectForge Engineering", page_icon="⚙️", layout="wide")

# --- WHATSAPP NUMBER ---
# Replace with your actual WhatsApp number including country code (no '+')
WA_NUMBER = "919876543210"

# --- HERO SECTION ---
st.markdown("<h1 style='text-align: center; color: #001f3f;'>We Build Your Engineering Projects. You Ace Your Viva.</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #4a5568;'>Verified hardware prototypes, clean software code, and complete engineering simulations delivered on time with full documentation and 1-on-1 defense coaching.</h4>", unsafe_allow_html=True)
st.write("---")

# --- VALUE ADD ---
st.markdown("### 🏆 The Viva Defense Kit")
st.success("""
**Every project comes with our complete Viva Defense Kit:**
*   Clean, fully commented source code and schematic diagrams.
*   Comprehensive report documentation (IEEE standard format).
*   **1-on-1 live online walkthrough** explaining every line of code, formula, and component.
*   Curated list of expected external examiner viva questions with answers.
""")

# --- INTERACTIVE CATALOG ---
st.markdown("### 📚 Project Catalog")
st.info("Select your department below to explore standard baseline projects with fixed service pricing. Have your own custom idea or unique problem statement? Submit your synopsis for a customized quote—pricing scales based on output complexity and component requirements.")

with st.expander("⚙️ 1. Mechanical Engineering (Analysis & Simulation)"):
    st.markdown("""
    **CAD / Design**
    *   3D Modeling of a V6 Engine Block — ₹2,000
    *   Modeling & Motion Simulation of a Geneva Mechanism — ₹3,000
    
    **FEA / Structural**
    *   Static Structural Analysis of a Spanner/Wrench — ₹1,500
    *   Stress Analysis of a 2D Bridge Truss — ₹1,500
    *   Load Bearing & Stress Simulation of a Bicycle Frame — ₹3,000
    
    **Thermal & HVAC**
    *   Heat Transfer Analysis of a Coffee Cup — ₹1,500
    *   HVAC Cooling Load Calculation for a Standard Classroom — ₹3,500
    
    **CFD & Fluids**
    *   2D Flow Analysis Through a Pipe Bend — ₹1,800
    *   Wind Load Simulation on a High-Rise Building Model — ₹4,000
    
    **Aerodynamics**
    *   Basic Aerodynamic Drag Analysis on a Generic Car Shape — ₹3,500
    """)

with st.expander("⚡ 2. Electrical & Electronics Engineering (EEE)"):
    st.markdown("""
    **IoT & Smart Systems**
    *   Bluetooth-Controlled Room Lights (HC-05) — ₹1,500
    *   Smart Home Dashboard (NodeMCU controlling 4 Relays) — ₹3,500
    
    **Automation**
    *   Automatic Street Light Controller using LDR — ₹1,500
    *   RFID-Based Automated Boom Barrier / Gate Entry — ₹3,500
    
    **Sensors & Agriculture**
    *   Ultrasonic Water Level Indicator with Buzzer — ₹1,500
    *   IR Sensor-Based Visitor Counter for Classrooms — ₹1,500
    *   Automated Plant Watering System with Soil Moisture Sensor — ₹3,000
    
    **Power & Measurement**
    *   Simple Digital Voltmeter using Arduino — ₹1,500
    *   Prepaid Energy Meter Prototype using RFID — ₹4,000
    
    **Robotics**
    *   Basic Line Follower AGV (using 2 IR Sensors) — ₹3,500
    """)

with st.expander("📡 3. Electronics & Communication Engineering (ECE)"):
    st.markdown("""
    **Communication & Audio**
    *   PC-to-PC Chat via Bluetooth / Serial Port — ₹1,500
    *   Simple Audio Amplifier Circuit (LM386) — ₹1,500
    *   Simple Speech / Audio Transmission over Laser Pointer — ₹3,000
    
    **Sensors & Healthcare**
    *   Basic Heart Rate Monitor using Pulse Sensor — ₹1,800
    *   Temperature & Humidity LCD Display (DHT11) — ₹1,500
    *   Patient Health Monitoring System (Vitals to Web Dashboard) — ₹4,000
    
    **Automation & Security**
    *   Clapping Switch / Sound-Operated LED — ₹1,500
    *   Voice-Controlled Home Appliances via Android App — ₹3,500
    *   Laser Security Alarm System with GSM SMS Alert — ₹3,500
    
    **Robotics**
    *   Obstacle Avoiding Robot with Servo & Ultrasonic Sensor — ₹3,500
    """)

with st.expander("💻 4. Computer Science & Engineering (CSE - FinTech & Web)"):
    st.markdown("""
    **Calculators & Parsing Tools**
    *   Simple EMI & Loan Calculator Web App — ₹1,500
    *   Currency Converter using Live Exchange Rate API — ₹1,500
    *   SIP / Mutual Fund Return Calculator Dashboard — ₹1,500
    *   CSV File Bank Statement Parser & Categorizer — ₹1,500
    
    **Web Portals & Apps**
    *   Personal Daily Expense Tracker (Income vs. Expense) — ₹1,800
    *   Dummy Banking Portal (Account creation, Transfers, Passbook) — ₹4,500
    *   Live Crypto Coin Price Tracker Dashboard — ₹3,500
    *   Peer-to-Peer Split Bill & IOU Manager Web App — ₹4,000
    
    **Machine Learning for Finance**
    *   Basic Credit Card Fraud Detection (using Pre-trained ML) — ₹3,500
    *   Stock Price Trend Predictor (Moving Average Plotter) — ₹3,500
    """)

with st.expander("🏭 5. Industrial Engineering & Management (IEM)"):
    st.markdown("""
    **Operations & Inventory**
    *   Time and Motion Study Tracker using MS Excel — ₹1,200
    *   Basic Raw Material Inventory Log Dashboard (Excel/Web) — ₹1,500
    *   Simple Reorder Point Calculator & Alert System — ₹3,000
    
    **Quality & Ergonomics**
    *   Simple 5S Implementation Audit Form (Web/Forms) — ₹1,200
    *   Desk Setup Posture Checklist & Scoring App — ₹1,500
    *   Automated Pareto Chart Generator for Defects — ₹1,500
    *   Automated Statistical Process Control (SPC) Chart Dashboard — ₹3,000
    
    **Planning & Layouts**
    *   2D Plant Layout Redesign for Flow Optimization (AutoCAD) — ₹3,000
    *   Simple Delivery Route Mapper (Google Maps API + Excel) — ₹3,500
    *   Basic Gantt Chart / Project Scheduler Web App — ₹3,000
    """)

with st.expander("🤖 6. Artificial Intelligence & Machine Learning (AIML)"):
    st.markdown("""
    **ML Foundations & Classification**
    *   Iris Flower Dataset Classification Model — ₹1,500
    *   Boston House Price Prediction (Linear Regression) — ₹1,500
    *   Titanic Dataset Survival Prediction — ₹1,500
    *   Basic Spam vs. Ham SMS Classifier — ₹1,800
    
    **Computer Vision & Gestures**
    *   Real-Time Color Detection using OpenCV — ₹1,500
    *   Face Recognition-Based Student Attendance Logger — ₹3,500
    *   Hand Gesture Controlled PC Volume (OpenCV + MediaPipe) — ₹3,500
    *   Optical Character Recognition (OCR) for ID Cards — ₹3,500
    
    **NLP & Speech**
    *   Rule-Based College Query Chatbot (FAQ Bot) — ₹3,000
    *   Speech-to-Text Classroom Notes Taker — ₹3,500
    """)

with st.expander("📊 7. Cross-Disciplinary: Applied Stats & Probability"):
    st.markdown("""
    **Statistical Tools & Simulations**
    *   Virtual Coin Toss & Dice Roll Simulator with Stats — ₹1,200
    *   Student Marks Distribution & Bell Curve Generator — ₹1,200
    *   Supermarket Customer Arrival Rate Calculator — ₹1,500
    *   Simple Acceptance Sampling Calculator — ₹1,500
    *   Simple Machine Breakdown Probability Calculator — ₹2,500
    *   Bank Teller Queue Simulation (Wait Time Calculation) — ₹3,000
    
    **Financial & Sports Analytics**
    *   Compound Interest & Probability of Doubling Money — ₹1,200
    *   Cricket Player Performance Statistical Tracker — ₹2,500
    *   Stock Market Trend Visualization Dashboard (Candlesticks) — ₹3,000
    *   Temperature Prediction using Historical Moving Averages — ₹2,500
    """)

st.write("---")

# --- PRICING TIERS ---
st.markdown("### 💎 Fixed Service Packages")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("#### Course Level Project\n**₹499**")
    st.markdown("""
    * Core execution script
    * Source code with comments
    * **Includes a free 1-on-1 online session to explain every step and line of code.**
    """)

with col2:
    st.markdown("#### 3rd Year Project\n**₹2,999**")
    st.markdown("""
    * Complete prototype
    * Circuit schematic / architecture
    * Standard project summary
    * **Includes a free 1-on-1 online session to explain every step and line of code.**
    """)

with col3:
    st.markdown("#### 4th Year Project\n**₹6,999**")
    st.markdown("""
    * Advanced functional system
    * IEEE format report & PPT
    * Guide feedback revisions
    * **Includes a free 1-on-1 online session to explain every step and line of code.**
    """)

with col4:
    st.markdown("#### Capstone Project\n**₹14,999**")
    st.markdown("""
    * Industrial-grade novel project
    * Research paper writing support
    * Priority viva defense coaching
    * **Includes a free 1-on-1 online session to explain every step and line of code.**
    """)

st.write("---")

# --- LEAD CAPTURE FORM ---
st.markdown("### 📝 Request a Direct Quote")
st.write("Submit your requirements below to instantly open a WhatsApp chat with our engineering team.")

with st.form("quote_form"):
    name = st.text_input("Full Name *")
    branch = st.selectbox("Branch / Department *", ["Mechanical", "EEE", "ECE", "CSE/AIML", "IEM", "Other"])
    topic = st.text_input("Project Topic (or write 'Need Suggestions') *")
    deadline = st.text_input("Submission Deadline *")
    tier = st.selectbox("Selected Budget Tier *", ["Course Level (₹499)", "3rd Year (₹2,999)", "4th Year (₹6,999)", "Capstone (₹14,999)", "Custom Quote"])
    
    submitted = st.form_submit_button("Send to WhatsApp for Instant Quote", type="primary")
    
    if submitted:
        if name and topic and deadline:
            message = f"*NEW PROJECT INQUIRY*%0A%0A*Name:* {name}%0A*Branch:* {branch}%0A*Topic:* {topic}%0A*Deadline:* {deadline}%0A*Tier:* {tier}"
            whatsapp_url = f"https://wa.me/{WA_NUMBER}?text={message}"
            st.markdown(f"<meta http-equiv='refresh' content='0; url={whatsapp_url}'>", unsafe_allow_html=True)
            st.success("Redirecting to WhatsApp...")
        else:
            st.error("Please fill in all required fields.")