Phase 1: Conceptual Design \& Applying the Principles

This is the most critical phase. Before writing any code, you must think through the design.



**Step 1: Apply Abstraction (Defining Roles)**



Abstraction means focusing on essential features while hiding unnecessary complexity. Here, we abstract the different users of the system into distinct roles.



Action: In your README.md file, create a section called "System Roles (Abstraction)" and define each role and its primary responsibilities.



Administrator: Manages user accounts (add/remove doctors, nurses) and system settings. Has the highest level of access.



Doctor: Can view and update the health records of patients assigned to them. Can prescribe medication. Can view appointment schedules.



Nurse: Can view patient records and update their daily reports (e.g., vital signs, notes). Cannot change a doctor's diagnosis or prescription.



Patient: Can only view their own medical records, prescriptions, and appointment history. Cannot see other patients' data or modify their own records.



**Step 2: Apply Decomposition and Modularity (Subsystems)**



Decomposition is breaking a large system into smaller, manageable parts. Modularity is the result, where these parts (modules) are organized logically.



Action: In your README.md, create a "System Modules (Decomposition)" section. List the subsystems and what each one does.



Patient Records Module: Manages creating, reading, updating, and deleting patient health information. This is the core module.



Appointment Scheduling Module: Handles booking, canceling, and viewing appointments for patients and doctors.



Billing Module: Manages patient invoices, payments, and insurance claims.



Pharmacy Module: Manages prescriptions, checks for drug availability, and tracks medication dispensed to patients.



**Step 3:** **Apply Cohesion and Coupling** 



High Cohesion: Each module should be highly focused on a single task. A cohesive module is like a well-organized toolbox where every tool is related to a specific job (e.g., a "plumbing" toolbox).



Low Coupling: Modules should be as independent as possible. A change in one module should not require major changes in another.



Action: Add a "Module Design (Cohesion and Coupling)" section to your README.md.



Justify Cohesion: Explain that the Billing Module only contains functions related to finance (e.g., create\_invoice(), process\_payment()). It doesn't handle appointment scheduling. This is high cohesion.



Justify Coupling: Explain how modules interact without being tightly dependent. For example, the Billing Module might need to know about a patient's appointment from the Appointment Scheduling Module. Instead of directly accessing its data, it would call a well-defined function like get\_appointment\_details(appointment\_id). This keeps them loosely coupled.



**Step 4:** **Apply Information Hiding (Security)** 



Information Hiding means concealing the internal state and implementation of an object, only exposing what is necessary. This is key for security and maintainability.



Action: Add a section on "Information Hiding and Security." Explain your strategy.



Patient data (like medical\_history) within a PatientRecord class will be a private attribute (e.g., \_medical\_history in Python).



Access to this private data will only be possible through public methods (e.g., get\_medical\_history(user)).



These methods will contain logic to check the user's role. If the user is a Doctor, return the data. If the user is a Patient, only return the data if their ID matches the record's ID. If the user is unauthorized, deny access.

