import pickle

def insertDrRec():
    ContactNo = int(input('Enter the Contact No.'))
    DrName = input('Enter the Name of the Dr.:')
    Specilization =input('Enter Specilization of that Dr.')
    address = input('Enter the Address')
    doctorID = int(input('doctor ID'))
    
    rec ={'ContactNo':ContactNo,'DrName':DrName,'Specilization':Specilization ,'address':address,'doctorID':doctorID}


    m = open('doctor.dat','ab')
    pickle.dump(rec,m)
    m.close()

def readDrRec():
    m = open('doctor.dat','rb')
    while True:
        try:
            rec = pickle.load(m)
            print('ContactNo',rec['ContactNo'])
            print('DrName:',rec['DrName'])
            print('Specilization:',rec['Specilization'])
            print('address:',rec['address'])
            print('doctorID:',rec['doctorID'])
        except EOFError:
            break
    m.close()



def searchdoctorID(r):
    m = open('doctor.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(m)
            if rec['doctorID'] == r:
                print('doctorID:',rec['doctorID'])
                print('DrName:',rec['DrName'])
                print('ContactNo:',rec['ContactNo'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No Records found')
    m.close()
    




def updateContactNo(r,n):
    m = open('doctor.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    for i in range (len(reclst)):
        if reclst[i]['doctorID']==r:
            reclst[i]['ContactNo'] = n
    m = open('doctor.dat','wb')
    for x in reclst:
        pickle.dump(x,m)
    m.close()            


def deleteDrRec(r):
    m = open('doctor.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    m = open('doctor.dat','wb')
    for x in reclst:
        if x['doctorID']==r:
            continue
        pickle.dump(x,m)
    m.close()



def insertPatRec():
    ContactNo = int(input('Enter the Contact Number the Patient.'))
    PatientName = input('Enter the Name of the Patient:')
    PatientAge =int(input('Enter patient of that Age'))
    address = input('Enter the Address')
    AcknowledgementID = int(input('Acknowledgement ID'))
    
    rec ={'ContactNo':ContactNo,'PatientName':PatientName,'PatientAge':PatientAge ,'address':address,'AcknowledgementID':AcknowledgementID}


    m = open('Patient.dat','ab')
    pickle.dump(rec,m)
    m.close()

def readPatRec():
    m = open('Patient.dat','rb')
    while True:
        try:
            rec = pickle.load(m)
            print('ContactNo',rec['ContactNo'])
            print('PatientName:',rec['PatientName'])
            print('PatientAge:',rec['PatientAge'])
            print('address:',rec['address'])
            print('AcknowledgementID:',rec['AcknowledgementID'])
        except EOFError:
            break
    m.close()



def searchAcknowledgementID1(r):
    m = open('Patient.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(m)
            if rec['AcknowledgementID'] == r:
                print('AcknowledgementID:',rec['AcknowledgementID'])
                print('PatientName:',rec['PatientName'])
                print('ContactNo:',rec['ContactNo'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No Records found')
    m.close()
    




def updateContactNo1(r,n):
    m = open('Patient.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    for i in range (len(reclst)):
        if reclst[i]['AcknowledgementID']==r:
            reclst[i]['ContactNo'] = n
    m = open('Patient.dat','wb')
    for x in reclst:
        pickle.dump(x,m)
    m.close()            


def deletePatRec(r):
    m = open('Patient.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    m = open('Patient.dat','wb')
    for x in reclst:
        if x['AcknowledgementID']==r:
            continue
        pickle.dump(x,m)
    m.close() 


def insertPatBoRec():
    ContactNo = int(input('Enter the Contact Number the Patient.'))
    PatientName = input('Enter the Name of the Patient:')
    DrName =input('Enter patient of that Age')
    DoctorFees =int(input('Enter fees of Doctor'))
    AcknowledgementID = int(input('Acknowledgement ID as per Dr. List'))
    
    rec ={'ContactNo':ContactNo,'PatientName':PatientName,'DrName':DrName ,'DoctorFees':DoctorFees,'AcknowledgementID':AcknowledgementID}


    m = open('Patientbook.dat','ab')
    pickle.dump(rec,m)
    m.close()

def readPatBoRec():
    m = open('Patientbook.dat','rb')
    while True:
        try:
            rec = pickle.load(m)
            print('ContactNo',rec['ContactNo'])
            print('PatientName:',rec['PatientName'])
            print('DrName:',rec['DrName'])
            print('DoctorFees:',rec['DoctorFees'])
            print('AcknowledgementID:',rec['AcknowledgementID'])
        except EOFError:
            break
    m.close()



def searchAcknowledgementID2(r):
    m = open('Patientbook.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(m)
            if rec['AcknowledgementID'] == r:
                print('AcknowledgementID:',rec['AcknowledgementID'])
                print('DrName:',rec['DrName'])
                print('ContactNo:',rec['ContactNo'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No Records found')
    m.close()
    




def updateContactNo2(r,n):
    m = open('Patientbook.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    for i in range (len(reclst)):
        if reclst[i]['AcknowledgementID']==r:
            reclst[i]['ContactNo'] = n
    m = open('Patientbook.dat','wb')
    for x in reclst:
        pickle.dump(x,m)
    m.close()            


def deletePatBoRec(r):
    m = open('Patientbook.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(m)
            reclst.append(rec)
        except EOFError:
            break
    m.close()
    m = open('Patientbook.dat','wb')
    for x in reclst:
        if x['AcknowledgementID']==r:
            continue
        pickle.dump(x,m)
    m.close() 








while True:
    print('Type 1 to insert Doctor rec.')
    print('Type 2 to display Doctor rec.')
    print('Type 3 to Search doctorID.')
    print('Type 4 to Update Contact Number.')
    print('Type 5 to delete a Doctor Record.')
    print('Type 6 to insert Patient rec.')
    print('Type 7 to display Patient rec.')
    print('Type 8 to Search AcknowledgementID.')
    print('Type 9 to Update Contact Number.')
    print('Type 10 to delete a Doctor Record.')
    print('Type 11 to insert Patient rec.')
    print('Type 12 to display Patient rec.')
    print('Type 13 to Search AcknowledgementID.')
    print('Type 14 to Update Contact Number.')
    print('Type 15 to delete a Patient Record.')
    print('Type 16 to exit.')
    choice = int(input('Enter you choice:'))
    if choice == 1:
        insertDrRec()
    if choice == 2:
        readDrRec()
    if choice == 3:
        r = int(input('Enter a doctorID to search:'))
        searchdoctorID(r)
    if choice == 4:
        r = int(input('Enter a doctorID:'))
        n = int(input('Enter new ContactNo:'))
        updateContactNo(r,n)
    if choice == 5:
        r = int(input('Enter a doctorID:'))
        deleteDrRec(r)
    if choice == 6:
        insertPatRec()
    if choice == 7:
        readPatRec()
    if choice == 8:
        r = int(input('Enter a AcknowledgementID to search:'))
        searchAcknowledgementID1(r)
    if choice == 9:
        r = int(input('Enter a AcknowledgementID:'))
        n = int(input('Enter new ContactNo:'))
        updateContactNo1(r,n)
    if choice == 10:
        r = int(input('Enter a AcknowledgementID:'))
        deletePatRec(r)
    if choice == 11:
        insertPatBoRec()
    if choice == 12:
        readPatBoRec()
    if choice == 13:
        r = int(input('Enter a AcknowledgementID to search:'))
        searchAcknowledgementID2(r)
    if choice == 14:
        r = int(input('Enter a AcknowledgementID:'))
        n = int(input('Enter new ContactNo:'))
        updateContactNo2(r,n)
    if choice == 15:
        r = int(input('Enter a AcknowledgementID:'))
        deletePatBoRec(r)
    if choice == 16:
        exit()
