import azure.cognitiveservices.speech as speechsdk
import config
import questions

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = config.api_key, config.service_region
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# print(speech_config.speech_synthesis_voice_name)

def readaloud(text):
    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Synthesizes the received text to speech.
    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")

def pop_fact(fact_number):
    
    text = questions.facts[fact_number]
    readaloud(text)

def pop_questions(question_number):
    
    text = questions.questions[question_number]
    readaloud(text)

def get_response():
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = config.api_key, config.service_region
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Say something...")

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed.  The task returns the recognition text as result. 
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query. 
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return "nomatch"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    
    return result.text

def do_quiz(question_number):
    pop_questions(question_number)
    answer = get_response()
    if answer == "Yes.":
        if questions.answers[question_number] == "yes":
            readaloud("That's correct! You really care about the enviroment.")
        else:
            readaloud("Surprisingly it's not true. Congrats you've learned something new today. Let's save the planet.")
    elif answer == "No.":
        if questions.answers[question_number] == "no":
            readaloud("That's correct! You really care about the enviroment.")
        else:
            readaloud("Surprisingly it's true. Congrats you've learned something new today. Let's save the planet.")
    elif answer == "nomatch":
        text = "Seems that you are a bit confused. The answer to this question is "
        text += questions.answers[question_number]
        text += " . Congrats you've learned something new today. Let's save the planet."
        readaloud(text)
    else:
        pass

if __name__ == "__main__":
    import random
    # pop_fact(random.randrange(9))
    do_quiz(random.randrange(4))