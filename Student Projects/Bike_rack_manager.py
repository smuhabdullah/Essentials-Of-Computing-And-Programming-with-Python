import tkinter as tk
from tkinter import messagebox, simpledialog

# Sample data of bikes
bikes = [
    {'name': 'HONDA 125 Bike', 'color': 'RED', 'price': 234900, 'model': 'NEW', 'quantity': 15},
    {'name': 'SUPER POWER Bike', 'color': 'BLACK', 'price': 112500, 'model': 'NEW', 'quantity': 13},
    {'name': 'SUPER STAR Bike', 'color': 'RED', 'price': 250000, 'model': 'NEW', 'quantity': 17},
    {'name': 'UNIQUE Bike', 'color': 'BLACK', 'price': 114500, 'model': 'NEW', 'quantity': 10},
    {'name': 'YAMAHA Bike', 'color': 'BLUE', 'price': 396000, 'model': 'NEW', 'quantity': 20},
    {'name': 'KAWASAKI Bike', 'color': 'GREEN', 'price': 500000, 'model': 'NEW', 'quantity': 15},
    {'name': 'KTM Bike', 'color': 'ORANGE', 'price': 149000, 'model': 'NEW', 'quantity': 13},
    {'name': 'UNION STAR Bike', 'color': 'RED', 'price': 125000, 'model': 'NEW', 'quantity': 17},
]

class BikeShowroomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bike Showroom Sale Management System")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.master, text="Bike Showroom", font=("Arial", 20, "bold"), bg="orange", fg="blue", pady=10)
        self.title_label.pack(fill=tk.X)
        
        # Frame to hold listbox and buttons
        self.frame = tk.Frame(self.master, bg="purple")
        self.frame.pack(pady=10, padx=20)
        
        # Listbox to display bike names
        self.bike_listbox = tk.Listbox(self.frame, width=50,bg="yellow", height=10, font=("Arial", 12), bd=0)
        self.bike_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
        
        # Add bike names to the listbox
        for bike in bikes:
            self.bike_listbox.insert(tk.END, bike['name'])
        
        # Button to view bike details
        self.view_details_button = tk.Button(self.frame, text="View Details", command=self.view_details, bg="#007bff", fg="black", bd=0, padx=10, pady=5, font=("Arial", 12))
        self.view_details_button.pack(side=tk.LEFT, padx=5)
        
        # Button to make a sale
        self.sell_button = tk.Button(self.frame, text="Sale", command=self.make_sale, bg="#28a745", fg="black", bd=0, padx=10, pady=5, font=("Arial", 12))
        self.sell_button.pack(side=tk.LEFT, padx=5)
        
        # Button to add inventory
        self.add_inventory_button = tk.Button(self.frame, text="Add Inventory", command=self.add_inventory, bg="#17a2b8", fg="black", bd=0, padx=10, pady=5, font=("Arial", 12))
        self.add_inventory_button.pack(side=tk.LEFT, padx=5)
        
        # Button to create bill
        self.bill_button = tk.Button(self.frame, text="Create Bill", command=self.create_bill, bg="#ffc107", fg="black", bd=0, padx=10, pady=5, font=("Arial", 12))
        self.bill_button.pack(side=tk.LEFT, padx=5)
        
        # Button to close the app
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit, bg="#dc3545", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        self.quit_button.pack(pady=10)
        
    def view_details(self):
        # Get the selected bike
        selected_index = self.bike_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a bike first.")
            return
        selected_index = selected_index[0]
        selected_bike = bikes[selected_index]
        
        # Display bike details
        messagebox.showinfo("Bike Details", f"Name: {selected_bike['name']}\nColor: {selected_bike['color']}\nPrice: PKR {selected_bike['price']}\nModel: {selected_bike['model']}\nQuantity: {selected_bike['quantity']}")
    
    def make_sale(self):
        # Get the selected bike
        selected_index = self.bike_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a bike first.")
            return
        selected_index = selected_index[0]
        selected_bike = bikes[selected_index]
        
        # Check if bike is available
        if selected_bike['quantity'] <= 0:
            messagebox.showerror("Error", "This bike is out of stock.")
            return
        
        # Decrease the quantity of the bike
        selected_bike['quantity'] -= 1
        
        # Update the listbox
        self.bike_listbox.delete(selected_index)
        self.bike_listbox.insert(selected_index, f"{selected_bike['name']} - {selected_bike['quantity']} left")
        
        # Show sale confirmation
        messagebox.showinfo("Sale Confirmation", "Sale successful.")
    
    def create_bill(self):
        # Get the selected bike
        selected_index = self.bike_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a bike first.")
            return
        selected_index = selected_index[0]
        selected_bike = bikes[selected_index]

        # Prompt user to enter your name
        customer_name = self.get_customer_name()
        if not customer_name :
            return  # If the user cancels, do nothing
        
        

        # Prompt user to enter delivery address
        delivery_address = self.get_delivery_address()
        if not delivery_address:
            return  # If the user cancels, do nothing

        # Display the bill with the delivery address
        bill = f"\nCUSTOMER NAME:{customer_name}  \nBike: {selected_bike['name']}\nColor: {selected_bike['color']}\nPrice: PKR {selected_bike['price']}\nModel: {selected_bike['model']}\nDelivery Address: {delivery_address}"
        messagebox.showinfo("Bill", bill)

       
    def add_inventory(self):
        # Get the selected bike
        selected_index = self.bike_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a bike first.")
            return
        selected_index = selected_index[0]
        selected_bike = bikes[selected_index]
        
        # Add inventory
        selected_bike['quantity'] += 1
        
        # Update the listbox
        self.bike_listbox.delete(selected_index)
        self.bike_listbox.insert(selected_index, f"{selected_bike['name']} - {selected_bike['quantity']} left")
        
        # Show inventory update confirmation
        messagebox.showinfo("Inventory Update", "Inventory added successfully.")
    
    def get_customer_name(self):
        # Function to get customer name
        customer_name = simpledialog.askstring("CUSTOMER NAME", "PLEASE ENTER YOUR NAME:")
        return customer_name

    
    def get_contact_details(self):
        # Function to get contact details
        contact_details = simpledialog.askstring("CONTACT ", "Please enter your contact number:")
        return contact_details
    
    def get_delivery_address(self):
        # Function to get delivery address
        delivery_address = simpledialog.askstring("Delivery Address", "Please enter the delivery address:")
        return delivery_address

# Main function
def main():
    root = tk.Tk()
    app = BikeShowroomApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
