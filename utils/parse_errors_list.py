import re


def camel_case_split(input_line):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', input_line)


f = open('errors_raw.txt', 'r')
errors = {'_': {}}
errors_reverse = {}
header = '_'
f2_lines = []
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    if line[:2] == '//':
        header = line[2:].strip()
        f2_line = '# {}\n'.format(header)
        f2_lines.append(f2_line)
        errors[header] = {}
        continue
    error = line.split()[1:]
    error_description = camel_case_split(error[0].strip())
    if error_description[0] == 'Error':
        error_description = error_description[1:]
    error_description = ' '.join(error_description)
    try:
        error_num = int(error[1])
    except ValueError:
        print('SKIP: ', header, '->', error_description, error[1])
        continue
    f2_line = '{0}: {1}\n'.format(error_description, error_num)
    f2_lines.append(f2_line)
    errors[header][error_description] = error_num
    errors_reverse[error_num] = {'category': header, 'description': error_description}
f.close()
f2 = open('errors.txt', 'w')
f2.writelines(f2_lines, )
f2.close()
print(errors)
print(errors_reverse)
