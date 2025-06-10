from django.core.management.base import BaseCommand
from pams.models import Patient

class Command(BaseCommand):
    help = 'Add dummy patients to the database'

    def handle(self, *args, **kwargs):
        dummy_patients = [
            {
                'full_name': 'Aarav Sharma',
                'age': 28,
                'gender': 'M',
                'insurance_provider': 'Star Health',
                'policy_number': 'SH987654'
            },
            {
                'full_name': 'Priya Patel',
                'age': 34,
                'gender': 'F',
                'insurance_provider': 'ICICI Lombard',
                'policy_number': 'IL123987'
            },
            {
                'full_name': 'Vikram Singh',
                'age': 40,
                'gender': 'M',
                'insurance_provider': 'HDFC Ergo',
                'policy_number': 'HE456321'
            },
            {
                'full_name': 'Ananya Gupta',
                'age': 19,
                'gender': 'F',
                'insurance_provider': 'Bajaj Allianz',
                'policy_number': 'BA654789'
            },
            {
                'full_name': 'Rohan Malhotra',
                'age': 52,
                'gender': 'O',
                'insurance_provider': 'Tata AIG',
                'policy_number': 'TA321654'
            },
        ]

        for patient_data in dummy_patients:
            if not Patient.objects.filter(
                full_name=patient_data['full_name'],
                policy_number=patient_data['policy_number']
            ).exists():
                Patient.objects.create(**patient_data)
                self.stdout.write(self.style.SUCCESS(f"Added patient: {patient_data['full_name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Patient already exists: {patient_data['full_name']}"))