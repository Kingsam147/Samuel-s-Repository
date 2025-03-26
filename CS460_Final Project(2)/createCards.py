import json 

# method to create a card
def createCard(image: str, name: str):
     card = {
          "image": image,
          "name": name
     } 
     return card

def main(): 

     # continuously calling the method to create a list of ten unique cards
     cards = [
        createCard('resized-images/chopper.jpg', 'cardOne'),
        createCard('resized-images/download.jpg', 'cardTwo'),
        createCard('resized-images/Duke_Dennis.jpg', 'cardThree'),
        createCard('resized-images/IMG_0399.jpg', 'cardFour'),
        createCard('resized-images/IMG_9346.jpg', 'cardFive'),
        createCard('resized-images/Lebron_Sunshine.jpg', 'cardSix'),
        createCard('resized-images/Luffy.jpg', 'cardSeven'),
        createCard('resized-images/shooters_gonna_shoot.jpg', 'cardEight'),
        createCard('resized-images/Sigma_Man.jpg', 'cardNine') 
     ] 

     # then creating a .json file to store those cards
     with open("cards.json", "w") as f: 
         json.dump(cards, f, indent=2)

if __name__ == "__main__":
     main()