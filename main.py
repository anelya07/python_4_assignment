#TASK 7

import classes

dl = classes.DataLoader('students.csv')
dl.load()

analyser = classes.GpaAnalyser(dl.students)   # ← вот здесь замена
print(analyser)
analyser.analyse()
analyser.print_results()

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

