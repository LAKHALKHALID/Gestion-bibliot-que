from tkinter import *
from tkinter import ttk, messagebox
from bibliotéque import Livre,Utilisateur,Emprinter ,Rendre

# Create interface princial.
window=Tk()
window.title("Interface principal")
window.geometry("400x200")
def open_form_livre():
  # Start function ajouter
  def ajouter():
    titre=t.get()
    auteur=a.get()
    prix=p.get()
    l=Livre(titre,auteur,prix)
    Livre.ajouter(l)
    Emprinter.livres.append(l)
    afficher()
    messagebox.showinfo("Message","Livre ajouté avec succès")
  # End function ajouter

  # Start function afficher
  def afficher():
    clear_table()
    for l in Livre.list_livres:
      table.insert("","end",values=(l.titre,l.auteur,l.prix))
  # End function afficher

  # Start function Clear_table
  def clear_table():
    for el in table.get_children():
      table.delete(el)
  # End function Clear_table

  # Star function delet
  def delet(): 
    clear_table()
    titre=t.get()
    for l in Livre.list_livres:
      if l.titre==titre:
        Livre.list_livres.remove(l)
        Emprinter.livres.remove(l)
    afficher()
    messagebox.showinfo("Delet","Delet Livre succes!!")
  # End function delet
  window_livre=Toplevel(window)
  window_livre.title("Information Livre")
  window_livre.geometry("800x400")

  l1=Label(window_livre,text="Entre le titre : ").grid(row=0,column=0)
  l2=Label(window_livre,text="Entre l'auteur : ").grid(row=1,column=0)
  l3=Label(window_livre,text="Entre prix : ").grid(row=2,column=0)

  t=Entry(window_livre)
  a=Entry(window_livre)
  p=Spinbox(window_livre,from_=1,to=1000)
  t.grid(row=0,column=1)
  a.grid(row=1,column=1)
  p.grid(row=2,column=1)

  aj_btn=Button(window_livre,text="Ajouter",bg="green",command=ajouter).grid(row=3,column=0)
  af_btn=Button(window_livre,text="Afficher",bg="blue",command=afficher).grid(row=3,column=1)
  del_btn=Button(window_livre,text="Delet",bg="red",command=delet).grid(row=4,column=0)
  cher_btn=Button(window_livre,text="Chercher",bg="yellow").grid(row=4,column=1)

  table=ttk.Treeview(window_livre,columns=("Titre","Auteur","Prix"),show="headings")
  table.grid(row=5,column=1)
  table.heading("Titre",text="Titre")
  table.heading("Auteur",text="Auteur")
  table.heading("Prix",text="Prix")

def open_form_user():
  window_user=Toplevel(window)
  window_user.title("Information User")
  window_user.geometry("800x400")

  # Start function ajouter
  def ajouter():
    name=n.get()
    age=a.get()
    tel=t.get()
    u=Utilisateur(name,age,tel)
    Utilisateur.ajouter(u)
    Emprinter.users.append(u)
    afficher()
    messagebox.showinfo("Message",f"Ajouter user {name} succes!!")
  # End function ajouter

  # Start function afficher
  def afficher():
    clear_tabel()
    for u in Utilisateur.list_users:
      table.insert("","end",values=(u.name,u.age,u.tel))
  # End function afficher

  # Start function clear_tabel
  def clear_tabel():
    for u in table.get_children():
      table.delete(u)
  # End function clear_table

  # Start function delet 
  def delet():
    clear_tabel()
    name=n.get()
    for u in Utilisateur.list_users:
      if u.name==name:
        Utilisateur.list_users.remove(u)
        Emprinter.users.remove(u)
    afficher()
    messagebox.showinfo("Delet",f"Delet user {name} succes!!")
  # End function delet

  # Start Create interface own historique
  def open_form_historique():
    window_historique=Toplevel(window_user)
    window_historique.title("Historique")
    window_historique.geometry("800x400")

    table=ttk.Treeview(window_historique,columns=("Titre","Auteur","Prix"),show="headings")
    table.grid(row=0,column=0)
    table.heading("Titre",text="Titre")
    table.heading("Auteur",text="Auteur")
    table.heading("Prix",text="Prix")

    nom=n.get()
    for user in Emprinter.users:
      if user.name==nom:
        for livre in user.historique:
          table.insert("","end",values=(livre.titre,livre.auteur,livre.prix))




  # End Create interface own historique


  l1=Label(window_user,text="Entre your name : ").grid(row=0,column=0)
  l2=Label(window_user,text="Entre your age : ").grid(row=1,column=0)
  l3=Label(window_user,text="Entre your tel : ").grid(row=2,column=0)

  n=Entry(window_user)
  a=Spinbox(window_user,from_=1,to=100)
  t=Entry(window_user)
  n.grid(row=0,column=1)
  a.grid(row=1,column=1)
  t.grid(row=2,column=1)

  table=ttk.Treeview(window_user,columns=("Name","Age","Tel"),show="headings")
  table.grid(row=5,column=1)
  table.heading("Name",text="Name")
  table.heading("Age",text="Age")
  table.heading("Tel",text="Tel")



  aj_btn=Button(window_user,text="Ajouter",bg="green",command=ajouter).grid(row=3,column=0)
  af_btn=Button(window_user,text="Afficher",bg="blue",command=afficher).grid(row=3,column=1)
  del_btn=Button(window_user,text="Delet",bg="red",command=delet).grid(row=4,column=0)
  cher_btn=Button(window_user,text="Historique",bg="yellow",command=open_form_historique).grid(row=4,column=1)

def open_form_charger():
  window_charger=Toplevel(window)
  window_charger.title("Charger les information")
  window_charger.geometry("800x300")
  l1=Label(window_charger,text="Livre : ").grid(row=0,column=0)
  l2=Label(window_charger,text="User : ").grid(row=1,column=0)

  li_livre=[]
  for livre in Emprinter.livres:
    li_livre.append(livre.titre)
  
  li_user=[]
  for user in Emprinter.users:
    li_user.append(user.name)

  spin_l=ttk.Combobox(window_charger,values=li_livre)
  spin_u=ttk.Combobox(window_charger,values=li_user)

  table=ttk.Treeview(window_charger,columns=("Name","Age","Tel"),show="headings")
  table.grid(row=4,column=1)
  table.heading("Name",text="Name")
  table.heading("Age",text="Age")
  table.heading("Tel",text="Tel")


  def charger():
    for user in Emprinter.users:
      if user.name==spin_u.get():
        # user.historique.append()
        for livre in Emprinter.livres:
          if livre.titre==spin_l.get():
            user.historique.append(livre)
            messagebox.showinfo("Message","Add livre to historique!!")

  def shearch():
    for user in Emprinter.users:

      for el in user.historique:
        messagebox.showinfo("Message","I run")

        if el.titre==spin_l.get():
          # table.insert("","end",values=(el.titre,el.auteur,el.prix))    
          table.insert("","end",values=(user.name,user.age,user.tel))    




  spin_l.grid(row=0,column=1)
  spin_u.grid(row=1,column=1)
  btn_charger=Button(window_charger,text="Charger",command=charger).grid(row=2,column=1)
  btn_shearch=Button(window_charger,text="Shearch",command=shearch).grid(row=3,column=1)






livre_btn=Button(window,bg="orange",text="Livre",command=open_form_livre).grid(row=0,column=1)
user_btn=Button(window,bg="green",text="User",command=open_form_user).grid(row=1,column=1)
emprunter_btn=Button(window,bg="yellow",text="Emprunter",command=open_form_charger).grid(row=3,column=1)
window.mainloop()