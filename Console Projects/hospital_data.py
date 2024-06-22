import random as rd
import datetime as datetime
doctor_pool = [
    "Dr.Stevens", 
    "Dr.Smith",
    "Dr.Von Trapp"
    ]

class Hopital:
    def __init__(self,name) -> None:
        self.name = name


    def med_doctors(self):
        self.doctors = doctor_pool
        doctors_pool = rd.randrange(0,3)
        return self.doctors[doctors_pool]
    

    def book_appointment(self):
        randdate = rd.randint(1,30)
        randhour = rd.randint(9,15)        
        appointment_ID = rd.randrange(100,999)
        appointment_date = datetime.date(2024,6,randdate)
        appointment_time = datetime.time(randhour,randdate)
        patient_record = self.get_record()
        print(f"\tAPPOINTMENT DETAILS\n Doctor: {self.med_doctors()} \n Appointment: A{appointment_ID}\n {patient_record[0]}{patient_record[1]} Date: {appointment_date}\n Time: {appointment_time}")
       

    def get_record(self):
        record_name = str(input("Please enter your full name: "))
        with open(f"Modules_work\\files\\{record_name}File.txt","r") as file:
            self.patient_details = file.readlines()
            return self.patient_details
        

    def family_card_details(self):
        patient_id = rd.randrange(1000,9999)
        patient_name = str(input("Please enter your name: "))
        patient_lastname = str(input("Please enter your last name: "))
        patient_gender = str(input("Please enter your gender: "))
        patient_contact = str(input("Please enter your contact: "))
        patient_age = int(input("Please enter your age: "))
        details = f"Patient ID: {patient_id} \n Full Name: {patient_name} {patient_lastname} \n Gender: {patient_gender} \n Age: {patient_age} \n Contact: {patient_contact} "
        with open(f"Modules_work\\files\\{patient_name}{patient_lastname}File.txt","a") as file:
            file.write(f"{details}")

    @staticmethod
    def enroll_Hospital(self):
        print(f"Welcome to {self.name} \n")
        while True:
            family_card =str(input("Is this your first  visit? Y/n:  "))
            if family_card == "n".lower() :
                self.book_appointment()
                break
            elif family_card ==  "y".lower():
                self.family_card_details()
                self.book_appointment()
                break
               
            




h1 = Hopital("City Hospital")     
# h1.get_record()         
Hopital("City Hospital").enroll_Hospital(h1)



