import streamlit as st
import random
import string

def get_user_choice(user_name, round_number):
    """Get user's choice: 'snake', 'water', or 'gun'."""
    unique_key = f"{user_name}_choice_{round_number}"
    user_choice = st.radio(f"Round {round_number}: {user_name}, select your choice:", ('snake', 'water', 'gun'), key=unique_key)
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'snake':
        return "You win!" if computer_choice == 'water' else "Jagadish wins!"
    elif user_choice == 'water':
        return "You win!" if computer_choice == 'gun' else "Jagadish wins!"
    else:  # user_choice == 'gun'
        return "You win!" if computer_choice == 'snake' else "Jagadish wins!"

def main():
    st.title("Snake Water Gun Game")
    st.write("Welcome to the Snake Water Gun game!")
    user_name = st.text_input("Please enter your name:")
    if not user_name:
        st.warning("Please enter your name to start playing.")
        return

    st.write(f"Hi {user_name}, You will play against Jagadish (the computer). Let's get started.\n")

    user_wins = 0
    jagadish_wins = 0

    for round_number in range(1, 4):  # 3 attempts
        st.write(f"Round {round_number}")
        user_choice = get_user_choice(user_name, round_number)
        computer_choice = get_computer_choice()

        st.write(f"\n{user_name} chose: {user_choice}")
        st.write(f"Jagadish chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        st.write(result)

        if "You win" in result:
            user_wins += 1
        elif "Jagadish wins" in result:
            jagadish_wins += 1

    st.write("\nGame Over! Final Results:")
    st.write(f"{user_name}: {user_wins} wins")
    st.write(f"Jagadish: {jagadish_wins} wins")

    if user_wins > jagadish_wins:
        st.write(f"Congratulations, {user_name}! You won the game!")
    elif user_wins < jagadish_wins:
        st.write("Oops! Jagadish won the game.")
    else:
        st.write("It's a tie!")

if __name__ == "__main__":
    main()





