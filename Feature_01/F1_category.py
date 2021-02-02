# Maintain a list of product/toy categories:
# • Add a category:
#   - Administrators should be able to enter a category code and name, then add the category to a database;
#     prompt administrators if the category already exists
# • Edit a category:
#   - Administrators should be able to select a category from available categories, edit its name and update
#     the database
# • Delete a category:
#   - Administrators should be able to select a category then delete its record from the database.

from tkinter import *
from tkinter import ttk
import Feature_01.F1_database
import sqlite3
from tkinter import messagebox


# Main Class
class Category:
    def __init__(self, master):
        self.master = master

        # Variables for Functions
        self.category_id = StringVar()
        self.category_name = StringVar()

        # Implementing Function to Clear the Entries
        def clear():
            self.ctg_entry.delete(0, END)
            self.name_entry.delete(0, END)

        # Implementing Function for Add Button
        def add_data():
            try:
                if self.category_id.get() == "" or self.category_name.get() == "":
                    messagebox.showinfo("Warning!", "Enter All Field")
                else:
                    Feature_01.F1_database.add_category(self.category_id.get(), self.category_name.get())
            except sqlite3.IntegrityError:
                messagebox.showerror("Warning!", "Category Already Exist!")
            clear()

        # Implementing Function for Display Button
        def display_data():
            result = Feature_01.F1_database.view_data()
            self.category_list.delete(*self.category_list.get_children())
            for row in result:
                self.category_list.insert('', END, values=row)

        # Implementing Function for Delete Button
        def delete_data():
            cg_id = self.category_id.get()
            con = sqlite3.connect("./AAT_Data.db")
            cur = con.cursor()
            if messagebox.askyesno("Confirm Delete!", "Are You Sure You Want To Delete This Category?"):
                cur.execute("DELETE FROM category WHERE id= " + cg_id)
                clear()
                con.commit()
                con.close()
            else:
                return True

        # Implementing Function for Update Button
        def update_data():
            edit_id = self.category_id.get()
            edit_name = self.category_name.get()
            con = sqlite3.connect("./AAT_Data.db")
            cur = con.cursor()
            if messagebox.askyesno("Confirm Please!", "Are You Sure You Want to Update This Category?"):
                cur.execute("UPDATE category SET category_name=? WHERE id=?", (edit_name, edit_id,))
                clear()
                con.commit()
                con.close()
            else:
                return True

        # Implementing Function for Adding Data on the Treeview
        def category_rec(event):
            item = self.category_list.item(self.category_list.focus())
            self.category_id.set(item['values'][0])
            self.category_name.set(item['values'][1])

        # Frames
        main_frame = Frame(self.master, bd=10, width=1350, height=700, relief=RIDGE, bg="cadet blue")
        main_frame.grid()

        top_frame1 = Frame(main_frame, bd=5, width=1340, height=50, relief=RIDGE)
        top_frame1.grid(row=2, column=0, pady=8)
        tittle_frame = Frame(main_frame, bd=7, width=1340, height=100, relief=RIDGE)
        tittle_frame.grid(row=0, column=0)
        top_frame3 = Frame(main_frame, bd=5, width=1840, height=500, relief=RIDGE)
        top_frame3.grid(row=1, column=0, sticky=W)

        left_frame = Frame(top_frame3, bd=5, width=1340, height=400, padx=2, bg="cadet blue", relief=RIDGE)
        left_frame.pack(side=LEFT)
        left_frame1 = Frame(left_frame, bd=5, width=600, height=100, padx=2, pady=4, relief=RIDGE)
        left_frame1.pack(side=TOP, padx=0, pady=4)

        right_frame1 = Frame(top_frame3, bd=5, width=320, height=400, padx=2, bg="cadet blue", relief=RIDGE)
        right_frame1.pack(side=RIGHT)
        right_frame1a = Frame(right_frame1, bd=5, width=310, height=200, padx=2, pady=2, relief=RIDGE)
        right_frame1a.pack(side=TOP)

        # Tittle Frame
        self.tittle_label = Label(tittle_frame, font=('arial', 33, 'bold'), text="Category Management",
                                  bd=7)
        self.tittle_label.grid(row=0, column=0, padx=70)

        # Widget
        self.ctg_label = Label(left_frame1, font=('arial', 12, 'bold'), text="Category ID: ", bd=7, anchor=W,
                               justify=LEFT)
        self.ctg_label.grid(row=0, column=0, sticky=W, padx=5)
        self.ctg_entry = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=30, justify=LEFT,
                               textvariable=self.category_id)
        self.ctg_entry.grid(row=0, column=1)

        self.name_label = Label(left_frame1, font=('arial', 12, 'bold'), text="Category Name: ", bd=7, anchor=W,
                                justify=LEFT)
        self.name_label.grid(row=1, column=0, sticky=W, padx=5)
        self.name_entry = Entry(left_frame1, font=('arial', 12, 'bold'), bd=7, width=30, justify=LEFT,
                                textvariable=self.category_name)
        self.name_entry.grid(row=1, column=1)

        # Treeview
        # Scroll Bar Function
        scroll_y = Scrollbar(right_frame1a, orient=VERTICAL)

        self.category_list = ttk.Treeview(right_frame1a, height=20, column=("Category ID", 'Category Name'),
                                          yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        # Treeview Heading and Column
        self.category_list.heading("Category ID", text="Category ID")
        self.category_list.heading("Category Name", text="Category Name")

        self.category_list['show'] = 'headings'

        self.category_list.column("Category ID", width=180, anchor=CENTER)
        self.category_list.column("Category Name", width=194, anchor=CENTER)

        self.category_list.pack(fill=BOTH, expand=1)
        self.category_list.bind("<ButtonRelease-1>", category_rec)

        # Button
        self.add_bt = Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text="Add", width=10, height=2,
                             command=add_data).grid(row=0, column=0, padx=1)
        self.display_bt = Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text="Display", width=11,
                                 height=2, command=display_data).grid(row=0, column=1, padx=1)
        self.delete_bt = Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text="Delete", width=11,
                                height=2, command=delete_data).grid(row=0, column=2, padx=1)
        self.update_bt = Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text="Update", width=10,
                                height=2, command=update_data).grid(row=0, column=3, padx=1)


if __name__ == '__main__':
    root = Tk()
    root.title("Category Database Management System")
    root.geometry("689x433")
    application = Category(root)
    root.mainloop()
