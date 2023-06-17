#!/bin/bash

# Greet user and request their name
echo "The activity generator"
read -p "What is your name? " name

# Create an array of activities
option[0]="Football"
option[1]="Table Tennis"
option[2]="8 Ball Pool"
option[3]="PS5"
option[4]="Blackjack"

array_length=${#option[@]} # Store the length of the array
index=$(($RANDOM % $array_length)) # Randomly select an index from 0 to array_length

# Invite the user to join you participate in an activity
echo "Hi" $name, "would you like to play" ${option[$index]}"?"
read -p "Answer: " answer

echo "Welcome, " $name ". You are most welcome to join me in a game of " ${option[$index]} "!"
