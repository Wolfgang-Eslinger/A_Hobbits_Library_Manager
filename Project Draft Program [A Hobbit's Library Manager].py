# Wolfgang Eslinger
# 10/1/2023
# The "A Hobbit's Library Manager" is a GUI application that 
# allows users to search for books, view their borrowed books, 
# and manage book borrowing and returning in a digital library system.

# Import necessary libraries
import tkinter as tk
from tkinter import messagebox, Listbox
import sqlite3

# Database Functions

# Function to create the necessary tables in the database
def create_database():
    # Connect to the SQLite database named 'library.db'
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Create a table for books if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                     (title TEXT, author TEXT, genre TEXT, status TEXT)''')
    
    # Create a table for borrowed books if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books
                     (user TEXT, title TEXT, due_date DATE)''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# GUI Functions

# Function to display the main window of the application
def main_window():
    # Create the main window
    window = tk.Tk()
    window.title("A Hobbit's Library Manager")

    # Create and display labels
    tk.Label(window, text="A Hobbit's Library Manager", font=("Arial", 16)).pack(pady=20)
    tk.Label(window, text="Search Bar", font=("Arial", 12)).pack(pady=10)

    # Create and display the search entry box
    global search_entry
    search_entry = tk.Entry(window, width=30)
    search_entry.pack(pady=10)

    # Create and display buttons
    tk.Button(window, text="Search", command=search_books).pack(pady=10)
    tk.Button(window, text="Borrowed Books", command=borrowed_books_window).pack(pady=10)
    tk.Button(window, text="Exit", command=window.quit).pack(pady=10)

    # Image placeholders ( don't forget you'll need to replace this Mr. Wolfgang with 
    # actual paths)
    # library_logo = tk.PhotoImage(file="path_to_library_logo.png")
    # search_icon = tk.PhotoImage(file="path_to_search_icon.png")

    # Start the main loop to display the window
    window.mainloop()

# Function to display the borrowed books window
def borrowed_books_window():
    # Create the borrowed books window
    borrowed_window = tk.Toplevel()
    borrowed_window.title("Borrowed Books")

    # Create and display labels
    tk.Label(borrowed_window, text="Borrowed Books", font=("Arial", 16)).pack(pady=20)
    tk.Label(borrowed_window, text="List of Borrowed Books", font=("Arial", 12)).pack(pady=10)

    # Create and display the listbox for borrowed books
    borrowed_books_list = Listbox(borrowed_window)
    borrowed_books_list.pack(pady=10)

    # Create and display buttons
    tk.Button(borrowed_window, text="Return Book", command=return_book).pack(pady=10)
    tk.Button(borrowed_window, text="Main Menu", command=borrowed_window.destroy).pack(pady=10)
    tk.Button(borrowed_window, text="Exit", command=borrowed_window.quit).pack(pady=10)

# Placeholder functions for functionality

# Function to handle book search (to be implemented)
def search_books():
    pass

# Function to handle book return (to be implemented)
def return_book():
    pass

# Initialize the database by creating tables
create_database()

# Start the main window of the application
main_window()
