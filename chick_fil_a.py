import tkinter as tk
from tkinter import ttk
import random
import math

class ChickFilAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chick-fil-A Decision Maker")
        self.root.geometry("400x300")
        
        # Center the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Create main label
        self.label = ttk.Label(
            root, 
            text="Do you want to get Chick-fil-A?",
            font=("Arial", 16)
        )
        self.label.pack(pady=20)
        
        # Create Yes button
        self.yes_button = ttk.Button(
            root,
            text="Yes!",
            command=self.celebrate
        )
        self.yes_button.pack(pady=10)
        
        # Create No button
        self.no_button = ttk.Button(root, text="No")
        self.no_button.pack(pady=10)
        
        # Bind mouse hover event to No button
        self.no_button.bind('<Enter>', self.avoid_no)
        
        # Prepare chicken confetti
        self.chickens = []
        
    def avoid_no(self, event):
        # Move the No button to a random position when mouse hovers over it
        x = random.randint(0, self.screen_width - 100)
        y = random.randint(0, self.screen_height - 100)
        self.no_button.place(x=x, y=y)
        
    def create_confetti(self):
        canvas = tk.Canvas(self.root, width=400, height=300)
        canvas.pack(fill="both", expand=True)
        
        for _ in range(30):  # Create 30 falling chickens
            x = random.randint(0, 400)
            y = random.randint(-50, 0)
            chicken = canvas.create_text(
                x, y, 
                text="🐔",  # Chicken emoji
                font=("Arial", 20)
            )
            speed = random.uniform(1, 3)
            self.chickens.append({
                'chicken': chicken,
                'canvas': canvas,
                'speed': speed,
                'x': random.uniform(-1, 1),  # Add some horizontal movement
                'rotation': 0,
                'spin': random.uniform(-5, 5)  # Add some spin
            })
        
        self.animate_confetti()
    
    def animate_confetti(self):
        still_falling = False
        
        for chick in self.chickens:
            pos = chick['canvas'].coords(chick['chicken'])
            if pos[1] < 300:  # If chicken hasn't reached bottom
                chick['canvas'].move(
                    chick['chicken'],
                    chick['x'],
                    chick['speed']
                )
                # Rotate the chicken
                chick['rotation'] += chick['spin']
                chick['canvas'].itemconfig(
                    chick['chicken'],
                    angle=chick['rotation']
                )
                still_falling = True
        
        if still_falling:
            self.root.after(20, self.animate_confetti)
    
    def celebrate(self):
        # Remove all widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Show celebration message
        celebration_label = ttk.Label(
            self.root,
            text="Yay! Let's get Chick-fil-A! 🐔",
            font=("Arial", 18)
        )
        celebration_label.pack(pady=20)
        
        # Start chicken confetti animation
        self.create_confetti()

def main():
    root = tk.Tk()
    app = ChickFilAApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
