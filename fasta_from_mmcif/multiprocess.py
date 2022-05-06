# -*- coding: utf-8 -*-

import os
import sys
from multiprocessing import Pool

# check parameters
if len(sys.argv) != 2 and len(sys.argv) != 3:
    sys.exit('Usage: %s <commands_list_file> [core_nums=30(optional)]' % sys.argv[0])

# get paramaters
commands_list_file = sys.argv[1]
if len(sys.argv) == 2:
    core_nums = 30
else:
    core_nums = int(sys.argv[2])

# get commands lists
with open(commands_list_file, 'r') as fin:
    cmd_list = [i.strip() for i in fin]
print('Commands list length is ', len(cmd_list))

# running cmds on different pools
print('Running different commands on %s subprocesses...' % core_nums)
p = Pool(core_nums)
for cmd in cmd_list:
    p.apply_async(os.system, args=(cmd, ))
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')

