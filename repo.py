from pathlib import Path
import json, csv
from models import Lead

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

class LeadRepository:
   def __init__(self, db_path=DB_PATH):
       self.db_path = db_path

   def _load(self):
       if not self.db_path.exists():
           return []
       try:
           return json.loads(self.db_path.read_text(encoding="utf-8"))
       except json.JSONDecodeError:
           return []
       
   def _save(self, leads):
       

       self.db_path.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

   def list_leads(self):
       return [Lead(**l) for l in self._load()]
   
   def add_lead(self, lead: Lead):
       leads = self._load()
       leads.append(lead.to_dict())
       self._save(leads)
       
   def export_csv(self, path=None):
       path = Path(path) if path else (DATA_DIR / "leads.csv")
       leads = self._load()
       try:
           with path.open("w", newline="", encoding="utf-8") as f:
               w = csv.DictWriter(f, fieldnames=["name", "company", "email", "stage", "created"])
               w.writeheader()
               for row in leads:
                   w.writerow(row)
           return path
       except PermissionError:
           return None