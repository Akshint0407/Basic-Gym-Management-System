import tkinter as tk
from tkinter import messagebox, ttk
from database import add_member, retrieve_members, update_member, delete_member  # Import new functions

def add_member_ui():
    def submit_member():
        full_name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        join_date = entry_join_date.get()
        subscription_type = entry_subscription.get()

        # Call the database function to add member
        add_member(full_name, email, phone, join_date, subscription_type)
        messagebox.showinfo("Success", "Member added successfully!")
        update_member_list()  # Refresh the list after adding

    def update_member_ui():
        selected_item = tree.selection()
        if selected_item:
            # Get existing member data
            member_data = tree.item(selected_item)["values"]
            member_id = member_data[0]  # Assuming the first value is the ID

            # Create a new window for updating
            update_window = tk.Toplevel(window)
            update_window.title("Update Member")

            tk.Label(update_window, text="Full Name").grid(row=0, column=0)
            tk.Label(update_window, text="Email").grid(row=1, column=0)
            tk.Label(update_window, text="Phone Number").grid(row=2, column=0)
            tk.Label(update_window, text="Join Date").grid(row=3, column=0)
            tk.Label(update_window, text="Subscription Type").grid(row=4, column=0)

            # Entry fields with existing member data
            entry_name_update = tk.Entry(update_window)
            entry_email_update = tk.Entry(update_window)
            entry_phone_update = tk.Entry(update_window)
            entry_join_date_update = tk.Entry(update_window)
            entry_subscription_update = tk.Entry(update_window)

            entry_name_update.grid(row=0, column=1)
            entry_email_update.grid(row=1, column=1)
            entry_phone_update.grid(row=2, column=1)
            entry_join_date_update.grid(row=3, column=1)
            entry_subscription_update.grid(row=4, column=1)

            # Pre-fill the entry fields with existing data
            entry_name_update.insert(0, member_data[1])
            entry_email_update.insert(0, member_data[2])
            entry_phone_update.insert(0, member_data[3])
            entry_join_date_update.insert(0, member_data[4])
            entry_subscription_update.insert(0, member_data[5])

            def update_member_confirm():
                full_name = entry_name_update.get()
                email = entry_email_update.get()
                phone = entry_phone_update.get()
                join_date = entry_join_date_update.get()
                subscription_type = entry_subscription_update.get()

                update_member(member_id, full_name, email, phone, join_date, subscription_type)
                messagebox.showinfo("Success", "Member updated successfully!")
                update_member_list()  # Refresh the list after updating
                update_window.destroy()  # Close the update window

            tk.Button(update_window, text="Update Member", command=update_member_confirm).grid(row=5, columnspan=2)

        else:
            messagebox.showwarning("Select Member", "Please select a member to update.")


    def delete_member_ui():
        selected_item = tree.selection()
        if selected_item:
            member_id = tree.item(selected_item)["values"][0]
            delete_member(member_id)
            messagebox.showinfo("Success", "Member deleted successfully!")
            update_member_list()  # Refresh the list after deletion
        else:
            messagebox.showwarning("Select Member", "Please select a member to delete.")

    def update_member_list(search_query=""):
        # Clear the existing list
        for row in tree.get_children():
            tree.delete(row)

        # Retrieve members from the database
        members = retrieve_members(search_query)
        for member in members:
            tree.insert("", "end", values=member)

    def search_member():
        search_query = search_entry.get()
        update_member_list(search_query)

    window = tk.Tk()
    window.title("Gym Management System")

    # Create a tab control
    tab_control = ttk.Notebook(window)

    # Create two tabs
    tab_add = ttk.Frame(tab_control)
    tab_view = ttk.Frame(tab_control)

    tab_control.add(tab_add, text='Add Member')
    tab_control.add(tab_view, text='View Members')

    tab_control.pack(expand=1, fill='both')

    # Add Member Tab
    tk.Label(tab_add, text="Full Name").grid(row=0)
    tk.Label(tab_add, text="Email").grid(row=1)
    tk.Label(tab_add, text="Phone Number").grid(row=2)
    tk.Label(tab_add, text="Join Date").grid(row=3)
    tk.Label(tab_add, text="Subscription Type").grid(row=4)

    entry_name = tk.Entry(tab_add)
    entry_email = tk.Entry(tab_add)
    entry_phone = tk.Entry(tab_add)
    entry_join_date = tk.Entry(tab_add)
    entry_subscription = tk.Entry(tab_add)

    entry_name.grid(row=0, column=1)
    entry_email.grid(row=1, column=1)
    entry_phone.grid(row=2, column=1)
    entry_join_date.grid(row=3, column=1)
    entry_subscription.grid(row=4, column=1)

    tk.Button(tab_add, text="Add Member", command=submit_member).grid(row=5, columnspan=2)

    # View Members Tab
    tk.Label(tab_view, text="Search").grid(row=0, column=0)
    search_entry = tk.Entry(tab_view)
    search_entry.grid(row=0, column=1)
    tk.Button(tab_view, text="Search", command=search_member).grid(row=0, column=2)

    # Treeview to display members
    tree = ttk.Treeview(tab_view, columns=("ID", "Full Name", "Email", "Phone", "Join Date", "Subscription"), show='headings')
    tree.grid(row=1, column=0, columnspan=2)

    # Define column headings
    for col in ("ID", "Full Name", "Email", "Phone", "Join Date", "Subscription"):
        tree.heading(col, text=col)

    # Bind selection event
    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            member_data = tree.item(selected_item)["values"]
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
            entry_join_date.delete(0, tk.END)
            entry_subscription.delete(0, tk.END)

            entry_name.insert(0, member_data[1])
            entry_email.insert(0, member_data[2])
            entry_phone.insert(0, member_data[3])
            entry_join_date.insert(0, member_data[4])
            entry_subscription.insert(0, member_data[5])

    tree.bind('<<TreeviewSelect>>', on_select)

    # Add Update and Delete buttons next to the treeview
    button_frame = tk.Frame(tab_view)
    button_frame.grid(row=1, column=2, padx=10)

    tk.Button(button_frame, text="Update Member", command=update_member_ui).pack(pady=5)
    tk.Button(button_frame, text="Delete Member", command=delete_member_ui).pack(pady=5)

    # Initially load members
    update_member_list()

    window.mainloop()
