const gridContainer = document.querySelector(".grid-container");
let cards = [];
let firstCard, secondCard; 
let lockBoard = true; // let's the user interact with the board
let score = 0; 
let attempts = 0; 
let time = 0;
let timerInterval;  
const minutesElement = document.getElementById("minutes"); 
const secondsElement = document.getElementById("seconds");
let topScores = [];  
let username = "username";

// If this is the user's first time than they should haven't have a list of topScores 
// saved in local storage
if (localStorage.getItem('topScores') != null) {
    topScores = JSON.parse(localStorage.getItem('topScores'));
}

// import cards from cards.json
fetch("cards.json")
    .then((res) => res.json())
    .then((data) => {
        cards = [...data, ...data];
        shuffleCards(); 
        generateCards();
    });   

function startTimer() {
    time = 0;  
    // if timer is already running than clear it and update the clock
    if (timerInterval) clearInterval(timerInterval); 
    updateTimeDisplay();

    timerInterval = setInterval(() => {
        time++; 
        updateTimeDisplay();
    }, 1000); 

}  

// restarts the timer
function stopTimer() {
    time = 0;
    clearInterval(timerInterval);  
    updateTimeDisplay();
}

// converts time variable to minutes and seconds then updates clock display
function updateTimeDisplay() {
    const minutes = Math.floor(time/60); 
    const seconds = time % 60;  

    if (minutesElement) minutesElement.innerText = minutes; 
    if (secondsElement) secondsElement.innerText = seconds;
    if (seconds < 10) {
        secondsElement.innerText = "0" + secondsElement.innerText;
    }
}

// randomizes the location of the cards
function shuffleCards() {
    let currentIndex = cards.length, 
        randomIndex, 
        temporaryValue;  
    while (currentIndex != 0) {
        randomIndex = Math.floor(Math.random() * currentIndex); 
        currentIndex -= 1; 
        temporaryValue = cards[currentIndex]; 
        cards[currentIndex] = cards[randomIndex]; 
        cards[randomIndex] = temporaryValue; 
    }
} 

// takes data from cards and generates it in .html file
function generateCards() { 
    for (let card of cards) {
        const cardElement = document.createElement("div"); 
        cardElement.classList.add("card"); 
        cardElement.setAttribute("data-name", card.name);  
        cardElement.innerHTML = `
            <div class="front"> 
                <img class="front-image" src=${card.image} />
            </div>  
            <div class = "back"></div> 
        `; 
        gridContainer.appendChild(cardElement); 
        cardElement.addEventListener("click", flipCard); 
    }
} 


function flipCard() {
    // if the board isn't locked or you didn't click on the first card again then...
    if (lockBoard) return; 
    if (this === firstCard) return; 

    // flip the card
    this.classList.add("flipped"); 

    if (!firstCard) {
        firstCard = this; 
        return; 
    } 
    secondCard = this;  

    // if the first card doesn't match the second card then increment attemps
    if (firstCard.dataset.name != secondCard.dataset.name) {
        attempts++; 
        document.querySelector(".attempts").textContent = attempts;
    } 

    // lock the board while the all this is happenning
    lockBoard = true;  

    checkForMatch();  

    const allCards = document.querySelectorAll(".card");
    const flippedCards = document.querySelectorAll(".card.flipped");
    const allFlipped = allCards.length == flippedCards.length;

    // if all the cards are flipped than the user has won
    if (allFlipped) {
        
        // update the score using time and number of failed attempts
        score = parseInt(100000/time - (20*attempts)); 
        if (score < 0) {
            score = 0; 
        }  
       
        // if there are less than 5 top scores than just add the score to the leaderboard
        if (topScores.length < 5) {
            topScores.push([username, score]);
            topScores.sort((a, b) => a[1] - b[1]); 
            topScores.reverse();
        } else {
            // check to see if the current score is bigger than the smallest topScore
            if (score > topScores[4][1]) {
                // if it is then append it to the list, sort the list, then remove the smallest element
                // resulting in the new top 5 scores
                topScores.push([username, score]); 
                topScores.sort((a, b) => a[1] - b[1]); 
                topScores.reverse();
                topScores.pop();
            }  
        } 

        // after everything is done store the new list of topScores to the localStorage
        // and add the topScores to the modal
        localStorage.setItem('topScores', JSON.stringify(topScores));
        
        // putting the scores for the win screen
        document.querySelector(".score").textContent = score;

        // display all the top scores that the user has 
        // if the topScore isn't null in the array then update the text 
        // otherwise tell the user that it's 0
        document.querySelector("#scoreOne").textContent = topScores[0][0] + ": " + topScores[0][1];
        if (topScores[1] != null) {
            document.querySelector("#scoreTwo").textContent = topScores[1][0] + ": " + topScores[1][1];
        }
        if (topScores[2] != null) {
            document.querySelector("#scoreThree").textContent = topScores[2][0] + ": " + topScores[2][1];
        }
        if (topScores[3] != null) {
            document.querySelector("#scoreFour").textContent = topScores[3][0] + ": " + topScores[3][1];
        }
        if (topScores[4] != null) {
            document.querySelector("#scoreFive").textContent = topScores[4][0] + ": " + topScores[4][1];
        }

        // make the you win screen appear
        setTimeout(() => {document.getElementById("modal").style.visibility = "visible"}, 500);

        clearInterval(timerInterval); 
    } 
    
}   

// removes you-win screen
function closeWindow() {
    document.getElementById("modal").style.visibility = "hidden";
}


// checks to see if cards match, if they do then keep them face up 
// otherwise flip them back down
function checkForMatch() {
    let isMatch = firstCard.dataset.name === secondCard.dataset.name; 

    isMatch ? disableCards() : unflipCards(); 
} 

// prevent the user from interacting with the cards
function disableCards() {
    firstCard.removeEventListener("click", flipCard); 
    secondCard.removeEventListener("click", flipCard); 

    resetBoard(); 
} 

// flip the cards back down
function unflipCards() {
    setTimeout (() => {
        firstCard.classList.remove("flipped"); 
        secondCard.classList.remove("flipped"); 
        resetBoard(); 
    }, 1000);
}  

// unselect the first and second cards and unlock the board
function resetBoard() {
    firstCard = null; 
    secondCard = null; 
    lockBoard = false; 
}

// resets the game to it's original state
function restart() {
    resetBoard(); 
    shuffleCards(); 
    stopTimer(); 
    score = 0; 
    document.getElementById("modal").style.visibility = "hidden";
    gridContainer.innerHTML = "";  
    generateCards(); 
    lockBoard = true; 
    attempts = 0; 
    score = 0; 
    time = 0; 
    document.querySelector(".attempts").innerText = "0";
}    

function startGame() {
    // if the game is already started then just restart it
    if (time > 0) {
        restart(); 
        startGame();
    }

    startTimer(); 
    lockBoard = false; 
    username = document.getElementById("username").value;
    if (!username) {
        username = "username";
    }  

    // added a cool effect that makes the clock glow purple for a second when the game starts
    const clockElement = document.querySelector(".clock"); 
    clockElement.style.transition = "color 1s ease, border 1s ease";
    clockElement.style.color = '#663399';
    clockElement.style.border = "2px solid #663399";
    setTimeout(() => {
        clockElement.style.color = 'white'; 
        clockElement.style.border = "2px solid white";
    }, 1000);
} 

// not really important, but nice little function to resize username textbox 
function resizeInput(input) {
    input.style.width = "250px"; 
    input.style.width = (input.scrollWidth + 1) + "px"; 
} 
// resets the textbox (called when textbox is clicked off of)
function resetInput(input) {
    input.style.width = "250px";
}

console.log("This is the main function"); 
