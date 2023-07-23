import streamlit as st
import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "water" and computer_choice == "gun") or \
         (player_choice == "gun" and computer_choice == "snake"):
        return "Congratulations! You win!"
    else:
        return "Computer wins!"

def main():
    st.title("Snake, Water, and Gun Game")

    player_choice = st.selectbox("Select your choice:", ("snake", "water", "gun"))
    computer_choice = get_computer_choice()

    if st.button("Play"):
        st.write(f"Computer's choice: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        st.write(result)

if __name__ == "__main__":
    main()
