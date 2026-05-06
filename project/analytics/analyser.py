class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key,value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"\nDataAnalyser: base class, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []
        counter = 0
        for row in self.students:
            try:
                value = float(row['GPA'])
                gpas.append(value)
                if value > 3.5:
                    counter+=1
            except ValueError:
                print(f"Warning: could not convert value for student {row['student_id']} — skipping row.")
                continue

        avg_gpa = sum(gpas) / len(gpas)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, self.students))
        gpa_values = list(map(lambda s: float(s['GPA']), self.students))
        hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, self.students))

        self.result = {"total_students": len(self.students), "average_gpa": round(avg_gpa, 2), "max_gpa": max_gpa, "min_gpa": min_gpa, "high_performers": counter, "high_gpa": len(high_gpa), "gpa_values": gpa_values[:5], "hard_workers": len(hard_workers)}
        return self.result

    def print_results(self):
        print('=' * 30)
        print('GPA ANALYSIS REPORT')
        print('=' * 30)
        super().print_results()
        print('=' * 30)

    def __str__(self):
        return f"\nGpaAnalyser: GPA Statistics, {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_counts = {}
        for row in self.students:
            country = row["country"]
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
        top_3 = sorted_countries[:3]

        self.result = {"total_students": len(self.students), "total_countries": len(country_counts), "top_3": top_3}
        return self.result

    def print_results(self):
        print('=' * 30)
        print('COUNTRY ANALYSIS REPORT')
        print('=' * 30)
        super().print_results()
        print('=' * 30)

    def __str__(self):
        return f"\nCountryAnalyser: Country Analysis, {len(self.students)} students"
