from models import Lead, VIPLead

class StageManager:
   def new_lead(self, name, company, email):
       return Lead(name, company, email)
   
   def new_vip_lead(self, name, company, email):
       return VIPLead(name, company, email)