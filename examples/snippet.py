#.................................................... Agent Configuration 👇.........................................................................................#

import requests

url = "https://api.aolabs.ai/v0dev/kennel"

payload = {
    "kennel_name": "Wscripted_Curator",
    "arch_URL": "https://gist.githubusercontent.com/mi3law/612f7cc6b9cbe96ba7304bad16931087/raw/5ea3b07f89a2b5eeacbc7045f841a8d48df0346a/arch__WScripted_Curator.py",
    "description": "Wscripted- Personal Curation Agent.  Takes in Genre, Theme, and Comparative Title (10 binary neurons each) for a piece of content to offer the user a recommendation, learning from subsequent individual user interaction.",
    "permissions": "private"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "buildBottomUpRealAGI"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)




#.................................................... Agent Training (Individual Input) 👇.........................................................................................#
import requests

url = "https://api.aolabs.ai/v0dev/kennel/agent"

payload = {
    "kennel_id": "Wscripted_Curator",  # use kennel_name entered above
    "agent_id": "1st_USER_ID",   # enter unique user IDs here, to call a unique agent for each ID
    "INPUT": "00000001010000000101011010100011100010101010101100",  # pass through the input from embedding_bucketing.auto_sort, adding any other inputs
    "size": "6"
    "control": {
        "CN": False,             # set as True when the user clicks "Good Recommendation," this will trigger learning to positively reinforce the agent's recommendation
        "CP": False,             # set as True when the user clicks "Bad Recommendation," this will trigger learning to **negatively** reinforce the agent's recommendation (inhibiting such recommendations going forward)
        "US": False,
        "neuron": {
            "DD": True,
            "Hamming": True,
            "Default": True
        }
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "buildBottomUpRealAGI"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)




#.................................................... Agent Pre-training 👇.........................................................................................#

import requests

url = "https://api.aolabs.ai/v0dev/kennel/agent"

# List of inputs to train the agent (In binary) 
# second element tell if recommend thsi particular video or not  
#after embedding
training_data = [
    ("00000001010000000101011010100011100010101010101100", 1),  # 1 --> recommend
    ("10000001100000010100101011100011100010101010101100", 0),  # 0 --> don't recommend
    # Add more binary input and feedback pairs as needed
]

# Iterate over each item in the training data
for binary_input, recommend in training_data:
    payload = {
        "kennel_id": "Wscripted_Curator",
        "agent_id": "1st_USER_ID",
        "INPUT": binary_input,
        "control": {
            "CN": True if recommend == 1 else False,  # True if recommend is 1 (Good Recommendation)
            "CP": True if recommend == 0 else False,  # True if recommend is 0 (Bad Recommendation)
            "US": False,
            "neuron": {
                "DD": True,
                "Hamming": True,
                "Default": True
            }
        }
    }

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "buildBottomUpRealAGI"
}    

response = requests.post(url, json=payload, headers=headers)

print(response.text)



