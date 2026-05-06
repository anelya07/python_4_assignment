import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            print("\nLoading data...")
            with open(self.filename, encoding = 'utf-8') as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
                print(f'Data loaded successfully: {len(self.students)} students')
                return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return None
        except Exception:
            print("General Error")
            return None

    def preview(self, n=5):
        print(f'\nFirst {n} rows: ')
        print('-' * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print('-' * 30)