"""
Views for GenTherapist
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .ai_engine import ai_engine
from .cbt_modules import CBTModules


def chat_home(request):
    """Main chat page"""
    if 'conversation' not in request.session:
        request.session['conversation'] = []
    return render(request, 'chat.html')


@csrf_exempt
@require_http_methods(["POST"])
def send_message(request):
    """Handle chat message"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)
        
        # Get conversation history
        conversation = request.session.get('conversation', [])
        
        # Analyze sentiment
        sentiment = ai_engine.analyze_sentiment(user_message)
        
        # Detect intent
        intent = ai_engine.detect_intent(user_message)
        
        # Check for crisis
        is_crisis = ai_engine.detect_crisis(user_message)
        
        # Save user message
        conversation.append({
            'role': 'user',
            'content': user_message,
            'sentiment': sentiment
        })
        
        # Generate AI response
        bot_response = ai_engine.generate_response(user_message, conversation)
        
        # Save bot response
        conversation.append({
            'role': 'assistant',
            'content': bot_response,
            'sentiment': 'neutral'
        })
        
        # Update session
        request.session['conversation'] = conversation
        request.session.modified = True
        
        # Get CBT techniques
        cbt_techniques = CBTModules.get_techniques_by_intent(intent)
        
        return JsonResponse({
            'success': True,
            'bot_response': bot_response,
            'sentiment': sentiment,
            'intent': intent,
            'is_crisis': is_crisis,
            'cbt_techniques': cbt_techniques
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


@require_http_methods(["POST"])
def clear_conversation(request):
    """Clear conversation"""
    request.session['conversation'] = []
    return JsonResponse({'success': True})
