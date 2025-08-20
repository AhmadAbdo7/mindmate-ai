# mindmate-ai
# MindMate – An AI-powered Early Mental Health Assistant  

Final project for the **Building AI course**  

## Summary  

MindMate is an AI assistant that helps people track their mental health through daily mood check-ins, journaling, and personalized well-being recommendations. It doesn’t replace therapy but encourages early awareness and self-care.  
*Building AI course project*  

---

## Background  

Mental health challenges such as stress, anxiety, and depression are widespread but often go unnoticed until they become severe.  

* 1 in 8 people worldwide live with a mental health condition (WHO).  
* Many avoid seeking help due to stigma or lack of awareness.  
* I’ve personally seen friends and colleagues experience burnout without realizing they needed support.  

**Why this matters:**  
Mental health is harder to detect than physical illness. Early awareness tools could empower individuals to notice changes before things worsen.  

---

## How is it used?  

* Users log daily moods and short journal entries via an app or website.  
* The AI analyzes mood trends and provides supportive feedback.  
* If prolonged low moods are detected, the app gently nudges users to seek help.  

**Example interaction:**  

Journal entry: "I feel exhausted today. Work has been overwhelming."
→ Sentiment detected: NEGATIVE (confidence 0.92)
→ Suggestion:Try a short walk or mindfulness exercise. If these feelings persist, talk to someone you trust.


This tool is for:  
* Students  
* Employees  
* Anyone who wants to monitor and improve their well-being  

---

## Data sources and AI methods  

* **Data sources:**  
  - User input (mood logs, journaling)  
  - Public datasets on mental health (e.g. WHO, open survey data)  
* **AI techniques:**  
  - Natural Language Processing (NLP) for journaling analysis  
  - Sentiment analysis to detect mood trends  
  - Anomaly detection to flag sudden changes  
  - Simple recommendation system for well-being tips  

---

## Demo Code  

See `demo.py` for a working prototype. Run with:  

```bash
pip install -r requirements.txt
python demo.py

Challenges

Not a replacement for professional therapy

Privacy concerns: handling sensitive personal data securely

Risk of bias in NLP models (cultural/language nuances)

Users may not log consistently

What next?

Add integration with wearables (heart rate, sleep)

Offer multilingual support for global reach

Collaborate with healthcare providers for referral pathways

Build anonymous community features for peer support

Acknowledgments

Inspired by mental health apps like Woebot, Wysa, and Daylio

Uses Hugging Face Transformers
