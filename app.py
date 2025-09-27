# Mental Health Detection Web Application
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
from textblob import TextBlob
import nltk
from datetime import datetime
import os

# Try to download NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('vader_lexicon', quiet=True)
except:
    pass

app = Flask(__name__)

# Load the trained model and scaler (we'll create fallback versions if files don't exist)
try:
    with open('mental_health_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    model_loaded = True
except:
    model_loaded = False
    print("Model files not found. Using fallback prediction method.")

def extract_features(text):
    """Extract various features from text for mental health analysis"""
    
    # Basic text statistics
    word_count = len(text.split())
    char_count = len(text)
    
    # Sentiment analysis using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Simple sentiment scoring (fallback for VADER)
    compound_score = polarity
    positive_score = max(0, polarity)
    negative_score = max(0, -polarity)
    neutral_score = 1 - abs(polarity)
    
    # Psychological indicators (simple keyword-based approach)
    negative_words = ['sad', 'depressed', 'hopeless', 'anxious', 'worried', 'stressed', 
                     'overwhelmed', 'tired', 'exhausted', 'lonely', 'isolated', 
                     'worthless', 'meaningless', 'difficult', 'struggle', 'can\'t cope']
    
    positive_words = ['happy', 'joy', 'excited', 'grateful', 'wonderful', 'amazing', 
                     'great', 'love', 'proud', 'optimistic', 'motivated', 'fulfilled']
    
    negative_count = sum(1 for word in negative_words if word in text.lower())
    positive_count = sum(1 for word in positive_words if word in text.lower())
    
    # Negation patterns (basic)
    negation_patterns = ['not', 'never', 'no', 'don\'t', 'can\'t', 'won\'t']
    negation_count = sum(1 for pattern in negation_patterns if pattern in text.lower())
    
    features = {
        'word_count': word_count,
        'char_count': char_count,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'compound_score': compound_score,
        'positive_score': positive_score,
        'negative_score': negative_score,
        'neutral_score': neutral_score,
        'negative_word_count': negative_count,
        'positive_word_count': positive_count,
        'negation_count': negation_count
    }
    
    return features

def simple_predict_mental_health(text):
    """Simple rule-based prediction when ML model is not available"""
    features = extract_features(text)
    
    # Simple scoring based on features
    score = 0
    
    # Sentiment-based scoring
    if features['compound_score'] < -0.5:
        score += 2
    elif features['compound_score'] < -0.1:
        score += 1
    elif features['compound_score'] > 0.5:
        score -= 1
    
    # Negative words impact
    if features['negative_word_count'] >= 3:
        score += 2
    elif features['negative_word_count'] >= 1:
        score += 1
    
    # Positive words impact
    if features['positive_word_count'] >= 2:
        score -= 1
    
    # Determine prediction
    if score >= 2:
        prediction = 2  # High concern
        confidence = 0.8
    elif score >= 1:
        prediction = 1  # Moderate concern
        confidence = 0.7
    else:
        prediction = 0  # Positive
        confidence = 0.75
    
    return prediction, confidence

def predict_mental_health(text):
    """Predict mental health status from text input"""
    try:
        # Extract features from text
        features = extract_features(text)
        
        if model_loaded:
            features_df = pd.DataFrame([features])
            features_scaled = scaler.transform(features_df)
            prediction = model.predict(features_scaled)[0]
            confidence = max(model.predict_proba(features_scaled)[0])
        else:
            prediction, confidence = simple_predict_mental_health(text)
        
        # Map prediction to labels
        labels = {0: 'Positive Mental Health', 1: 'Moderate Concern', 2: 'High Concern'}
        prediction_label = labels[prediction]
        
        # Generate recommendations
        recommendations = get_recommendations(prediction, features)
        
        # Risk level
        risk_levels = {0: 'Low', 1: 'Medium', 2: 'High'}
        risk_level = risk_levels[prediction]
        
        # Colors for UI
        colors = {0: 'success', 1: 'warning', 2: 'danger'}
        color = colors[prediction]
        
        return {
            'prediction': prediction_label,
            'risk_level': risk_level,
            'confidence': confidence,
            'features': features,
            'recommendations': recommendations,
            'color': color,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {
            'prediction': 'Error in analysis',
            'risk_level': 'Unknown',
            'confidence': 0.0,
            'features': {},
            'recommendations': ['Please try again or consult with a mental health professional.'],
            'color': 'secondary',
            'error': str(e),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def get_recommendations(prediction, features):
    """Generate personalized recommendations based on prediction and features with Indian context"""
    
    recommendations = []
    
    if prediction == 0:  # Positive mental health
        recommendations.extend([
            "🌟 Excellent! Keep up the great work maintaining your positive mental health",
            "🧘‍♀️ Continue with regular yoga and pranayama practice for sustained wellness",
            "📿 Consider incorporating daily meditation or mindfulness into your routine",
            "👥 Spend quality time with family and friends - social connections are vital",
            "🌱 Follow Ayurvedic lifestyle principles: fresh food, regular routine, adequate rest",
            "🎵 Listen to uplifting music, bhajans, or classical Indian music for emotional balance",
            "🙏 Practice gratitude daily - acknowledge the positive aspects in your life"
        ])
    
    elif prediction == 1:  # Moderate concern
        recommendations.extend([
            "🤝 Talk to trusted family members, friends, or elders about your feelings",
            "🏥 Consider visiting a nearby government hospital or PHC for mental health support",
            "🧘‍♂️ Practice daily yoga and pranayama (Anulom-Vilom, Bhramari) for stress relief",
            "🌿 Try natural remedies: Tulsi tea, Ashwagandha, or Brahmi supplements",
            "📱 Contact mental health helplines: National Mental Health Helpline 08046110007",
            "⏰ Maintain a regular daily routine - wake up early, sleep on time",
            "🍛 Eat sattvic (pure) foods: fruits, vegetables, dal, rice, avoid processed foods",
            "🎭 Engage in cultural activities, festivals, or community gatherings",
            "💭 Practice positive thinking techniques and challenge negative thoughts",
            "📝 Keep a gratitude journal - write down 3 good things daily"
        ])
        
        # Additional recommendations based on specific features
        if features.get('negative_word_count', 0) > 2:
            recommendations.append("💭 Practice the mantra 'This too shall pass' when facing negative thoughts")
        
        if features.get('compound_score', 0) < -0.3:
            recommendations.append("🙏 Focus on positive affirmations and count your blessings daily")
    
    else:  # High concern
        recommendations.extend([
            "🚨 IMPORTANT: Please immediately inform family members and seek professional help",
            "🏥 Contact nearby government medical college or AIIMS psychiatry department urgently",
            "📞 Call National Mental Health Helpline: 08046110007 (24/7 support)",
            "👨‍⚕️ Consult a psychiatrist - CBT, DBT therapy options are available in India",
            "🏘️ Visit Community Health Centre (CHC) for accessible mental health services",
            "👥 Do not isolate yourself - stay with family or friends for support",
            "🧘‍♀️ Try immediate calming techniques: deep breathing or yoga nidra",
            "🙏 Reach out to spiritual counselors or community religious leaders"
        ])
        
        # Indian crisis resources
        recommendations.extend([
            "🆘 Indian Crisis Resources - Available 24/7:",
            "📞 National Mental Health Helpline: 08046110007",
            "📞 Sneha India: 022-25521111 (Mumbai)", 
            "📞 Aasra: 022-27546669 (Mumbai)", 
            "📞 Parivarthan: 0877-23456777 (Telangana)",
            "📞 Maithri: 0484-2540530 (Kochi)",
            "📞 Roshni: 040-66202000 (Hyderabad)",
            "📞 Sumaitri: 011-23389090 (Delhi)",
            "🏥 For immediate medical emergency dial: 102"
        ])
    
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Please provide some text to analyze'}), 400
        
        if len(text) < 10:
            return jsonify({'error': 'Please provide more detailed text (at least 10 characters)'}), 400
        
        result = predict_mental_health(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)