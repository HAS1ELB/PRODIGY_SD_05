# web_scraper_gui.py

import tkinter as tk
from tkinter import messagebox
from scraper import scrape_products, save_to_csv

class WebScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        
        # URL Entry
        tk.Label(root, text="Enter URL:").pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        
        # Buttons
        scrape_button = tk.Button(root, text="Scrape", command=self.scrape)
        scrape_button.pack(pady=5)
        save_button = tk.Button(root, text="Save to CSV", command=self.save_to_csv)
        save_button.pack(pady=5)
        
        # Results Display
        self.results_text = tk.Text(root, width=80, height=20)
        self.results_text.pack(pady=10)
        
        self.products = []

    def scrape(self):
        """Scrape data from the URL and display it."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        try:
            self.products = scrape_products(url)
            self.display_results()
            messagebox.showinfo("Success", "Scraping completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_results(self):
        """Display scraped data in the text widget."""
        self.results_text.delete(1.0, tk.END)
        for product in self.products:
            self.results_text.insert(tk.END, f"Name: {product['Name']}\n")
            self.results_text.insert(tk.END, f"Price: {product['Price']}\n")
            self.results_text.insert(tk.END, f"Rating: {product['Rating']}\n")
            self.results_text.insert(tk.END, "-" * 40 + "\n")

    def save_to_csv(self):
        """Save scraped data to a CSV file."""
        if not self.products:
            messagebox.showerror("Error", "No data to save")
            return
        
        save_to_csv(self.products)
        messagebox.showinfo("Success", "Data saved to products.csv")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperGUI(root)
    root.mainloop()
