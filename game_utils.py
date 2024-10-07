def solve_riddle(riddle):
    print(f"Riddle: {riddle}")
    
    # Zu Debug-Zwecken: Die richtige Antwort anzeigen
    correct_answer = ""
    if riddle == "I am not alive, but I can grow. What am I?":
        correct_answer = "crystal"
    elif riddle == "I have hands, but I can't clap. What am I?":
        correct_answer = "clock"
    elif riddle == "I have cities, but no houses. I have mountains, but no land. What am I?":
        correct_answer = "map"
    
    # Debug-Ausgabe: Zeigt die korrekte Antwort an
    print(f"Debug: The correct answer is '{correct_answer}'")
    
    # Benutzereingabe
    answer = input("Your answer: ").lower().strip()
    
    # Vergleich der Benutzereingabe mit der richtigen Antwort
    if answer == correct_answer:
        print("Correct! You can move on.")
    else:
        print("Wrong answer! Try again.")
        solve_riddle(riddle)  # Spieler kann es erneut versuchen

def end_game():
    print("Thanks for playing! See you next time.")
