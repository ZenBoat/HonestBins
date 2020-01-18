import os

# Sign up for an Azure Speech services account and put hte key and region in here.
# You can sign up here: https://portal.azure.com/?WT.mc_id=twitchcaptions-github-jabenn#create/Microsoft.CognitiveServicesSpeechServices
# There is a free tier you can use
api_key = os.environ["AZURE_API_KEY"]
service_region = "westeurope"

# Put your device ID here, or leave this blank to use the default microphone.
# You can get your device Id by following these instructions: https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-select-audio-input-devices/?WT.mc_id=twitchcaptions-github-jabenn
device_uuid = ""
