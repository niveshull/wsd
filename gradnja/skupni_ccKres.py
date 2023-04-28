import glob, os
with open('../ccKres_skupni.txt', 'w', encoding='utf-8') as outfile:
    for file in glob.glob(os.path.join('../cckresV1_0-text/cckresV1_0-text', '*.txt')):
        with open(file, 'r', encoding='utf-8') as infile:
            for line in infile:
                outfile.write(line)