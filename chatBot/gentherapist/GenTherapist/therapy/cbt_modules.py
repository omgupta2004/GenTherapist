"""
CBT Modules and Techniques
"""

class CBTModules:
    """Collection of CBT techniques"""
    
    @staticmethod
    def get_techniques_by_intent(intent):
        """Get CBT techniques based on intent"""
        techniques = {
            'anxiety': {
                'title': 'Anxiety Management Techniques',
                'exercises': [
                    {
                        'name': '4-7-8 Breathing',
                        'icon': '🌬️',
                        'description': 'Calm your nervous system',
                        'instructions': '''1. Sit comfortably
2. Breathe in through nose for 4 counts
3. Hold breath for 7 counts
4. Exhale through mouth for 8 counts
5. Repeat 3-4 times'''
                    },
                    {
                        'name': '5-4-3-2-1 Grounding',
                        'icon': '🌍',
                        'description': 'Ground yourself in the present',
                        'instructions': '''Name out loud:
• 5 things you can see
• 4 things you can touch
• 3 things you can hear
• 2 things you can smell
• 1 thing you can taste'''
                    },
                    {
                        'name': 'Challenge Anxious Thoughts',
                        'icon': '🧠',
                        'description': 'Question your worries',
                        'instructions': '''Ask yourself:
• What evidence supports this?
• What evidence contradicts it?
• What would I tell a friend?
• What's realistically likely?'''
                    }
                ]
            },
            'depression': {
                'title': 'Depression Support Techniques',
                'exercises': [
                    {
                        'name': 'Behavioral Activation',
                        'icon': '⚡',
                        'description': 'Small activities boost mood',
                        'instructions': '''Choose ONE small activity:
• 5-minute walk
• Listen to a favorite song
• Call a friend
• Do one small chore
• 5 minutes in sunlight'''
                    },
                    {
                        'name': 'Gratitude Practice',
                        'icon': '🙏',
                        'description': 'Notice positives',
                        'instructions': '''Write down 3 things:
• One thing you're grateful for
• One small win today
• One thing you're looking forward to'''
                    },
                    {
                        'name': 'Self-Compassion',
                        'icon': '💙',
                        'description': 'Be kind to yourself',
                        'instructions': '''Repeat:
• "I'm doing the best I can"
• "It's okay to struggle"
• "I deserve kindness"
• "This feeling is temporary"'''
                    }
                ]
            },
            'stress': {
                'title': 'Stress Management Techniques',
                'exercises': [
                    {
                        'name': 'Progressive Muscle Relaxation',
                        'icon': '💪',
                        'description': 'Release physical tension',
                        'instructions': '''For each muscle group:
1. Tense for 5 seconds
2. Release and notice difference
3. Start with toes, move to head
4. Take your time'''
                    },
                    {
                        'name': 'Priority Matrix',
                        'icon': '📊',
                        'description': 'Organize tasks',
                        'instructions': '''Sort tasks:
• Urgent & Important → Do now
• Important not urgent → Schedule
• Urgent not important → Delegate
• Neither → Let go'''
                    },
                    {
                        'name': 'Mindful Break',
                        'icon': '☕',
                        'description': '5-minute pause',
                        'instructions': '''For 5 minutes:
• Step away from work
• Focus on breathing
• Notice body sensations
• No phone or screens'''
                    }
                ]
            },
            'general': {
                'title': 'General Wellness Techniques',
                'exercises': [
                    {
                        'name': 'Deep Breathing',
                        'icon': '🌬️',
                        'description': 'Simple calming breath',
                        'instructions': '''Basic technique:
1. Breathe in for 4 counts
2. Hold for 4 counts
3. Breathe out for 4 counts
4. Repeat 5 times'''
                    },
                    {
                        'name': 'Thought Record',
                        'icon': '📝',
                        'description': 'Track and challenge thoughts',
                        'instructions': '''Write down:
• Situation
• Automatic thought
• Emotion (1-10)
• Evidence for/against
• Alternative thought'''
                    },
                    {
                        'name': 'Body Scan',
                        'icon': '🧘',
                        'description': 'Notice sensations',
                        'instructions': '''Sit comfortably:
1. Close your eyes
2. Scan from toes to head
3. Just observe, don't judge
4. Take 5-10 minutes'''
                    }
                ]
            }
        }
        
        return techniques.get(intent, techniques['general'])
