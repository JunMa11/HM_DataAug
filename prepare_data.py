# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:55:31 2020

@author: MA
"""

import pandas as pd
import os
join = os.path.join
import shutil

path = './mnms'
info_csv = pd.read_csv(join(path, 'info.csv'))

test_path = join(path, 'test_data')
if os.path.isdir(test_path) is not True:
    os.mkdir(test_path)

for i, name in enumerate(info_csv['External code']):
    case_path = join(path, name)
    shutil.copy(join(case_path, name+'_sa_ED.nii.gz'), join(test_path, name+'_sa_ED_0000.nii.gz'))
    shutil.copy(join(case_path, name+'_sa_ES.nii.gz'), join(test_path, name+'_sa_ES_0000.nii.gz'))
    print(i, name)