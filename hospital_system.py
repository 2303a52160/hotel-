# hospital_system.py

# ==============================================================================
# ABSTRACTION: Base class for all user roles
# ==============================================================================
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Doctor(User):
    def __init__(self, user_id, name, specialization):
        super().__init__(user_id, name)
        self.specialization = specialization

class Patient(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.record = PatientRecord(user_id)

# ==============================================================================
# INFORMATION HIDING & COHESION: A focused, secure module for patient records
# ==============================================================================
class PatientRecord:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        # Information Hiding: This attribute is "private" and should not be accessed directly
        self._medical_history = []

    def add_entry(self, user, entry_text):
        """Only Doctors can add entries to the medical history."""
        if isinstance(user, Doctor):
            self._medical_history.append(f"Entry by Dr. {user.name}: {entry_text}")
            print("Medical entry added successfully.")
            return True
        else:
            print(f"ACCESS DENIED: {user.name} is not authorized to add medical entries.")
            return False

    def get_history(self, user):
        """Doctors can view any history. Patients can only view their own."""
        if isinstance(user, Doctor):
            return self._medical_history
        elif isinstance(user, Patient) and user.user_id == self.patient_id:
            return self._medical_history
        else:
            print(f"ACCESS DENIED: {user.name} is not authorized to view this record.")
            return None

# ==============================================================================
# MODULARITY: A high-level system class to manage different parts
# In a real app, these would be separate, loosely coupled modules.
# ==============================================================================
class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    def register_patient(self, patient_id, name):
        if patient_id not in self.patients:
            new_patient = Patient(patient_id, name)
            self.patients[patient_id] = new_patient
            return new_patient
        return None

    def register_doctor(self, doctor_id, name, specialization):
        if doctor_id not in self.doctors:
            new_doctor = Doctor(doctor_id, name, specialization)
            self.doctors[doctor_id] = new_doctor
            return new_doctor
        return None

# ==============================================================================
# DEMONSTRATION
# ==============================================================================
if __name__ == "__main__":
    system = HospitalSystem()

    # Create users with different roles
    dr_smith = system.register_doctor("doc001", "Smith", "Cardiology")
    patient_john = system.register_patient("pat123", "John Doe")

    print("--- Doctor updating patient record ---")
    patient_john.record.add_entry(dr_smith, "Patient shows signs of stable heart rhythm.")

    print("\n--- Patient trying to update their own record (should fail) ---")
    patient_john.record.add_entry(patient_john, "I feel great today!")

    print("\n--- Doctor viewing patient history (should succeed) ---")
    history_for_doc = patient_john.record.get_history(dr_smith)
    if history_for_doc:
        print(f"Dr. Smith viewing John's record: {history_for_doc}")

    print("\n--- Patient viewing their own history (should succeed) ---")
    history_for_patient = patient_john.record.get_history(patient_john)
    if history_for_patient:
        print(f"John Doe viewing his own record: {history_for_patient}")