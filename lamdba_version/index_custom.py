"""
This code sample is a part of a simple demo to show beginners how to create a skill (app) for the Amazon Echo using AWS Lambda and the Alexa Skills Kit.

For the full code sample visit https://github.com/pmckinney8/Alexa_Skill_Dojo_Demo_Pyhton.git
"""

from __future__ import print_function

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "DojoInfoIntent":
        return get_dojo_info_response()
    elif intent_name == "DojoStaffIntent":
        return get_dojo_staff_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "TextBrendenIntent":
        return touch_face_with_Brenden()
    elif intent_name == "GetTouchFaceIntent":
        return get_touchface_response()
    elif intent_name == "DojoBrendenIntent":
        return dojo_Brenden_response()
    elif intent_name == "AskBrendan":
        return ask_brendan()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to our team presentation. Luba, Anette, Minh, and Andy all created an app where you can literally...Touch Face with Brenden"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with the same text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "Welcome to the help section for the Coding Dojo Skill. A couple of examples of phrases that I can except are... What is the coding dojo... or, who are the instructors. Lets get started now by trying one of these."

    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def get_dojo_info_response():
    session_attributes = {}
    card_title = "Dojo_Info"
    speech_output = "The Coding Dojo is a 3 month immersive web developement bootcamp. During these 3 months you will learn 3 full web developement stacks. The stacks that we offer are... Django, Rails, Mean, and IOS."

    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def get_dojo_staff_response():
    session_attributes = {}
    card_title = "Dojo_Staff"
    speech_output = "The coding dojo currently has 7 instructors. Their names are Anna, Oscar, Jay, Pariece, Brendan, Howard, and Eli."
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

# Text to Brenden below:
def touch_face_with_Brenden():
    session_attributes = {}
    card_title = "touch_face_with_Brenden"
    speech_output = "Do you want me to text Brendan or Touch his face... Just kidding, I'll text him."
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def get_touchface_response():
    session_attributes = {}
    card_title = "Touchface"
    speech_output = "Just remember Fat Model, skinny controller...Fat Model, skinny controller"
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def dojo_Brenden_response():
    session_attributes = {}
    card_title = "Brenden_Response"
    speech_output = "He is a coding dojo Sensei. Michael Choi is his Soke, also known as the Grand Master."
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def ask_brendan():
    session_attributes = {}
    card_title = "Ask_Brendan"
    speech_output = "Touch face is great thing to interact with Brendan. He is a funny guy."
    reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))




# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
