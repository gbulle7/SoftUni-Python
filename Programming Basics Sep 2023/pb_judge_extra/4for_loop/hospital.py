period_days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_days + 1):
    currentday_patients = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if currentday_patients <= doctors:
        treated_patients += currentday_patients
    else:
        treated_patients += doctors
        untreated_patients += currentday_patients - doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
