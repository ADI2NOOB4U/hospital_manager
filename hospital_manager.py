import json
import os

data_file = "patients.json"

def load_patients():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    else:
        return []

def save_patients(patients):
    with open(data_file, "w") as f:
        json.dump(patients, f, indent=4)

def add_patient():
    patients = load_patients()
    print("\n--- Add Patient ---")
    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    illness = input("Enter Disease/Problem: ")
    doctor = input("Assigned Doctor: ")
    admit = input("Admit Date: ")
    phone = input("Phone Number: ")

    new_patient = {
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "illness": illness,
        "doctor": doctor,
        "admit_date": admit,
        "phone": phone
    }

    patients.append(new_patient)
    save_patients(patients)
    print("Patient Added.\n")

def view_all():
    patients = load_patients()
    print("\n--- All Patients ---")
    if len(patients) == 0:
        print("No records found.\n")
        return

    for p in patients:
        print("--------------------------")
        print("ID:", p["id"])
        print("Name:", p["name"])
        print("Age:", p["age"])
        print("Gender:", p["gender"])
        print("Disease:", p["illness"])
        print("Doctor:", p["doctor"])
        print("Admit Date:", p["admit_date"])
        print("Phone:", p["phone"])
    print("--------------------------\n")

def search_patient():
    patients = load_patients()
    pid = input("Enter Patient ID to search: ")
    found = False

    for p in patients:
        if p["id"] == pid:
            print("\n--- Patient Found ---")
            print("ID:", p["id"])
            print("Name:", p["name"])
            print("Age:", p["age"])
            print("Gender:", p["gender"])
            print("Disease:", p["illness"])
            print("Doctor:", p["doctor"])
            print("Admit Date:", p["admit_date"])
            print("Phone:", p["phone"], "\n")
            found = True
            break

    if not found:
        print("Patient not found.\n")

def update_patient():
    patients = load_patients()
    pid = input("Enter Patient ID to update: ")

    for p in patients:
        if p["id"] == pid:
            print("\n--- Update Details (press enter to skip) ---")
            new_name = input(f"Name ({p['name']}): ")
            new_age = input(f"Age ({p['age']}): ")
            new_gender = input(f"Gender ({p['gender']}): ")
            new_ill = input(f"Disease ({p['illness']}): ")
            new_doc = input(f"Doctor ({p['doctor']}): ")
            new_date = input(f"Admit Date ({p['admit_date']}): ")
            new_phone = input(f"Phone ({p['phone']}): ")

            if new_name: p["name"] = new_name
            if new_age: p["age"] = new_age
            if new_gender: p["gender"] = new_gender
            if new_ill: p["illness"] = new_ill
            if new_doc: p["doctor"] = new_doc
            if new_date: p["admit_date"] = new_date
            if new_phone: p["phone"] = new_phone

            save_patients(patients)
            print("Patient Updated.\n")
            return

    print("Patient not found.\n")

def delete_patient():
    patients = load_patients()
    pid = input("Enter Patient ID to delete: ")

    new_list = []
    deleted = False

    for p in patients:
        if p["id"] == pid:
            deleted = True
        else:
            new_list.append(p)

    if deleted:
        save_patients(new_list)
        print("Patient deleted.\n")
    else:
        print("No record found.\n")

def main_menu():
    while True:
        print("""
=============================
   Hospital Patient System
=============================
1. Add Patient
2. View All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            print("Closing Program...")
            break
        else:
            print("Invalid choice, try again.\n")

main_menu()
