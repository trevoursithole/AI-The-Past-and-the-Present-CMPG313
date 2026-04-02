import threading
import tkinter as tk
from tkinter import scrolledtext
from eliza import get_eliza_response
from LLM import get_llm_response

class ChatComparisonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CMPG 313: ELIZA vs LLM Comparison")
        self.root.geometry("1200x700")
        self.root.configure(bg="#0f172a")
        self.build_ui()

    def build_ui(self):
        # Header section
        title = tk.Label(self.root, text="AI Comparison Lab", font=("Segoe UI", 22, "bold"), fg="white", bg="#0f172a")
        title.pack(pady=(15, 5))

        top_frame = tk.Frame(self.root, bg="#0f172a")
        top_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Left Panel: ELIZA (Past AI)
        self.eliza_frame = tk.Frame(top_frame, bg="#1e293b")
        self.eliza_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        tk.Label(self.eliza_frame, text="ELIZA (Rule-Based)", font=("Segoe UI", 14), fg="white", bg="#1e293b").pack(pady=5)
        self.eliza_chat = scrolledtext.ScrolledText(self.eliza_frame, wrap=tk.WORD, bg="#0b1220", fg="#e2e8f0")
        self.eliza_chat.pack(fill="both", expand=True, padx=10, pady=10)

        # Right Panel: LLM (Present AI)
        self.llm_frame = tk.Frame(top_frame, bg="#1e293b")
        self.llm_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        tk.Label(self.llm_frame, text="Modern LLM (Contextual)", font=("Segoe UI", 14), fg="white", bg="#1e293b").pack(pady=5)
        self.llm_chat = scrolledtext.ScrolledText(self.llm_frame, wrap=tk.WORD, bg="#0b1220", fg="#e2e8f0")
        self.llm_chat.pack(fill="both", expand=True, padx=10, pady=10)

        # Input Area
        self.input_box = tk.Entry(self.root, font=("Segoe UI", 13))
        self.input_box.pack(fill="x", padx=20, pady=10)
        self.input_box.bind("<Return>", self.send_message)

    def append_text(self, widget, text):
        widget.config(state="normal")
        widget.insert(tk.END, text + "\n\n")
        widget.see(tk.END)
        widget.config(state="disabled")

    def send_message(self, event=None):
        user_text = self.input_box.get().strip()
        if not user_text: return
        self.input_box.delete(0, tk.END)

        self.append_text(self.eliza_chat, f"You: {user_text}")
        self.append_text(self.llm_chat, f"You: {user_text}")

        # ELIZA response [cite: 19]
        self.append_text(self.eliza_chat, f"ELIZA: {get_eliza_response(user_text)}")

        # LLM response (threaded to avoid freezing) [cite: 36]
        self.append_text(self.llm_chat, "LLM: Thinking...")
        threading.Thread(target=self.run_llm, args=(user_text,), daemon=True).start()

    def run_llm(self, user_text):
        response = get_llm_response(user_text)
        self.root.after(0, self.update_llm_ui, response)

    def update_llm_ui(self, response):
        self.llm_chat.config(state="normal")
        # Logic to replace "Thinking..." with actual text
        self.append_text(self.llm_chat, f"LLM: {response}")
        self.llm_chat.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatComparisonGUI(root)
    root.mainloop()