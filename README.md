<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-FFC0CB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/POO-Conceitos_Sólidos-F48FB1?style=for-the-badge&logo=appveyor&logoColor=white" alt="POO Conceitos">
  <img src="https://img.shields.io/badge/JSON_e_CSV-Persistência-E91E63?style=for-the-badge&logo=json&logoColor=white" alt="JSON e CSV">
</div>

# Mini CRM de Leads — Versão POO 🐍

<div style="background-color:#fff3e0; padding:15px; border-left:5px solid #ff9800; border-radius:5px; margin-bottom: 20px;">
💡 <strong>Mini CRM com POO:</strong> Uma aplicação em Python para cadastrar, listar, buscar e exportar leads com foco em boas práticas de Programação Orientada a Objetos!
</div>

## Funcionalidades Principais

<div style="background-color:#f3e5f5; padding:15px; border-left:5px solid #9c27b0; border-radius:5px; margin-bottom: 20px;">
• Cadastro e Gestão de Leads: Adiciona leads comuns e Leads VIP.<br>
• Exportação para CSV: Saída organizada e compatível com Excel.<br>
• Busca Eficiente: Permite buscar leads por nome, empresa ou e-mail.<br>
• Leads VIP (Polimorfismo): Utilização de Herança e Polimorfismo para diferenciar leads de alto valor.
</div>

### Status das Funcionalidades

| Funcionalidade | Status | Observação |
| :--- | :---: | :--- |
| Adicionar novo lead | ✅ | Normal ou VIP (Herança) |
| Listar leads cadastrados | ✅ | Ordenado por data de criação |
| Buscar lead | ✅ | Por nome, empresa ou e-mail |
| Exportar CSV | ✅ | Saída compatível com Excel |
| Leads VIP (POO) | ✅ | Polimorfismo aplicado no método `__str__` (exemplo) |

## Estrutura do Projeto

A aplicação segue uma estrutura modular para separar responsabilidades (Princípio da Responsabilidade Única - SRP).

<div style="background-color:#e1f5fe; padding:10px; border-left:5px solid #03a9f4; border-radius:5px; margin-bottom: 20px;">
<pre>
aula10-mini-crm-leads/
│
├── app.py          # Interface principal (CLI) e lógica de fluxo
├── repo.py         # Repositório de dados (Camada de Persistência JSON/CSV)
├── stages.py       # Controle de estágios dos leads (Enum ou constantes)
├── models.py       # Classes Lead e VIPLead (Modelagem de Dados)
└── data/
    └── leads.json  # Base de dados local (JSON)
</pre>
</div>

## Conceitos de POO Aplicados

O projeto é um excelente exemplo prático dos pilares da Programação Orientada a Objetos em Python, utilizando classes com responsabilidades bem definidas.

<div style="background-color:#e8f5e9; padding:10px; border-left:5px solid #4caf50; border-radius:5px; margin-bottom: 20px;">
Princípios e Classes
</div>

| Conceito / Classe | Princípio POO | Detalhe da Implementação |
| :--- | :--- | :--- |
| **`Lead`** | Encapsulamento | Classe base para leads, protege dados internos. |
| **`VIPLead`** | Herança & Polimorfismo | Herda de `Lead` e redefine o método `__str__` para um formato VIP. |
| **`LeadRepository`** | Encapsulamento | Isolamento da lógica de persistência (JSON/CSV). |
| **`MiniCRMApp`** | Encapsulamento | Gerencia o fluxo do programa e esconde a complexidade de UI/Regras. |

## Exemplo de Uso (CLI)

Veja como é simples adicionar um novo lead, aplicando a lógica de Herança para o `VIPLead`.

<div style="background-color:#e0f7fa; padding:10px; border-left:5px solid #03a9f4; border-radius:5px; margin-bottom: 20px;">
<pre>
Mini CRM — Versão POO
[1] Adicionar lead
[2] Listar leads
[3] Buscar lead
[4] Exportar CSV
[0] Sair
Escolha: 1
Nome: Giovana
Empresa: FIAP
E-mail: gi@exemplo.com
Lead VIP? (s/n): s
✔ Lead adicionado com sucesso!
</pre>
</div>

## Saída de Exportação CSV

O arquivo `leads.csv` é gerado com os dados formatados, pronto para importação em outras ferramentas.

<div style="background-color:#fbe9e7; padding:10px; border-left:5px solid #ff5722; border-radius:5px; margin-bottom: 20px;">
<pre>
name,company,email,stage,created
Giovana,FIAP,gi@exemplo.com,vip,2025-10-23
Alexandre,FIAP,a@b.com,novo,2025-09-28
</pre>
</div>

---

## Tecnologias e Ferramentas

| Tecnologia | Observação |
| :--- | :--- |
| **Python** | Versão 3.10+ para execução da aplicação. |
| **JSON** | Utilizado para armazenamento local e persistência de dados. |
| **CSV** | Formato de exportação para interoperabilidade. |
| **POO** | Foco principal do projeto: Encapsulamento, Herança e Polimorfismo. |

---

## 🧑‍💻 Autora & Contexto

| Detalhe | Informação |
| :--- | :--- |
| **Autora** | Giovanna F. |
| **Disciplina** | PCP – FIAP |
| **Data** | Outubro de 2025 |
