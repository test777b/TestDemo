import tkinter as tk
import pandas as pd
from tkinter import messagebox

class StoreInventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Inventory App")
        
        self.data = pd.DataFrame(columns=["Product", "Inventory", "Sales", "Refunds"])
        
        # Create GUI elements
        self.label = tk.Label(root, text="Product:")
        self.label.pack()
        
        self.product_entry = tk.Entry(root)
        self.product_entry.pack()
        
        self.inventory_button = tk.Button(root, text="Enter Inventory", command=self.enter_inventory)
        self.inventory_button.pack()
        
        self.sales_button = tk.Button(root, text="Enter Sales", command=self.enter_sales)
        self.sales_button.pack()
        
        self.refund_button = tk.Button(root, text="Enter Refunds", command=self.enter_refunds)
        self.refund_button.pack()
        
        self.view_button = tk.Button(root, text="View Data", command=self.view_data)
        self.view_button.pack()

    def enter_inventory(self):
        product = self.product_entry.get()
        if product:
            self.data.loc[len(self.data)] = [product, 0, 0, 0]
            messagebox.showinfo("Success", f"{product} inventory entered.")
        else:
            messagebox.showwarning("Error", "Please enter a product name.")
    
    def enter_sales(self):
        # Similar logic to enter sales data
        pass
    
    def enter_refunds(self):
        # Similar logic to enter refunds data
        pass
    
    def view_data(self):
        data_viewer = tk.Toplevel(self.root)
        data_viewer.title("View Data")
        
        text = tk.Text(data_viewer)
        text.pack()
        text.insert(  tk.END, str(self.data)  )   

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreInventoryApp(root)
    root.mainloop()






