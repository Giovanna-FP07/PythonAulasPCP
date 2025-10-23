from datetime import date

class Lead:
   def __init__(self, name, company, email, stage="novo", created=None):
       self.name = name
       self.company = company
       self.email = email
       self.stage = stage
       self.created = created or date.today().isoformat()

   def to_dict(self):
       return {
           "name": self.name,
           "company": self.company,
           "email": self.email,
           "stage": self.stage,
           "created": self.created,
       }
   
   def __str__(self):
       return f"{self.name} ({self.company}) — {self.email}"

# Exemplo de herança e polimorfismo
class VIPLead(Lead):
   def __init__(self, name, company, email):
       super().__init__(name, company, email, stage="vip")
       
   # Polimorfismo: comportamento diferente para VIP
   def __str__(self):
       return f"[VIP] {self.name} — {self.company} ({self.email})"