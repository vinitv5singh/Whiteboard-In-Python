import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from textblob import TextBlob

def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y

def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y

def stop_drawing(event):
    global is_drawing
    is_drawing = False

def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color

def change_line_width(value):
    global line_width
    line_width = int(value)

def analyze_sentiment():
    note = text_widget.get("1.0", tk.END).strip()
    if note:
        blob = TextBlob(note)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        messagebox.showinfo("Sentiment Analysis", f"Sentiment: {sentiment} (Polarity: {polarity:.2f})")
    else:
        messagebox.showwarning("Empty Note", "Please enter some notes first.")

def suggest_drawing():
    note = text_widget.get("1.0", tk.END).strip().lower()
    canvas.delete("all")
    if "sun" in note:
        canvas.create_oval(100, 100, 200, 200, fill="yellow", outline="orange", width=4)
    elif "tree" in note:
        canvas.create_rectangle(140, 200, 160, 300, fill="brown")
        canvas.create_oval(100, 150, 200, 250, fill="green")
    elif "house" in note:
        canvas.create_rectangle(100, 200, 200, 300, fill="blue")
        canvas.create_polygon(100, 200, 200, 200, 150, 150, fill="red")
    else:
        messagebox.showinfo("Suggestion", "No suggestion available for your input.")

# Main GUI setup
root = tk.Tk()
root.title("AI Whiteboard")
root.geometry("800x600")

canvas = tk.Canvas(root, bg="grey")
canvas.pack(fill="both", expand=True)

is_drawing = False
drawing_color = "black"
line_width = 2

controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")

color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))
sentiment_button = tk.Button(controls_frame, text="Analyze Sentiment", command=analyze_sentiment)
suggest_button = tk.Button(controls_frame, text="Suggest Drawing", command=suggest_drawing)

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)
sentiment_button.pack(side="left", padx=5, pady=5)
suggest_button.pack(side="left", padx=5, pady=5)

line_width_label = tk.Label(controls_frame, text="Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=change_line_width)
line_width_slider.set(line_width)
line_width_slider.pack(side="left", padx=5, pady=5)

text_widget_label = tk.Label(controls_frame, text="Notes:")
text_widget_label.pack(side="left", padx=5, pady=5)

text_widget = tk.Text(controls_frame, height=6, width=50)
text_widget.pack(side="left", padx=5, pady=5)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()



