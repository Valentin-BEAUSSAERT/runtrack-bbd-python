import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from product_database import ProductDatabase

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau de bord de gestion des stocks")
        self.database = ProductDatabase("localhost", "root", "SQL12345", "shop")
        self.create_widgets()
        self.fetch_products_callback()

    def create_widgets(self):
        ttk.Label(self.root, text="Nom:").pack()
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()

        ttk.Label(self.root, text="Description:").pack()
        self.description_entry = ttk.Entry(self.root)
        self.description_entry.pack()

        ttk.Label(self.root, text="Prix:").pack()
        self.price_entry = ttk.Entry(self.root)
        self.price_entry.pack()

        ttk.Label(self.root, text="Quantité:").pack()
        self.quantity_entry = ttk.Entry(self.root)
        self.quantity_entry.pack()

        ttk.Label(self.root, text="Catégorie:").pack()
        # Par exemple : categories_dict = {1: "Accessoires", 2: "Vêtements", 3: "Collaborations"}
        self.category_combobox = ttk.Combobox(self.root, values=[1, 2, 3])
        self.category_combobox.pack()

        self.add_button = ttk.Button(self.root, text="Ajouter le produit", command=self.add_product_callback)
        self.add_button.pack()
#

#Treeview pour l'affichage des produits
        self.product_tree = ttk.Treeview(self.root, columns=("ID", "Name", "Description", "Price", "Quantity", "Category"), show='headings')
        self.product_tree.heading("ID", text="ID")
        self.product_tree.heading("Name", text="Nom")
        self.product_tree.heading("Description", text="Description")
        self.product_tree.heading("Price", text="Prix")
        self.product_tree.heading("Quantity", text="Quantité")
        self.product_tree.heading("Category", text="Category")
        self.product_tree.pack()

#Bouton pour la suppression et la mise à jour
        self.update_button = ttk.Button(self.root, text="Mettre à jour le produit sélectionné", command=self.update_product_callback)
        self.update_button.pack()
        self.delete_button = ttk.Button(self.root, text="Supprimer le produit sélectionné", command=self.delete_product_callback)
        self.delete_button.pack()


    def add_product_callback(self):
    # Ajout d'un produit à la base de données
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_combobox.get()
        

        if not name or not description or not price or not quantity or not category:
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
            return
        
        try:
            price = int(price)
            quantity = int(quantity)
        except ValueError:
            messagebox.showwarning("Attention", "Le prix doit être un nombre et la quantité un entier.")
            return

    # Appel à la base de données
        if self.database.add_product(name, description, price, quantity, category):
            messagebox.showinfo("Succès", "Produit ajouté avec succès")
            self.fetch_products_callback()  # Actualiser l'affichage
        else:
            messagebox.showerror("Erreur", "Impossible d'ajouter le produit")


    def delete_product_callback(self):
        # Suppression du produit sélectionné de la base de données
        selected_item = self.product_tree.selection()[0]
        product_id = self.product_tree.item(selected_item)['values'][0]
        
        if self.database.delete_product(product_id):
            messagebox.showinfo("Succès", "Produit supprimé avec succès")
            self.fetch_products_callback()  # Actualiser l'affichage
        else:
            messagebox.showerror("Erreur", "Impossible de supprimer le produit")


    def update_product_callback(self):
        selected_item = self.product_tree.selection()
        if selected_item:  # Vérifiez qu'un élément est bien sélectionné
            selected_item = selected_item[0]
            product_id = self.product_tree.item(selected_item)['values'][0]

            new_values = {'name': 'New Name', 'description': 'New Description', 'price': 20.99, 'quantity': 15, 'category': 'New Category'}
            
            if self.database.update_product(product_id, **new_values):
                messagebox.showinfo("Succès", "Produit mis à jour avec succès")
                self.fetch_products_callback()
            else:
                messagebox.showerror("Erreur", "La mise à jour du produit a échoué")
        else:
            messagebox.showwarning("Sélectionnez un produit", "Veuillez sélectionner un produit à mettre à jour")


    def fetch_products_callback(self):
        # Récupération et affichage des produits
        for i in self.product_tree.get_children():
            self.product_tree.delete(i)
        
        products = self.database.fetch_products()
        for product in products:
            self.product_tree.insert('', 'end', values=product)



def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

