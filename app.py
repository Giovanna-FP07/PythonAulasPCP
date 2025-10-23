from repo import LeadRepository
from stages import StageManager

class MiniCRMApp:
   def __init__(self):
       self.repo = LeadRepository()
       self.stages = StageManager()

   def add_flow(self):
       name = input("Nome: ").strip()
       company = input("Empresa: ").strip()
       email = input("E-mail: ").strip()

       if not name or not email or "@" not in email:
           print("❌ Nome e e-mail válidos são obrigatórios.")
           return
       
       tipo = input("Lead VIP? (s/n): ").strip().lower()
       lead = self.stages.new_vip_lead(name, company, email) if tipo == "s" else self.stages.new_lead(name, company, email)
       
       self.repo.add_lead(lead)
       print("✔ Lead adicionado com sucesso!")
   
   def list_flow(self):
       leads = self.repo.list_leads()
       if not leads:
           print("Nenhum lead ainda.")
           return
       
       print("\n# | Nome                 | Empresa            | E-mail")
       print("--+----------------------+-------------------+-----------------------")
       for i, l in enumerate(leads):
           print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

   def search_flow(self):
       q = input("Buscar por: ").strip().lower()
       if not q:
           print("Consulta vazia.")
           return
       
       results = [l for l in self.repo.list_leads() if q in f"{l.name} {l.company} {l.email}".lower()]

       if not results:
           print("Nada encontrado.")
           return
       
       print("\n# | Nome                 | Empresa            | E-mail")
       print("--+----------------------+-------------------+-----------------------")
       for i, l in enumerate(results):
           print(f"{i:02d}| {l.name:<20} | {l.company:<17} | {l.email:<21}")

   def export_flow(self):
       path = self.repo.export_csv()
       if path:
           print(f"✔ Exportado para: {path}")
       else:
           print("Não consegui exportar. Feche o CSV e tente novamente.")

   def print_menu(self):
       print("\nMini CRM — Versão POO")
       print("[1] Adicionar lead")
       print("[2] Listar leads")
       print("[3] Buscar lead")
       print("[4] Exportar CSV")
       print("[0] Sair")

   def main(self):
       while True:
           self.print_menu()
           op = input("Escolha: ").strip()
           if op == "1":
               self.add_flow()
           elif op == "2":
               self.list_flow()
           elif op == "3":
               self.search_flow()
           elif op == "4":
               self.export_flow()
           elif op == "0":
               print("Até mais!")
               break
           else:
               print("Opção inválida.")
               
if __name__ == "__main__":
   app = MiniCRMApp()
   app.main()