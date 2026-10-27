# UNO-for-beginner
A fun and simple UNO game for beginners.

Our application is a card game where a human player plays against the computer. The game must follow the rules and check if each move is valid. Players can see their cards, save and load their games, and view the statistics to see how often the human player and the computer have won.

## Probelm
Beginners may find it difficult to learn UNO and understand the rules, especially when playing with special cards or figuring out which cards can be played. Above all, it's hard to always find someone to play with.

## Scenario
The UNO game allows all players to play against the computer whenever they want. Players can start the game and play cards according to the rules. They can also save the game, load saved game progress, and view statistics from previous games.

## Team Members
- Nicolas Schneider
- Thasika Sivaramalingam
- Subidsha Yoharajah
  
## UNO Rules
1. The game is played between one human player and one computer opponent using four colours: red, blue, green and yellow.
2. The human player begind the game.
3. The deck contains number cards from 0 to 9, Block (Skip) cards, +2 cards and colour-change (Wild) cards. Reverse and +4 cards are excluded to keep the game simple.
4. Each player receives seven cards at the beginning of the game.
5. 	5. A player can play a card if its colour or its number matches the top card on the discard pile.
6. A player can play a card if its symbol matches the symbol of the top card on the discard pile. Action symbols include Skip, Draw Two (+2)
7. When a player plays a Wild card, they must choose one of the four colours. The chosen colour becomes the active colour. The next player can play a card if its colour matches the active colour or if its number or action symbol matches the top card on the discard pile. Another Wild card can always be played, regardless of the active colour.
8. Block cards skip the opponent's turn.
9. The +2 cards make the opponent draw two cards and lose their turn.
10. +2 and skip cards cannot be stacked.
11. If a player has no playable card, they draw one card. If it is playable, they have to play it immediately. If not, then the next turn goes to the other player.
12. A player may only draw a card if he has no playable cards
13. The computer randomly plays a valid card or draws one if it cannot play.
14. The first player to get rid of all their cards wins the game.
      
## User Stories

### US-01: Start a new game (Thasika Sivaramalingam)
As a player, I want to start a new game, so that i can play with a new card deck

Acceptance criteria
- A new card deck is created and shuffled
- The human player starts the game
- The human player and the computer recive both 7 cards
- The game starts with the human players turn
- The previous game's are reset.

### US-02: View Cards (Thasika Sivaramalingam)
As a player, I need to see my cards, so that i know which card i can play

Acceptance criteria:
- All cards in the human player's hand are displayed.
- Each card's number or special type is visible.
- Each card's colour is visible.
- The computer's cards are hidden from the human player.
- The displayed hand updates after a card is played or drawn
- The active colour of the game is clearly displayed

### US-03: Play Valid Cards (Thasika Sivaramalingam)
As a player, I want to play a valid card from my hand, so that I can make a legal move

Acceptance criteria:
- The player can select a card from their hand.
- The game checks if the selected card can be played
- A number card can be played if the colour and number matches the top card
- A invalid card cannot be played and stays in the players hand.
- If the player dont have playable cards, they have to draw one card from the drwa pile
- If the draw card is playable, the player have to play it immediatly
- After a Wild card is played, a number card is valid if its colour matches the chosen active colour OR its number matches the number of the Wild card's preceding top card.
  
### US-04: Play Action & Wild Card (Subidsha Yoharajah)
As a player, I want to play a Action & Wild cards, so that I can use their special effects during the game

Acceptance criteria:
- The player can play a wild card from their hand regardless of the current colour.
- The player have to choose one of the four colours.
- The selected colour becomes the active colour for the next round.
- The wild card will be removed from the players hand.
- The computer player have to follow the selected colour unless they play another wild card
- The player can play an Action card if ist colour matches the active colour.
- The player can play an Action card if its symbol matches the active symbol.
- A skip card skips the next players turn
- When a player plays a + 2 card, the next player drwas two cards and loses their turn
- A player cannot stack another + 2 card on a + 2 card.
- Skip and + 2 cards cannot be stacked to avoid their effect.
- After a Wild card is played, an Action card (Skip or +2) is valid if its colour matches the chosen active colour OR its symbol matches the symbol of the top card on the discard pile.

### US-05: Computer Player (Nicolas Schneider)
As a player, I want the computer to play its turn automatically, so that I can play against the computer.
Acceptance criteria:
- The computer checks if it has playable cards
- If it has playable card, the computer choose it randomly
- If the compuuter don't have playable cards, it draws one card from the draw pile
- If the draw card is playable, it plays the card immediatly
- If the computer plays a wild card, it chooses the colour that appears often in their hand.
- If the computer plays a skip card, the human players turn is skipped
- After the computer completes its turn, the next turn depends on the effect of the card played. If the computer plays a Skip or +2 card, the human player's next turn is skipped, and the computer takes another turn
- If the computer has no cards left, the game ends and the computer is the winner
  
### US-06: Save and Load Game (Nicolas Schneider)
As a player, I want to save and load my game, so that I can continue playing later without losing my progress
Acceptance criteria:

- The player can save a current game
- They player can load a save game and continue playing
- The game will safe automatically when the player exit the game
- The loaded game restores both players card and the current game state
- If no save game exists, the game shows an error message when the player tries to load a game.
  
### US-07: Detect Winner (Subidsha Yoharajah)
As a player, I want the game to detect when a player has no cards left, so that the game
Acceptance criteria:
- The games checks who has any cards left after playing a card
- The game ends when a player has no card left
- The game shows if the human player or the computer has won
- The winner is recorded in the game statistics
- No turns can be played after the game ends.
  
### US-08: View Game Statistcs (Subidsha Yoharajah)
As a player, I want to view the game statistics, so that I can see how often the human player and the computer have won
Acceptance criteria:
- The game shows the total number of wins for the human player
- The game shows the total number of wins for the computer
- The Statistcs are updated when a game ends
- Each game result is counted only once
- The statistics stay saved after the application is cloed an restarted
- If a game hasn’t been completed, it doesn’t count towards the statistics
