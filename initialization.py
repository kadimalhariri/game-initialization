import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f8ff")
        
        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.user_choice = None
        self.computer_choice = None
        
        # Set up game icons (using emoji as a simple alternative)
        self.icons = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️"
        }
        
        # Set up colors
        self.colors = {
            "rock": "#d9d9d9",
            "paper": "#f8f8ff",
            "scissors": "#e6f2ff"
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Rock-Paper-Scissors Game", 
            font=("Arial", 28, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Choose rock, paper, or scissors. Rock beats scissors, scissors beats paper, paper beats rock.",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#34495e",
            wraplength=600
        )
        instructions.pack(pady=10)
        
        # Score Frame
        score_frame = tk.Frame(self.root, bg="#f0f8ff")
        score_frame.pack(pady=20)
        
        # User Score
        user_score_label = tk.Label(
            score_frame,
            text=f"Player: {self.user_score}",
            font=("Arial", 18, "bold"),
            bg="#3498db",
            fg="white",
            width=12,
            height=2,
            relief="ridge"
        )
        user_score_label.grid(row=0, column=0, padx=10)
        
        # Ties
        ties_label = tk.Label(
            score_frame,
            text=f"Ties: {self.ties}",
            font=("Arial", 18, "bold"),
            bg="#f39c12",
            fg="white",
            width=12,
            height=2,
            relief="ridge"
        )
        ties_label.grid(row=0, column=1, padx=10)
        
        # Computer Score
        computer_score_label = tk.Label(
            score_frame,
            text=f"Computer: {self.computer_score}",
            font=("Arial", 18, "bold"),
            bg="#e74c3c",
            fg="white",
            width=12,
            height=2,
            relief="ridge"
        )
        computer_score_label.grid(row=0, column=2, padx=10)
        
        # Store score labels for updating
        self.user_score_label = user_score_label
        self.ties_label = ties_label
        self.computer_score_label = computer_score_label
        
        # Choice Frame
        choice_frame = tk.Frame(self.root, bg="#f0f8ff")
        choice_frame.pack(pady=30)
        
        # Choice buttons
        choices = ["rock", "paper", "scissors"]
        self.choice_buttons = {}
        
        for i, choice in enumerate(choices):
            button = tk.Button(
                choice_frame,
                text=f"{self.icons[choice]}\n{choice.capitalize()}",
                font=("Arial", 20),
                bg=self.colors[choice],
                fg="#2c3e50",
                width=10,
                height=3,
                relief="raised",
                command=lambda c=choice: self.select_choice(c)
            )
            button.grid(row=0, column=i, padx=15)
            self.choice_buttons[choice] = button
        
        # Selected choice display
        selection_frame = tk.Frame(self.root, bg="#f0f8ff")
        selection_frame.pack(pady=20)
        
        # User selection
        user_label = tk.Label(
            selection_frame,
            text="Your Choice:",
            font=("Arial", 16, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        user_label.grid(row=0, column=0, padx=10)
        
        self.user_choice_label = tk.Label(
            selection_frame,
            text="None",
            font=("Arial", 20),
            bg="#ecf0f1",
            width=12,
            height=2,
            relief="sunken"
        )
        self.user_choice_label.grid(row=0, column=1, padx=10)
        
        # VS label
        vs_label = tk.Label(
            selection_frame,
            text="VS",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#e74c3c"
        )
        vs_label.grid(row=0, column=2, padx=20)
        
        # Computer selection
        computer_label = tk.Label(
            selection_frame,
            text="Computer:",
            font=("Arial", 16, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        computer_label.grid(row=0, column=3, padx=10)
        
        self.computer_choice_label = tk.Label(
            selection_frame,
            text="None",
            font=("Arial", 20),
            bg="#ecf0f1",
            width=12,
            height=2,
            relief="sunken"
        )
        self.computer_choice_label.grid(row=0, column=4, padx=10)
        
        # Result display
        self.result_label = tk.Label(
            self.root,
            text="Make your selection!",
            font=("Arial", 22, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50",
            height=2
        )
        self.result_label.pack(pady=20)
        
        # Play button
        play_button = tk.Button(
            self.root,
            text="PLAY",
            font=("Arial", 20, "bold"),
            bg="#2ecc71",
            fg="white",
            width=15,
            height=2,
            command=self.play_game
        )
        play_button.pack(pady=10)
        
        # Reset button
        reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 14),
            bg="#95a5a6",
            fg="white",
            width=15,
            height=1,
            command=self.reset_game
        )
        reset_button.pack(pady=10)
        
        # Rules frame
        rules_frame = tk.Frame(self.root, bg="#ecf0f1", relief="ridge", borderwidth=2)
        rules_frame.pack(pady=20, padx=20, fill="x")
        
        rules_title = tk.Label(
            rules_frame,
            text="Game Rules:",
            font=("Arial", 14, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        rules_title.pack(anchor="w", padx=10, pady=5)
        
        rules_text = tk.Label(
            rules_frame,
            text="• Rock beats Scissors (rock crushes scissors)\n• Paper beats Rock (paper covers rock)\n• Scissors beats Paper (scissors cut paper)\n• Same choice results in a tie",
            font=("Arial", 12),
            bg="#ecf0f1",
            fg="#34495e",
            justify="left"
        )
        rules_text.pack(anchor="w", padx=20, pady=5)
    
    def select_choice(self, choice):
        # Reset previous selection
        for btn in self.choice_buttons.values():
            btn.configure(relief="raised", bg=self.colors[btn.cget("text").split("\n")[1].lower()])
        
        # Highlight selected choice
        self.choice_buttons[choice].configure(relief="sunken", bg="#3498db", fg="white")
        
        # Update user choice display
        self.user_choice = choice
        self.user_choice_label.config(text=f"{self.icons[choice]}\n{choice.capitalize()}")
    
    def play_game(self):
        if self.user_choice is None:
            messagebox.showwarning("No Selection", "Please select rock, paper, or scissors first!")
            return
        
        # Computer makes a random choice
        choices = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(choices)
        
        # Update computer choice display
        self.computer_choice_label.config(text=f"{self.icons[self.computer_choice]}\n{self.computer_choice.capitalize()}")
        
        # Determine winner
        result = self.determine_winner(self.user_choice, self.computer_choice)
        
        # Update result display
        self.result_label.config(text=result["text"], fg=result["color"])
        
        # Update scores
        if result["winner"] == "user":
            self.user_score += 1
        elif result["winner"] == "computer":
            self.computer_score += 1
        else:
            self.ties += 1
        
        # Update score labels
        self.user_score_label.config(text=f"Player: {self.user_score}")
        self.ties_label.config(text=f"Ties: {self.ties}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return {
                "winner": "tie",
                "text": "It's a Tie!",
                "color": "#f39c12"
            }
        
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        
        if winning_combinations[user_choice] == computer_choice:
            return {
                "winner": "user",
                "text": "You Win!",
                "color": "#2ecc71"
            }
        else:
            return {
                "winner": "computer",
                "text": "Computer Wins!",
                "color": "#e74c3c"
            }
    
    def reset_game(self):
        # Reset scores
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        
        # Reset choices
        self.user_choice = None
        self.computer_choice = None
        
        # Reset UI
        self.user_score_label.config(text=f"Player: {self.user_score}")
        self.ties_label.config(text=f"Ties: {self.ties}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        
        self.user_choice_label.config(text="None")
        self.computer_choice_label.config(text="None")
        
        self.result_label.config(text="Make your selection!", fg="#2c3e50")
        
        # Reset button highlights
        for btn in self.choice_buttons.values():
            choice_name = btn.cget("text").split("\n")[1].lower()
            btn.configure(relief="raised", bg=self.colors[choice_name], fg="#2c3e50")

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()