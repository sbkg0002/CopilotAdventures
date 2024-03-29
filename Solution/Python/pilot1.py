from PIL import Image
from io import BytesIO
import torch
class Creature:
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves

class Forest:
    def __init__(self):
        self.state = "Normal"

    def change_state(self, effect):
        self.state = effect

class Dance:
    def __init__(self, creature1, creature2, forest):
        self.creature1 = creature1
        self.creature2 = creature2
        self.forest = forest
        self.effects = {
            ("Twirl", "Twirl"): "Fireflies light up the forest",
            ("Leap", "Spin"): "Gentle rain starts falling",
            ("Spin", "Leap"): "A rainbow appears in the sky",
            ("Twirl", "Spin"): "A unicorn appears",
            ("Spin", "Twirl"): "A unicorn appears",
            ("Twirl", "Leap"): "Solar Eclipse",  # New effect
            ("Leap", "Twirl"): "Solar Eclipse",   # New effect
            ("Leap", "Twirl"): "A storm appears",  # New effect
            ("Twirl", "Leap"): "A storm appears"   # New effect
        }

    # Rest of the code remains the same...



    def perform(self):
        for move1, move2 in zip(self.creature1.moves, self.creature2.moves):
            effect = self.effects.get((move1, move2), "Unknown effect")
            self.forest.change_state(effect)
            print(f"{self.creature1.name} and {self.creature2.name} performed {move1} and {move2}. {effect}. Current state: {self.forest.state}")

lox_moves = ["Twirl", "Leap", "Spin", "Twirl", "Leap"]
drako_moves = ["Spin", "Twirl", "Leap", "Leap", "Spin"]

lox = Creature("Lox", lox_moves)
drako = Creature("Drako", drako_moves)
forest = Forest()

dance = Dance(lox, drako, forest)



dance.perform()
import requests
import json



# Get the dance effect
dance_effect = forest.state

# Make a POST request to the DALL-E instance
api_key = ""
headers = {"API-key": f"{api_key}"}


url = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generations?api-version=2023-12-01-preview"
data = json.dumps({"prompt": dance_effect})

response = requests.post(url, headers=headers, data=data)


# Check if the request was successful
if response.status_code == 200:
    try:
        # Try to open the image from the response
        image = Image.open(BytesIO(response.content))

        # Save the image as a JPEG file
        image.save("output.jpg")
    except Exception as e:
        print(f"Failed to open image: {e}")
        print(f"Response content: {response.content}")
else:
    print(f"Request failed with status code {response.status_code}")