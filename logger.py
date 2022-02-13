from datetime import datetime as dt

def logger_a(value):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; value_a = {};'
                    .format(time, value))

def logger_b(value):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(' value_b = {};'
                    .format(value))

def logger_math_action(value):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('  math_action "{}";'
                    .format(value))

def logger_result(value):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(' result = {};\n'
                    .format(value))