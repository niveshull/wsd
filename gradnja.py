import glob, os
for text_file in glob.glob(os.path.join('..', 'delo', 'cckresV1_0-text', '*.txt')):
    print(text_file)