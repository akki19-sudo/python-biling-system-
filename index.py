import datetime
from tkinter import *
from tkinter import messagebox

class LoginPage:
    def __init__(self, win):
        self.win = win
        self.win.title("Restaurant Management System")
        self.win.geometry("1350x750+0+0")

        self.title_label = Label(self.win, text="Restaurant Management System", font=("Arial", 25, 'bold'), bg='lightgray', bd=8, relief="groove")
        self.title_label.pack(side=TOP, fill=X)

        self.main_frame = Frame(self.win, bg="lightgray", bd=4, relief="groove")
        self.main_frame.place(x=450, y=200, width=450, height=400)

        self.entry_frame = LabelFrame(self.main_frame, text="Enter Details", bd=6, relief="groove", bg="lightgray", font=("sans-serif", 10))
        self.entry_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.username_label = Label(self.entry_frame, text="Username:-", font=("Arial", 14), bg="lightgray", bd=4)
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = Entry(self.entry_frame, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = Label(self.entry_frame, text="Password:-", font=("Arial", 14), bg="lightgray", bd=4)
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = Entry(self.entry_frame, font=("Arial", 14), show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.button_frame = Frame(self.main_frame, bg="lightgray")
        self.button_frame.pack(pady=20)

        self.login_button = Button(self.button_frame, text="Login", font=("Arial", 14), bg="green", fg="white", command=self.login)
        self.login_button.grid(row=0, column=0, padx=20, pady=10)

        self.billing_button = Button(self.button_frame, text="Billing", font=("Arial", 14), bg="blue", fg="white", state="disabled", command=self.open_billing_window)
        self.billing_button.grid(row=0, column=1, padx=20, pady=10)

        self.reset_button = Button(self.button_frame, text="Reset", font=("Arial", 14), bg="red", fg="white", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=20, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "user" and password == "password":
            print(f"Login Successful: {username}")
            self.billing_button.config(state="normal")
        else:
            print("Invalid credentials")
            self.billing_button.config(state="disabled")

    def reset(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.billing_button.config(state="disabled")

    def open_billing_window(self):
        billing_window = Toplevel(self.win)
        billing_window.title("Billing System")
        billing_window.geometry("1350x850+0+0")

        billing_frame = Frame(billing_window, bg="lightgray", bd=4, relief="groove")
        billing_frame.place(x=10, y=10, width=900, height=800)

        left_frame = Frame(billing_frame, bg="lightgray")
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+W+E)

        self.bill_number = 1001
        self.bill_number_label = Label(left_frame, text="Bill No:", font=("Arial", 14), bg="lightgray")
        self.bill_number_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.bill_number_value = Label(left_frame, text=str(self.bill_number), font=("Arial", 14), bg="lightgray")
        self.bill_number_value.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.customer_name_label = Label(left_frame, text="Customer Name:", font=("Arial", 14), bg="lightgray")
        self.customer_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.customer_name_entry = Entry(left_frame, font=("Arial", 14))
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.customer_contact_label = Label(left_frame, text="Customer Contact:", font=("Arial", 14), bg="lightgray")
        self.customer_contact_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.customer_contact_entry = Entry(left_frame, font=("Arial", 14))
        self.customer_contact_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        self.date_label = Label(left_frame, text="Date:", font=("Arial", 14), bg="lightgray")
        self.date_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.date_value = Label(left_frame, text=datetime.datetime.now().strftime("%Y-%m-%d"), font=("Arial", 14), bg="lightgray")
        self.date_value.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        self.item_label = Label(left_frame, text="Item Name:", font=("Arial", 14), bg="lightgray")
        self.item_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.item_entry = Entry(left_frame, font=("Arial", 14))
        self.item_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        self.quantity_label = Label(left_frame, text="Quantity:", font=("Arial", 14), bg="lightgray")
        self.quantity_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.quantity_entry = Entry(left_frame, font=("Arial", 14))
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        self.price_label = Label(left_frame, text="Price per Item:", font=("Arial", 14), bg="lightgray")
        self.price_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
        self.price_entry = Entry(left_frame, font=("Arial", 14))
        self.price_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        self.total_label = Label(left_frame, text="Total Price: $0", font=("Arial", 14, 'bold'), bg="lightgray")
        self.total_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky=W)

        self.bill_output_frame = Frame(billing_window, bg="white", bd=4, relief="groove", width=400, height=400)
        self.bill_output_frame.place(x=920, y=50)

        self.bill_output = Text(self.bill_output_frame, wrap=WORD, font=("Courier", 12), bg="lightgray", height=15, width=40)
        self.bill_output.pack(padx=10, pady=10)

        button_frame = Frame(billing_window, bg="lightgray")
        button_frame.place(x=920, y=500, width=400, height=200)

        self.add_button = Button(button_frame, text="Add", font=("Arial", 14), bg="blue", fg="white", command=self.add_item)
        self.add_button.grid(row=0, column=0, padx=20, pady=10)

        self.generate_button = Button(button_frame, text="Generate", font=("Arial", 14), bg="green", fg="white", command=self.generate_bill)
        self.generate_button.grid(row=0, column=1, padx=20, pady=10)

        self.clear_button = Button(button_frame, text="Clear", font=("Arial", 14), bg="orange", fg="white", command=self.clear)
        self.clear_button.grid(row=1, column=0, padx=20, pady=10)

        self.reset_button = Button(button_frame, text="Reset", font=("Arial", 14), bg="red", fg="white", command=self.reset_billing)
        self.reset_button.grid(row=1, column=1, padx=20, pady=10)

        self.print_button = Button(button_frame, text="Print", font=("Arial", 14), bg="purple", fg="white", command=self.print_bill)
        self.print_button.grid(row=2, column=0, padx=20, pady=10)

        self.items = []
        self.total_price = 0
        self.tax_rate = 0.05

    def add_item(self):
        item_name = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        total = quantity * price
        self.items.append((item_name, quantity, price, total))

        self.bill_output.insert(END, f"{item_name:<15} x{quantity:<3} @${price:<5.2f} = ${total:.2f}\n")

        self.total_price += total
        self.total_label.config(text=f"Total Price: ${self.total_price:.2f}")
        self.item_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)

    def generate_bill(self):
        line = "-" * 40
        bill_text = f"{line}\n"
        bill_text += f"{'BILL RECEIPT':^40}\n"
        bill_text += f"{line}\n"
        bill_text += f"Bill No    : {self.bill_number}\n"
        bill_text += f"Date       : {self.date_value.cget('text')}\n"
        bill_text += f"Customer   : {self.customer_name_entry.get()}\n"
        bill_text += f"Contact    : {self.customer_contact_entry.get()}\n"
        bill_text += f"{line}\n"
        bill_text += f"{'Item':<15}{'Qty':<6}{'Price':<8}{'Total':>9}\n"
        bill_text += f"{line}\n"

        for item in self.items:
            item_name, quantity, price, total = item
            bill_text += f"{item_name:<15}{quantity:<6}{price:<8.2f}{total:>9.2f}\n"

        tax = self.total_price * self.tax_rate
        total_amount = self.total_price + tax

        bill_text += f"{line}\n"
        bill_text += f"{'Subtotal':<30}${self.total_price:>8.2f}\n"
        bill_text += f"{'Tax (5%)':<30}${tax:>8.2f}\n"
        bill_text += f"{'Total Amount':<30}${total_amount:>8.2f}\n"
        bill_text += f"{line}\n"
        bill_text += f"{'Thank you for visiting!':^40}\n"
        bill_text += f"{line}"

        self.bill_output.delete(1.0, END)
        self.bill_output.insert(END, bill_text)

    def clear(self):
        self.item_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)

    def reset_billing(self):
        self.customer_name_entry.delete(0, END)
        self.customer_contact_entry.delete(0, END)
        self.item_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.total_price = 0
        self.items.clear()
        self.total_label.config(text="Total Price: $0")
        self.bill_output.delete(1.0, END)

    def print_bill(self):
        bill_content = self.bill_output.get(1.0, END)
        if bill_content.strip() == "":
            messagebox.showwarning("No Bill", "Please generate a bill first!")
        else:
            messagebox.showinfo("Print Bill", "Bill is ready to print!")
            print(bill_content)  # Simulates print

# Main Program
root = Tk()
login_page = LoginPage(root)
root.mainloop()
