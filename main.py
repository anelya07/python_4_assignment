#TASK 7

import classes

fm = classes.FileManager('students.csv')
fm.check_file()
fm.create_output_folder()
dl = classes.DataLoader('students.csv')
dl.load()
dl.preview()

analysers = [classes.GpaAnalyser(dl.students), classes.CountryAnalyser(dl.students)]
print('Running all analysers:')
print('-'*30)
for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = classes.ResultSaver(analysers[0].result, 'output/result.json')
report = classes.Report(analysers[0], saver)
report.generate()

