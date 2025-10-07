"""
Offline AI Engine - No External APIs Required
Uses rule-based NLP and pattern matching
"""
from textblob import TextBlob
import re
import random
from django.conf import settings


class OfflineAIEngine:
    """Rule-based conversational AI for therapy chatbot"""
    
    def __init__(self):
        # Intent patterns with keywords
        self.intent_patterns = {
            'anxiety': {
                'keywords': ['anxious', 'anxiety', 'worried', 'nervous', 'panic', 'fear', 
                            'scared', 'frightened', 'terrified', 'tense', 'uneasy'],
                'questions': [
                    "What specific situation is making you feel this way?",
                    "Can you tell me more about what triggers these feelings?",
                    "Have you noticed any physical sensations when you feel anxious?",
                    "On a scale of 1-10, how intense is your anxiety right now?",
                    "What thoughts go through your mind when you feel anxious?"
                ]
            },
            'depression': {
                'keywords': ['depressed', 'depression', 'sad', 'sadness', 'hopeless', 
                            'worthless', 'empty', 'lonely', 'alone', 'unmotivated', 'tired', 'exhausted'],
                'questions': [
                    "How long have you been feeling this way?",
                    "What activities did you used to enjoy?",
                    "Have you been able to talk to anyone about how you're feeling?",
                    "What does a typical day look like for you right now?",
                    "Is there anything that makes you feel even slightly better?"
                ]
            },
            'stress': {
                'keywords': ['stressed', 'stress', 'overwhelmed', 'pressure', 'busy', 
                            'burnout', 'overworked', 'too much', 'can\'t cope'],
                'questions': [
                    "What's the main source of your stress right now?",
                    "How many things are you trying to juggle at the moment?",
                    "Have you been able to take any breaks?",
                    "What usually helps you manage stress?",
                    "Is there anything you can delegate or let go of?"
                ]
            },
            'greeting': {
                'keywords': ['hello', 'hi', 'hey', 'good morning', 'good evening', 
                            'good afternoon', 'greetings', 'howdy'],
                'responses': [
                    "Hello! I'm GenTherapist, your AI companion for mental wellness. How are you feeling today?",
                    "Hi there! I'm here to support you with CBT techniques. What's on your mind?",
                    "Welcome! I'm GenTherapist. How can I help you today?",
                    "Hello! It's good to connect with you. What would you like to talk about?"
                ]
            },
            'gratitude': {
                'keywords': ['thank', 'thanks', 'grateful', 'appreciate', 'helped', 'helpful'],
                'responses': [
                    "You're very welcome! I'm glad I could help. Is there anything else you'd like to talk about?",
                    "I'm happy I could support you! Remember, I'm here whenever you need to talk.",
                    "You're welcome! Taking care of your mental health is important. How are you feeling now?"
                ]
            },
            'goodbye': {
                'keywords': ['bye', 'goodbye', 'see you', 'later', 'leave', 'exit', 'quit'],
                'responses': [
                    "Take care of yourself! Remember, I'm here whenever you need support.",
                    "Goodbye! Don't hesitate to come back if you need to talk.",
                    "Wishing you well! Remember to practice the techniques we discussed."
                ]
            }
        }
        
        # Response templates
        self.response_templates = {
            'anxiety_validation': [
                "I hear that you're feeling anxious. That must be really challenging for you.",
                "It sounds like you're dealing with a lot of anxiety right now. I'm here to help.",
                "Anxiety can be overwhelming. Thank you for sharing this with me.",
                "I understand that anxiety can feel very intense. You're not alone in this."
            ],
            'depression_validation': [
                "I'm sorry you're feeling this way. Depression can make everything feel harder.",
                "Thank you for opening up about your feelings. That takes courage.",
                "It sounds like you're going through a really difficult time. I'm here to support you.",
                "Depression can be so heavy to carry. I want you to know that these feelings are valid."
            ],
            'stress_validation': [
                "It sounds like you're dealing with a lot right now. That's really stressful.",
                "I can understand feeling overwhelmed when there's so much on your plate.",
                "Stress can be exhausting. Let's work together to find ways to manage it.",
                "It's completely normal to feel stressed in your situation."
            ],
            'general_validation': [
                "Thank you for sharing that with me. Tell me more about what's going on.",
                "I'm here to listen. What's been on your mind?",
                "It's important to talk about how you're feeling. I'm listening.",
                "I appreciate you opening up. How can I best support you right now?"
            ]
        }
        
        # Coping suggestions
        self.coping_suggestions = {
            'anxiety': [
                "Let's try a quick grounding exercise. Can you name 5 things you can see right now?",
                "When anxiety rises, deep breathing can help. Try breathing in for 4, hold for 4, out for 6.",
                "Sometimes it helps to ask: Is this thought based on facts or feelings?",
                "Have you tried the 5-4-3-2-1 grounding technique? It can help bring you to the present."
            ],
            'depression': [
                "Even small activities can help. Is there one tiny thing you could do today that you used to enjoy?",
                "Depression can make everything feel pointless, but small steps matter. What's one achievable thing today?",
                "Reaching out, like you're doing now, is a positive step. Have you considered talking to a professional?",
                "Being gentle with yourself is important. What would you say to a friend feeling this way?"
            ],
            'stress': [
                "Let's break down what's stressing you. What's the most urgent thing on your list?",
                "Sometimes we can't control everything. What's one thing you CAN control right now?",
                "Taking a 5-minute break can actually boost productivity. Can you step away briefly?",
                "Have you considered making a priority list? Not everything needs to be done today."
            ]
        }
    
    def analyze_sentiment(self, text):
        """Analyze sentiment using TextBlob"""
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            
            if polarity > 0.1:
                return 'positive'
            elif polarity < -0.1:
                return 'negative'
            else:
                return 'neutral'
        except:
            return 'neutral'
    
    def detect_intent(self, text):
        """Detect user intent from keywords"""
        text_lower = text.lower()
        
        for intent, data in self.intent_patterns.items():
            if any(keyword in text_lower for keyword in data['keywords']):
                return intent
        
        return 'general'
    
    def detect_crisis(self, text):
        """Detect crisis keywords"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in settings.CRISIS_KEYWORDS)
    
    def extract_keywords(self, text):
        """Extract important keywords"""
        stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'you', 'your', 'he', 
                     'she', 'it', 'they', 'am', 'is', 'are', 'was', 'been', 'being',
                     'have', 'has', 'had', 'do', 'does', 'did', 'a', 'an', 'the', 
                     'and', 'but', 'if', 'or', 'as', 'at', 'by', 'for', 'with',
                     'about', 'into', 'through', 'during', 'before', 'after'}
        
        words = re.findall(r'\b\w+\b', text.lower())
        keywords = [w for w in words if w not in stop_words and len(w) > 3]
        return keywords[:5]
    
    def generate_response(self, user_message, conversation_history=None):
        """Generate response using rule-based logic"""
        
        # Check for crisis first
        if self.detect_crisis(user_message):
            return settings.CRISIS_RESPONSE
        
        # Detect intent
        intent = self.detect_intent(user_message)
        
        # Handle special intents
        if intent in ['greeting', 'gratitude', 'goodbye']:
            return random.choice(self.intent_patterns[intent]['responses'])
        
        # Get sentiment
        sentiment = self.analyze_sentiment(user_message)
        
        # Extract keywords
        keywords = self.extract_keywords(user_message)
        
        # Build response
        response_parts = []
        
        # 1. Validation/Empathy
        if intent in ['anxiety', 'depression', 'stress']:
            validation = random.choice(self.response_templates[f'{intent}_validation'])
        else:
            validation = random.choice(self.response_templates['general_validation'])
        response_parts.append(validation)
        
        # 2. Context-specific response
        if 'exam' in keywords or 'test' in keywords:
            response_parts.append("Exams can be very stressful. Remember, it's okay to feel nervous - that shows you care.")
        elif 'work' in keywords or 'job' in keywords:
            response_parts.append("Work-related stress is very common. It's important to set boundaries.")
        elif 'sleep' in keywords:
            response_parts.append("Sleep problems can really affect how we feel. Have you tried a consistent bedtime routine?")
        elif 'family' in keywords or 'relationship' in keywords:
            response_parts.append("Relationship challenges are difficult. Open communication can help.")
        
        # 3. Coping suggestion or question
        if intent in self.coping_suggestions:
            suggestion = random.choice(self.coping_suggestions[intent])
            response_parts.append(suggestion)
        elif intent in self.intent_patterns and 'questions' in self.intent_patterns[intent]:
            question = random.choice(self.intent_patterns[intent]['questions'])
            response_parts.append(question)
        
        # Join response
        response = " ".join(response_parts)
        
        # Add encouragement for positive sentiment
        if sentiment == 'positive':
            response += " I'm glad to hear some positivity in your message!"
        
        return response


# Global instance
ai_engine = OfflineAIEngine()
