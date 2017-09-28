#!/usr/bin/python2.7 
#  #!/usr/bin/env python
__AUTHOR__='Danevych V.'
__COPYRIGHT__='Danevych V. 2016 Kiev, Ukraine'
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys
import re


def main():
    path = '/home/fmuser2/scripts/rbs_data/log/'
    #os.chdir('/home/fmuser2/scripts/rbs_data/response/')    
    f2 = open('/home/fmuser2/scripts/rbs_data/response/rbs_license_result.csv','w')
    f3 = open('/home/fmuser2/scripts/rbs_data/response/good_sites.txt','w')
    f4 = open('/home/fmuser2/scripts/rbs_data/response/bad_sites.txt','w')
    files = os.listdir(path)
    files_log = [i for i in files if i.endswith('.log')]
    file_count = 0
    for file in files_log:
        list_my = []
        line_count = 0
        file_count += 1
        full_file = path + file
        license_iu = False
        print str(file_count) + '  ' + full_file
        f = open(full_file, 'rU')
        for line in f:
            line_count += 1
            #print str(line_count) + ' ' + line
            matched = re.search(r'^(\w+)\>\s+license server', line)
            if matched:
                #print 'HHHHH1'
                matched = matched.group(1)
                list_my.append(matched)
            matched = re.search(r'^(License\s+Server)\s+\:\s+(\d+[\w+]?)', line)
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Latest\s+PV)\s+\:\s+(\d+[\w+]?)', line)
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(License\s+Key\s+File)\s+\:\s+(.*$)', line)
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Sequence\s+Number)\s+\:\s+(\d+)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Node\s+Identity\s+State)\s+\:\s+(\d+)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)  
            matched = re.search(r'^(Backplane\s+Node\s+Id)\s+\:\s+(.*$)', line)
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Generated\s+Node\s+Id)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched) 
            matched = re.search(r'^(Validation\s+Start)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Validation\s+Interval)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Emergency\s+Status)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Emergency\s+State)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Emergency\s+State\s+Time)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)
            matched = re.search(r'^(Emergency\s+Time\s+Limit)\s+\:\s+(.*$)', line)    
            if matched:
                matched = matched.group(1) + '=' + matched.group(2)
                list_my.append(matched)   
            matched = re.search(r'^\$\s+license\s+iu\s+status', line) #$ license iu status
            if matched:
                license_iu = True
            matched = re.search(r'^State\s+\:\s+(\w+)', line)
            if matched and license_iu:
                matched = 'State=' + matched.group(1)
                list_my.append(matched)  
            matched = re.search(r'^Integration\s+Unlock\s+available\s+\:\s+(\w+)', line)      
            if matched:
                matched = 'Integration_Unlock_available=' + matched.group(1)
                list_my.append(matched) 
        if len(list_my) > 10:
            f3.write("%s" % file)
            f3.write("\n")
        elif len(list_my) <= 10:
            f4.write("%s" % file)
            f4.write("\n")
            print list_my
        for each in list_my:
            #print each
            f2.write("%s;" % each)
        f2.write("\n")
        f.close()
    f2.close()
    f3.close() 
    f4.close() 

    
if __name__ == '__main__':
  main()

