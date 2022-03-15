import random
hospitalID, DoctorID, PharmacyID, NurseID, PatientID = 0, 0, 0, 0, 0
# global BillID  # <- likely needs to exist.


def mkHospital(names):
    global hospitalID
    hospitalID += 1
    hosp = random.choice(names).rsplit('\t', 1)
    return 'Hospital', f'{hospitalID - 1}, \'{hosp[0]}\', \'{hosp[1]}\''


def mkDoctor(fname, lname, hospital):
    global DoctorID
    DoctorID += 1
    docName = f"'{random.choice(fname)} {random.choice(lname).capitalize()}'"
    return 'Doctor', f'{DoctorID-1}, {docName}, {hospital}'


def mkNurse(fname, lname, hospital):
    global NurseID
    NurseID += 1
    nurName = f"'{random.choice(fname)} {random.choice(lname).capitalize()}'"
    return 'Nurse', f'{NurseID - 1}, {nurName}, {hospital}'


def mkPatient(fname, lname, hospital, primary_doc):
    global PatientID
    PatientID += 1
    patName = f"'{random.choice(fname)} {random.choice(lname).capitalize()}'"
    return 'Patient', f'{PatientID - 1}, {patName}, {random.randrange(10)}, {mkPhone()}, {hospital}, \'{random.choice(["M", "F"])}\', {random.randrange(100)}, {random.randrange(100, 200)}, {primary_doc}'
    pass


def mkPhone():
    return f'\'(519)-{str(random.randrange(0, 1000)).ljust(3, "0")}-{str(random.randrange(0, 10000)).ljust(4, "0")}\''


def writeToFile(file, info):
    file.write(f'INSERT INTO {info[0]} Values({info[1]});\n')


def main(doctor=9, nurse=15, patient=30, hospital=3):
    fNames, lNames, hospitalNames, addressList = [line.replace('\n', '').replace('\r', '') for line in open('firstNames.txt')],  \
                                    [line.replace('\n', '').replace('\r', '') for line in open('lastNames.txt')],  \
                                    [line.replace('\n', '').replace('\r', '') for line in open('hospital_names.txt')], \
                                    [line.replace('\n', '').replace('\r', '') for line in open('street_names.txt')]
    hospitalList = {}
    sqlFile = open('output.sql', 'w')
    for _ in range(hospital):
        hos = mkHospital(hospitalNames)
        hospitalList.update({_: []})
        writeToFile(sqlFile, hos)

    sqlFile.write('\n\n')
    for _ in range(doctor):
        doc = mkDoctor(fNames, lNames, _ % hospital)
        hospitalList[_ % hospital].append(_)
        writeToFile(sqlFile, doc)

    sqlFile.write('\n\n')
    for _ in range(nurse):
        nur = mkNurse(fNames, lNames, _ % hospital)
        writeToFile(sqlFile, nur)

    sqlFile.write('\n\n')
    for _ in range(patient):
        nur = mkPatient(fNames, lNames, _ % hospital, random.choice(hospitalList[_ % hospital]))
        writeToFile(sqlFile, nur)
    pass


if __name__ == '__main__':
    main()
