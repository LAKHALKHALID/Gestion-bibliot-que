class Livre:
  list_livres=[]
  def __init__(self,titre ,auteur ,prix):
    self.titre = titre
    self.auteur = auteur
    self.prix = prix

  @classmethod
  def ajouter(cls,livre):
    cls.list_livres.append(livre)

  @classmethod
  def remove(cls,livre):
    for l in cls.list_livres:
      if l.titre == livre:
        cls.list_livres.remove(l)

  


class Utilisateur:
  list_users=[]
  def __init__(self,name,age ,tel):
    self.name = name
    self.age = age
    self.tel = tel
    self.historique=[]

 
  
  @classmethod
  def ajouter(cls,user):
    cls.list_users.append(user)

  @classmethod
  def remove(cls,user):
    for u in cls.list_users:
      if u.name == user:
        cls.list_users.remove(u)


class Emprinter:
  users=[]
  livres=[]
  def __init__(self):
    pass
    

  
  
  # def historique(cls,name_user,name_liver):
  #   for u in cls.users:
  #     if u==name_user:
  #       for l in cls.livres:
  #         if l==name_liver:



  # def ajouter_livre(self):
  #   # Emprinter.livres.append(self.livre.titre)
  #   for livre in self.livre.

class Rendre:
  users=Emprinter.users
  def __init__(self):
    pass

  
