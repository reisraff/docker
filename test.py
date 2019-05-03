import re

file = open('docker-compose.yml', 'r')

container = 'php'
spaces = 0
from_line = 0

iterator = list(file.readlines())

for _, line in enumerate(iterator):
    if ' {}:'.format(container) in line:
        spaces = line.count(' ')
        from_line = _
        break

ports = []
p = False

for _, line in enumerate(iterator):
    if _ < from_line:
        continue

    if _ > from_line and line.count(' ') < spaces + 1:
        break

    if 'ports:' in line:
        spaces = line.count(' ')
        p = True
        continue

    if p:
        ports.append(line)


real_ports = []


for port in ports:
    result = re.findall('[0-9.:]+', port)
    real_ports.append(result[0])

print(real_ports)
