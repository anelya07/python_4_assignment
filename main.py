#TASK 7

import classes
from classes import ResultSaver

dl = classes.DataLoader('students.csv')
dl.load()

analyser = classes.GpaAnalyser(dl.students)
saver = ResultSaver(analyser.result, 'output/result.json')
report = classes.Report(analyser, saver)
report.generate()

# fm = classes.FileManager('students.csv')
# if not fm.check_file():
#     print('Stopping program.')
#     exit()
# fm.create_output_folder()
# saver = classes.ResultSaver(analyser.result, 'output/result.json')
# saver.save_json()
#
# print('-'*30)
# wr = classes.DataLoader('wrong.csv')
# wr.load()

