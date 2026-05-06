#TASK 7

from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.analyser import GpaAnalyser,CountryAnalyser
from analytics.result_saver import ResultSaver
from analytics.report import Report

fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()
dl = DataLoader('students.csv')
dl.load()
dl.preview()

analysers = [GpaAnalyser(dl.students), CountryAnalyser(dl.students)]
print('Running all analysers:')
print('-'*30)
for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()

