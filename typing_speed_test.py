import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Test variables
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet and is commonly used for typing practice.",
            "Programming is the art of telling another human being what one wants the computer to do. It requires patience, logic, and creativity.",
            "In the world of technology, continuous learning is essential. New frameworks, languages, and tools emerge constantly, challenging developers to adapt.",
            "Artificial intelligence is transforming how we work, communicate, and solve problems. Machine learning algorithms can now recognize patterns in data.",
            "The internet has revolutionized global communication, making it possible to connect with people anywhere in the world instantly and efficiently."
        ]
        
        self.current_text = ""
        self.start_time = None
        self.is_test_active = False
        self.typed_characters = 0
        self.correct_characters = 0
        
        self.setup_ui()
        self.load_new_text()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Typing Speed Test", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Click 'Start Test' and begin typing the text below. Your speed will be calculated in real-time.",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        instructions.pack(pady=10)
        
        # Sample text display
        text_frame = tk.Frame(self.root, bg="#fff", relief="solid", bd=1)
        text_frame.pack(pady=20, padx=40, fill="x")
        
        self.text_display = tk.Text(
            text_frame,
            height=6,
            font=("Courier", 14),
            wrap="word",
            state="disabled",
            bg="#fff",
            fg="#333",
            padx=15,
            pady=15
        )
        self.text_display.pack(fill="both", expand=True)
        
        # Input field
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20, padx=40, fill="x")
        
        tk.Label(
            input_frame,
            text="Type here:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(anchor="w")
        
        self.input_text = tk.Text(
            input_frame,
            height=6,
            font=("Courier", 14),
            wrap="word",
            padx=15,
            pady=15,
            state="disabled"
        )
        self.input_text.pack(fill="both", expand=True, pady=(5, 0))
        self.input_text.bind("<KeyPress>", self.on_key_press)
        self.input_text.bind("<KeyRelease>", self.on_key_release)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="Start Test",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.start_test
        )
        self.start_button.pack(side="left", padx=10)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            command=self.reset_test
        )
        self.reset_button.pack(side="left", padx=10)
        
        self.new_text_button = tk.Button(
            button_frame,
            text="New Text",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=10,
            command=self.load_new_text
        )
        self.new_text_button.pack(side="left", padx=10)
        
        # Stats display
        stats_frame = tk.Frame(self.root, bg="#f0f0f0")
        stats_frame.pack(pady=20, padx=40, fill="x")
        
        self.wpm_label = tk.Label(
            stats_frame,
            text="WPM: 0",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.wpm_label.pack(side="left")
        
        self.accuracy_label = tk.Label(
            stats_frame,
            text="Accuracy: 100%",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.accuracy_label.pack(side="right")
        
        self.time_label = tk.Label(
            stats_frame,
            text="Time: 0s",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.time_label.pack()  
  
    def load_new_text(self):
        """Load a new random text for typing practice"""
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(state="normal")
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(1.0, self.current_text)
        self.text_display.config(state="disabled")
        
        # Reset highlighting
        self.text_display.tag_remove("correct", 1.0, tk.END)
        self.text_display.tag_remove("incorrect", 1.0, tk.END)
        self.text_display.tag_config("correct", background="#c8e6c9")
        self.text_display.tag_config("incorrect", background="#ffcdd2")
    
    def start_test(self):
        """Start the typing test"""
        self.is_test_active = True
        self.start_time = time.time()
        self.typed_characters = 0
        self.correct_characters = 0
        
        # Enable input and focus
        self.input_text.config(state="normal")
        self.input_text.delete(1.0, tk.END)
        self.input_text.focus()
        
        # Update button states
        self.start_button.config(state="disabled")
        
        # Start updating stats
        self.update_stats()
    
    def reset_test(self):
        """Reset the test to initial state"""
        self.is_test_active = False
        self.start_time = None
        self.typed_characters = 0
        self.correct_characters = 0
        
        # Clear input
        self.input_text.config(state="normal")
        self.input_text.delete(1.0, tk.END)
        self.input_text.config(state="disabled")
        
        # Reset stats
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 100%")
        self.time_label.config(text="Time: 0s")
        
        # Reset button states
        self.start_button.config(state="normal")
        
        # Clear highlighting
        self.text_display.config(state="normal")
        self.text_display.tag_remove("correct", 1.0, tk.END)
        self.text_display.tag_remove("incorrect", 1.0, tk.END)
        self.text_display.config(state="disabled")
    
    def on_key_press(self, event):
        """Handle key press events"""
        if not self.is_test_active:
            return "break"
        
        # Don't count special keys
        if len(event.char) != 1:
            return
        
        self.typed_characters += 1
    
    def on_key_release(self, event):
        """Handle key release events to update highlighting"""
        if not self.is_test_active:
            return
        
        self.update_highlighting()
        
        # Check if test is complete
        typed_text = self.input_text.get(1.0, tk.END).rstrip('\n')
        if typed_text == self.current_text:
            self.complete_test()
    
    def update_highlighting(self):
        """Update text highlighting based on typed input"""
        typed_text = self.input_text.get(1.0, tk.END).rstrip('\n')
        
        # Clear previous highlighting
        self.text_display.config(state="normal")
        self.text_display.tag_remove("correct", 1.0, tk.END)
        self.text_display.tag_remove("incorrect", 1.0, tk.END)
        
        self.correct_characters = 0
        
        # Highlight character by character
        for i, char in enumerate(typed_text):
            if i < len(self.current_text):
                start_pos = f"1.{i}"
                end_pos = f"1.{i+1}"
                
                if char == self.current_text[i]:
                    self.text_display.tag_add("correct", start_pos, end_pos)
                    self.correct_characters += 1
                else:
                    self.text_display.tag_add("incorrect", start_pos, end_pos)
        
        self.text_display.config(state="disabled")
    
    def update_stats(self):
        """Update WPM, accuracy, and time statistics"""
        if not self.is_test_active:
            return
        
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        
        # Update time
        self.time_label.config(text=f"Time: {elapsed_time:.1f}s")
        
        # Calculate WPM (words per minute)
        if elapsed_time > 0:
            typed_text = self.input_text.get(1.0, tk.END).rstrip('\n')
            words_typed = len(typed_text.split())
            wpm = (words_typed / elapsed_time) * 60
            self.wpm_label.config(text=f"WPM: {wpm:.1f}")
        
        # Calculate accuracy
        if self.typed_characters > 0:
            accuracy = (self.correct_characters / self.typed_characters) * 100
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
        
        # Schedule next update
        if self.is_test_active:
            self.root.after(100, self.update_stats)
    
    def complete_test(self):
        """Handle test completion"""
        self.is_test_active = False
        
        # Calculate final stats
        elapsed_time = time.time() - self.start_time
        typed_text = self.input_text.get(1.0, tk.END).rstrip('\n')
        words_typed = len(typed_text.split())
        wpm = (words_typed / elapsed_time) * 60 if elapsed_time > 0 else 0
        accuracy = (self.correct_characters / self.typed_characters) * 100 if self.typed_characters > 0 else 100
        
        # Show completion message
        messagebox.showinfo(
            "Test Complete!",
            f"Congratulations! You completed the test!\n\n"
            f"Final Results:\n"
            f"WPM: {wpm:.1f}\n"
            f"Accuracy: {accuracy:.1f}%\n"
            f"Time: {elapsed_time:.1f} seconds\n"
            f"Characters typed: {self.typed_characters}"
        )
        
        # Disable input
        self.input_text.config(state="disabled")
        self.start_button.config(state="normal")

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()