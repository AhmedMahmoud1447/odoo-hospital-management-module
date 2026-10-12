#  Hospital Management System - Custom Odoo 17 Module

A custom **Odoo 17** module designed to streamline and automate hospital operations, patient management, doctor schedules, and consultation billing workflows.

---

##  Key Features

- **Patient Management:**
  - Complete patient profile handling (Contact Info, Age, Gender, Medical Notes).
  - Integrated Chatter view (`mail.thread` & `mail.activity.mixin`) for tracking communications and log notes.

- **Doctor Directory:**
  - Specialty management and consultation fee configuration.
  - Linked directly to appointment histories (`One2many` relational mapping).

- **Appointment Workflow & Billing Integration:**
  - Unique auto-sequence generation for appointment reference numbers (e.g., `APP0001`).
  - Appointment lifecycle states (`Draft` ➔ `Confirmed` ➔ `Done` / `Cancelled`).
  - **Automated Invoicing:** One-click confirmation (`action_confirm`) that automatically generates a Customer Invoice (`account.move`) in Odoo Accounting with the doctor's consultation fee.

- **Security & Access Controls:**
  - Fine-grained Access Control Lists (`ir.model.access.csv`) defined per user group.

---

## 🛠️ Tech Stack & Architecture

- **ERP Platform:** Odoo 17 (Community / Enterprise)
- **Programming Language:** Python 3.10+
- **Backend Database:** PostgreSQL
- **Frontend / UI:** Odoo XML Architecture (Form, Tree, and Search Views)
- **Deployment:** Docker & Docker Compose

---

## 📂 Project Structure

```text
custom_addons/
└── hospital_management/
    ├── models/
    │   ├── __init__.py
    │   ├── patient.py
    │   ├── doctor.py
    │   └── appointment.py
    ├── views/
    │   ├── patient_views.xml
    │   ├── doctor_views.xml
    │   ├── appointment_views.xml
    │   └── menus.xml
    ├── security/
    │   └── ir.model.access.csv
    ├── __init__.py
    └── __manifest__.py
