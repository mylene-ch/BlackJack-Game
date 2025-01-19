Blackjack Game

Introduction

This project is a Python program that simulates a simplified version of the popular casino game Blackjack (also known as 21). Players compete against a dealer to accumulate as much money as possible without exceeding a hand value of 21. This program uses Object-Oriented Programming (OOP) concepts to implement game logic, such as deck creation, card dealing, betting, and game rules.

Features

Gameplay Mechanics:

Player vs. dealer gameplay.

Ace can be valued at 1 or 11, depending on the player's hand.

Automatic handling of busts, ties, and Blackjack scenarios.

User Interaction:

Place bets between $1 and the player's current balance.

Options to hit or stay during the player's turn.

Clear and user-friendly prompts with validation.

Game Rules:

Dealer hits until the hand value reaches 17 or more.

Player wins, ties, or loses based on hand comparison with the dealer.

Blackjack payout is 1.5x the original bet.

Sample Usage

Welcome to Blackjack!

You are starting with $500. Would you like to play a hand? yes
Place your bet: 10
You are dealt: A♥, K♣
The dealer is dealt: 7♦, Unknown
Blackjack! You win $15 :)

You are starting with $505. Would you like to play a hand? no
You left the game with $505.

How It Works

Game Start:

Players start with a balance of $500.

The game asks if the player wants to play a hand.

Betting:

Players place a bet between $1 and their current balance.

Bets are validated to ensure they are within limits.

Card Dealing:

Two cards are dealt to both the player and the dealer.

The player's cards are face-up, while one of the dealer's cards is face-down.

Player's Turn:

Players decide to "hit" (draw a card) or "stay" (end their turn).

If the player's hand value exceeds 21, they bust and lose the round.

Dealer's Turn:

The dealer reveals the face-down card.

The dealer hits until the hand value is 17 or more.

If the dealer busts, the player wins.

End of Round:

The winner is determined based on hand values.

Bets are settled, and the game resets for the next round.

Code Structure

Card Class: Represents individual cards with suit and value.

Deck Class: Creates and shuffles a standard 52-card deck.

Hand Class: Manages cards in a player's or dealer's hand and calculates hand value.

Player Class: Extends the dealer to add balance and betting functionality.

Dealer Class: Manages the dealer's hand and actions.

Game Class: Implements game logic, including betting, card dealing, and turn handling.

Main Script: Starts the game and handles user interaction.

Requirements

Python 3.x

Future Improvements

Add advanced Blackjack rules, such as splitting and doubling down.

Enhance user interface with graphical elements or web integration.

Support multiplayer functionality.

Save and load player progress.
