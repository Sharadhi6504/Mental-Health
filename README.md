# MindScope AI - Mental Health Detection for Indians 🇮🇳

A comprehensive web application that uses machine learning and natural language processing to analyze text input and provide mental health insights, recommendations, and resources specifically designed for Indian users, integrating traditional healing practices with modern psychology.

## 🌟 Key Features

- **🤖 AI-Powered Analysis**: Advanced machine learning model for text-based mental health assessment
- **⚡ Real-time Processing**: Instant analysis of user input with detailed feedback
- **🎯 Personalized Recommendations**: Tailored suggestions based on analysis results with Indian cultural context
- **🔒 Privacy-First**: Text is processed in real-time and never stored on servers
- **🇮🇳 Indian Context**: Resources specifically curated for Indian healthcare system and culture
- **🕉️ Traditional Integration**: Combines modern psychology with yoga, meditation, and Ayurveda
- **🌐 Multi-language Support**: English-first with optional Hindi and regional languages
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🆘 Crisis Support**: Immediate access to Indian crisis helplines and resources

## 🚀 Live Demo

🌐 **Access the application**: [https://mental-health-mindscope.herokuapp.com](https://mental-health-mindscope.herokuapp.com) *(deployment URL)*

## 💻 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project files to your directory**

2. **Navigate to the project directory**
   ```bash
   cd c:\Users\shara\VSPython
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your web browser and go to**
   ```
   http://localhost:5000
   ```

## 🧠 How It Works

### 1. Text Analysis
- Analyzes language patterns, sentiment, and emotional indicators
- Extracts linguistic features like word count, sentiment scores, and emotional tone
- Identifies psychological indicators through keyword analysis

### 2. Machine Learning Model
- Random Forest classifier trained on synthetic mental health data
- Features include sentiment analysis, word patterns, and emotional markers
- Provides confidence scores for predictions

### 3. Classification Levels
- **Positive Mental Health**: Indicators suggest good mental wellbeing
- **Moderate Concern**: Some stress or mild concerns detected
- **High Concern**: Patterns suggest need for professional support

### 4. Personalized Recommendations
- Tailored suggestions based on analysis results
- Crisis resources for high-risk situations
- Self-care tips and professional help guidance

## 📱 Usage

1. **Enter Your Text**: Describe your thoughts, feelings, or current situation in the text area
2. **Analyze**: Click the "Analyze Mental Health" button to process your input
3. **Review Results**: View your mental health assessment with confidence scores
4. **Explore Recommendations**: Read personalized suggestions and resources
5. **Access Resources**: Browse the comprehensive mental health resource library

## 🔒 Privacy & Security

- **No Data Storage**: Your text input is processed in real-time and never stored
- **Local Processing**: Analysis happens on the server without external data sharing
- **Anonymous**: No personal information is collected or tracked
- **Secure**: Uses HTTPS and secure processing methods

## ⚠️ Important Disclaimers

### Medical Disclaimer
- This tool is for **educational and awareness purposes only**
- **NOT a substitute** for professional medical diagnosis or treatment
- **Always consult** qualified healthcare providers for mental health concerns
- **Cannot replace** therapy, counseling, or psychiatric care

### Crisis Situations - India 🇮🇳
If you're experiencing thoughts of self-harm or suicide:
- **📞 National Mental Health Helpline**: 08046110007 (Toll Free)
- **🚨 Medical Emergency**: 102 (All States)
- **💬 Sneha India (Mumbai)**: 022-25521111
- **🏥 Government Hospitals**: Visit nearest district hospital Mental Health OPD
- **💻 Online Crisis Support**: YourDOST, Wysa India

## 🇮🇳 Indian Healthcare Integration

### Government Support
- **🏥 Ayushman Bharat**: Mental health services covered
- **🏢 ESI Scheme**: Mental health coverage for employees  
- **🏥 NIMHANS**: Bangalore - National mental health institute
- **🏥 AIIMS**: Psychiatry departments in major cities

### Traditional Healing Integration
- **🕉️ Yoga & Pranayama**: Surya Namaskara, Anulom-Vilom, Bhramari
- **🧘 Meditation**: Vipassana centers, Om mantra, Gayatri mantra
- **🌿 Ayurveda**: Ashwagandha, Brahmi, Jatamansi, Tulsi
- **👨‍👩‍👧‍👦 Community Support**: Satsang, spiritual groups, family networks

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework
- **Scikit-learn**: Machine learning library
- **NLTK**: Natural language processing
- **TextBlob**: Sentiment analysis
- **Pandas/NumPy**: Data processing

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Chart.js**: Data visualization
- **jQuery**: JavaScript functionality
- **Font Awesome**: Icons

### Machine Learning
- **Random Forest Classifier**: Main prediction model
- **Feature Engineering**: Text analysis and extraction
- **Sentiment Analysis**: Emotional tone detection
- **Natural Language Processing**: Language pattern analysis

## 📊 Model Performance

The machine learning model achieves high accuracy on synthetic training data:
- **Training Accuracy**: 100%
- **Testing Accuracy**: 100%
- **Features**: 11 extracted text features
- **Classes**: 3 mental health categories

*Note: Performance on real-world data may vary. This is a demonstration system.*

## 🗂️ Project Structure

```
MindScope-AI/
├── app.py                      # Main Flask application
├── mental_health_model.pkl     # Trained ML model  
├── scaler.pkl                  # Feature scaler
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── templates/
│   ├── base.html              # Base template with Indian design
│   ├── index.html             # Main analysis page
│   ├── resources.html         # Indian mental health resources
│   └── about.html             # About page with cultural context
└── static/
    ├── css/
    │   └── animations.css     # Modern UI animations
    └── favicon.svg           # Indian-themed favicon
```

## 🧪 Development & Testing

### Running in Development Mode
```bash
python app.py
```
The application runs in debug mode by default, providing detailed error messages and auto-reload.

### Model Training
The Jupyter notebook (`Untitled-1.ipynb`) contains the complete model training pipeline:
- Data generation and preprocessing
- Feature engineering and extraction
- Model training and evaluation
- Model persistence and deployment

### Testing the API
You can test the analysis endpoint directly:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "I feel great today and excited about the future!"}' \
     http://localhost:5000/analyze
```

## 🤝 Contributing

This is a demonstration project showcasing mental health AI applications. For production use:

1. Use real clinical data (with proper permissions and ethics approval)
2. Implement comprehensive testing and validation
3. Add user authentication and session management
4. Enhance security measures
5. Conduct thorough clinical validation

## 📚 Resources

### Indian Mental Health Resources 🇮🇳
- **📞 National Mental Health Helpline**: 08046110007
- **🏥 NIMHANS Bangalore**: https://nimhans.ac.in/
- **🌐 Indian Association for Mental Health**: https://iamh.in/
- **🕉️ Art of Living**: https://www.artofliving.org/
- **💻 YourDOST**: https://yourdost.com/
- **📱 Wysa India**: https://wysa.io/

### Technical Resources
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Scikit-learn**: https://scikit-learn.org/
- **NLTK**: https://www.nltk.org/
- **Bootstrap**: https://getbootstrap.com/

## 🚀 Deployment

This project is deployed on GitHub and can be easily deployed to various platforms:

### GitHub Pages (Static Demo)
```bash
git clone https://github.com/Sharadhi6504/Mental-Health.git
cd Mental-Health
python -m http.server 8000
```

### Heroku Deployment
1. Create Heroku app
2. Connect to GitHub repository
3. Enable automatic deployments
4. Set Python buildpack

## 📄 License

This project is for educational and demonstration purposes. Please ensure proper licensing and ethical approval before using in production environments.

## 🆘 Crisis Support - India

If you're experiencing a mental health crisis:
- **🚨 Emergency**: 102 (Medical Emergency)
- **📞 Mental Health Helpline**: 08046110007
- **💬 Crisis Text Support**: Contact local NGOs via WhatsApp
- **🏥 Immediate Help**: Visit nearest government hospital Mental Health OPD

For technical support with this application, please create an issue in the [GitHub repository](https://github.com/Sharadhi6504/Mental-Health).

---

**Remember**: This tool is designed to raise awareness about mental health with Indian cultural context. Always seek professional help for mental health concerns. Your mental health matters, and help is always available. 🧠💚🇮🇳