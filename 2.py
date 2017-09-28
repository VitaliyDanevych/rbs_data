#!/usr/bin/python2.7 
#  #!/usr/bin/env python
__AUTHOR__='Danevych V.'
__COPYRIGHT__='Danevych V. 2016 Kiev, Ukraine'
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys
import re
#import pdb


def get_array_index(cell,list_my):
    array_line_index = [(index, row.index(cell)) for index, row in enumerate(list_my) if cell in row]
    for elem in array_line_index:
        cell_pos = elem[0]
        print cell_pos
    return cell_pos
    
    
def get_cell_name(site,s_num,c_num):
    if  (s_num  == '1') and (c_num == '1'):
        cell = site + 'A'
    elif (s_num  == '1') and (c_num == '2'):
        cell = site + 'E'
    elif (s_num  == '1') and (c_num == '3'):
        cell = site + 'I'
    elif (s_num  == '2') and (c_num == '1'):
        cell = site + 'B'
    elif (s_num  == '2') and (c_num == '2'):
        cell = site + 'F'
    elif (s_num  == '2') and (c_num == '3'):
        cell = site + 'J'
    elif (s_num  == '3') and (c_num == '1'):
        cell = site + 'C'
    elif (s_num  == '3') and (c_num == '2'):
        cell = site + 'G'
    elif (s_num  == '3') and (c_num == '3'):
        cell = site + 'K'
    elif (s_num  == '4') and (c_num == '1'):
        cell = site + 'D'
    elif (s_num  == '4') and (c_num == '2'):
        cell = site + 'H'
    elif (s_num  == '4') and (c_num == '3'):
        cell = site + 'L'
    elif (s_num  == '5') and (c_num == '1'):
        cell = site + 'M'
    elif (s_num  == '5') and (c_num == '2'):
        cell = site + 'N'
    elif (s_num  == '5') and (c_num == '3'):
        cell = site + 'O'
    elif (s_num  == '6') and (c_num == '1'):
        cell = site + 'P'
    elif (s_num  == '6') and (c_num == '2'):
        cell = site + 'R'
    elif (s_num  == '6') and (c_num == '3'):
        cell = site + 'S'  
    elif (s_num  == '7') and (c_num == '1'):
        cell = site + 'T'
    elif (s_num  == '7') and (c_num == '2'):
        cell = site + 'U'
    elif (s_num  == '7') and (c_num == '3'):
        cell = site + 'V'
    elif (s_num  == '8') and (c_num == '1'):
        cell = site + 'W'
    elif (s_num  == '8') and (c_num == '2'):
        cell = site + 'X'
    elif (s_num  == '8') and (c_num == '3'):
        cell = site + 'Y'
    
    return cell    

#(site,cell,status,antenna_type,s_num,c_num,e_tilt)    
def insert_array(site,cell,status=None,antenna_type=None,s_num=None,c_num=None,e_tilt=None):
    if  cell == site + 'A':
            list_my[0][0] = site
            list_my[0][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[0][2] = antenna_type +'=' + s_num + '-' + c_num #'SectorAntenna=1-1'
            if status is not None:
                list_my[0][3] = status
            if e_tilt is not None:
                list_my[0][4] = e_tilt
    elif cell == site + 'E':
            list_my[1][0] = site
            list_my[1][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[1][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[1][3] = status
            if e_tilt is not None:    
                list_my[1][4] = e_tilt
    elif  cell == site + 'I':
            list_my[2][0] = site
            list_my[2][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[2][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[2][3] = status
            if e_tilt is not None: 
                list_my[2][4] = e_tilt
    elif  cell == site + 'B':
            list_my[3][0] = site
            list_my[3][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[3][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[3][3] = status
            if e_tilt is not None: 
                list_my[3][4] = e_tilt
    elif  cell == site + 'F':
            list_my[4][0] = site
            list_my[4][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[4][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[4][3] = status
            if e_tilt is not None: 
                list_my[4][4] = e_tilt
    elif  cell == site + 'J':
            list_my[5][0] = site
            list_my[5][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[5][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[5][3] = status
            if e_tilt is not None: 
                list_my[5][4] = e_tilt
    elif  cell == site + 'C':
            list_my[6][0] = site
            list_my[6][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[6][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[6][3] = status
            if e_tilt is not None: 
                list_my[6][4] = e_tilt            
    elif  cell == site + 'G':
            list_my[7][0] = site
            list_my[7][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[7][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[7][3] = status
            if e_tilt is not None:
                list_my[7][4] = e_tilt            
    elif  cell == site + 'K':
            list_my[8][0] = site
            list_my[8][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[8][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[8][3] = status
            if e_tilt is not None:
                list_my[8][4] = e_tilt
    elif  cell == site + 'D':
            list_my[9][0] = site
            list_my[9][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[9][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[9][3] = status
            if e_tilt is not None:
                list_my[9][4] = e_tilt
    elif  cell == site + 'H':
            list_my[10][0] = site
            list_my[10][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[10][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[10][3] = status
            if e_tilt is not None:
                list_my[10][4] = e_tilt
    elif  cell == site + 'L':
            list_my[11][0] = site
            list_my[11][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[11][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[11][3] = status
            if e_tilt is not None:
                list_my[11][4] = e_tilt
    elif  cell == site + 'M':
            list_my[12][0] = site
            list_my[12][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[12][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[12][3] = status
            if e_tilt is not None:
                list_my[12][4] = e_tilt
    elif  cell == site + 'N':
            list_my[13][0] = site
            list_my[13][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[13][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[13][3] = status
            if e_tilt is not None:
                list_my[13][4] = e_tilt
    elif  cell == site + 'O':
            list_my[14][0] = site
            list_my[14][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[14][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[14][3] = status
            if e_tilt is not None:
                list_my[14][4] = e_tilt
    elif  cell == site + 'P':
            list_my[15][0] = site
            list_my[15][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[15][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[15][3] = status
            if e_tilt is not None:
                list_my[15][4] = e_tilt
    elif  cell == site + 'R':
            list_my[16][0] = site
            list_my[16][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[16][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[16][3] = status
            if e_tilt is not None:
                list_my[16][4] = e_tilt
    elif  cell == site + 'S':
            list_my[17][0] = site
            list_my[17][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[17][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[17][3] = status
            if e_tilt is not None:
                list_my[17][4] = e_tilt
    elif  cell == site + 'T':
            list_my[18][0] = site
            list_my[18][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[18][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[18][3] = status
            if e_tilt is not None:
                list_my[18][4] = e_tilt
    elif  cell == site + 'U':
            list_my[19][0] = site
            list_my[19][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[19][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[19][3] = status
            if e_tilt is not None:
                list_my[19][4] = e_tilt
    elif  cell == site + 'V':
            list_my[20][0] = site
            list_my[20][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[20][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[20][3] = status
            if e_tilt is not None:
                list_my[20][4] = e_tilt
    elif  cell == site + 'W':
            list_my[21][0] = site
            list_my[21][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[21][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[21][3] = status
            if e_tilt is not None:
                list_my[21][4] = e_tilt
    elif  cell == site + 'X':
            list_my[22][0] = site
            list_my[22][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[22][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[22][3] = status
            if e_tilt is not None:
                list_my[22][4] = e_tilt
    elif  cell == site + 'Y':
            list_my[23][0] = site
            list_my[23][1] = cell
            if (antenna_type is not None) and (s_num is not None) and (c_num is not None):
                list_my[23][2] = antenna_type +'=' + s_num + '-' + c_num
            if status is not None:
                list_my[23][3] = status
            if e_tilt is not None:
                list_my[23][4] = e_tilt
  
    return cell 

"""
def insert_etilt_array(site,cell,e_tilt):
    if  cell == site + 'A':
            list_my[0][4] = e_tilt
            list_my[1][4] = e_tilt
            list_my[2][4] = e_tilt
    elif  cell == site + 'B':
            list_my[3][4] = e_tilt
            list_my[4][4] = e_tilt
            list_my[5][4] = e_tilt
    elif  cell == site + 'C':
            list_my[6][4] = e_tilt           
            list_my[7][4] = e_tilt     
            list_my[8][4] = e_tilt
    elif  cell == site + 'D':
            list_my[9][4] = e_tilt           
            list_my[10][4] = e_tilt     
            list_my[11][4] = e_tilt
    elif  cell == site + 'M':
            list_my[12][4] = e_tilt           
            list_my[13][4] = e_tilt     
            list_my[14][4] = e_tilt
    elif  cell == site + 'P':
            list_my[15][4] = e_tilt           
            list_my[16][4] = e_tilt     
            list_my[17][4] = e_tilt
    elif  cell == site + 'T':
            list_my[18][4] = e_tilt           
            list_my[19][4] = e_tilt     
            list_my[20][4] = e_tilt
    elif  cell == site + 'W':
            list_my[21][4] = e_tilt           
            list_my[22][4] = e_tilt     
            list_my[23][4] = e_tilt
  
    return cell        
"""    

def main():
    path = '/home/fmuser2/scripts/rbs_data/log/'
    #os.chdir('/home/fmuser2/scripts/rbs_data/response/')    
    f2 = open('/home/fmuser2/scripts/rbs_data/response/rbs_etilt_result.csv','w')
    files = os.listdir(path)
    files_log = [i for i in files if i.endswith('.log')]
    file_count = 0
    title = 'site;' + 'cell;' + 'sector_antenna;' + 'ret_status;' + 'e_tilt;'
    f2.write("%s;" % title)
    f2.write("\n")
    for file in files_log:
        global list_my
        #list_my=[[0 for j in range(5)] for i in range(9)]
        list_my=[[0 for j in range(5)] for i in range(24)]
        site = ''
        line_count = 0
        count_cells = -1
        #cell_pos = 0
        file_count += 1
        full_file = path + file
        print str(file_count) + '  ' + full_file
        f = open(full_file, 'rU')
        for line in f:
            cell = ''
            matched = ''
            line_count += 1

            # VN9154> lst cell
            matched = re.search(r'^(\w+)\>\s+lst cell.*', line)
            if matched:
                site = matched.group(1)
                #print 'HHHHH1' + ' site detected = ' + site
                #pdb.set_trace()
                
            #st ret
            #    346                1 (ENABLED)   Equipment=1,SectorAntenna=1-1,AuxPlugInUnit=2,RetuDeviceGroup=1
            matched = re.search(r'^.*\((ENABLED|DISABLED)\)\s+ Equipment=1,(ExternalAntenna|SectorAntenna)=([1-8])-(1|2|3)', line)
            # 1 - 	ENABLED  2 - SectorAntenna 3 - 1  4 - 1
            if matched:
                status = matched.group(1)                
                s_num = matched.group(3) 
                c_num = matched.group(4)
                #print 'ret status: ' + ret_status + ' s_num: ' + s_num + ' c_num: ' + c_num
                cell = get_cell_name(site,s_num,c_num)
                if cell is not None:
                    insert_array(site,cell,status)

            #lget . electricalAntennaTilt
            #    353 ExternalAntenna=1-2,AuxPlugInUnit=2,RetuDeviceGroup=1,RetDeviceSet=1,RetDevice=1 electricalAntennaTilt 50
            matched = re.search(r'^\s+\d+\s+(ExternalAntenna|SectorAntenna)=([1-8])-(1|2|3).*electricalAntennaTilt\s+(\d+)', line)
            # Match 1 = 1, 2 = 1, 3 = 50
            if matched:
                antenna_type = matched.group(1) #s_num = matched.group(1) 
                s_num = matched.group(2) #c_num = matched.group(2)
                c_num = matched.group(3) #e_tilt = matched.group(3)
                e_tilt = matched.group(4)
                if e_tilt.isdigit():
                    e_tilt_zelyi = float(e_tilt) // 10
                    e_tilt_drob = float(e_tilt) % 10
                    if e_tilt_drob == 0:
                        e_tilt = str(int(e_tilt_zelyi))
                        #print e_tilt
                    else:
                        e_tilt = str(int(e_tilt_zelyi)) + '.' + str(int(e_tilt_drob))
                        #print e_tilt
                cell = get_cell_name(site,s_num,c_num)
                #print "HHHHH3 " + cell + " e_tilt detected"
                #print 'site= ' + site + ' cell= ' + cell + 'antenna_type= ' + antenna_type + ' s_num= ' + s_num + ' c_num ' + c_num + ' status= ' + status + ' e_tilt= ' + e_tilt
                if cell is not None:
                    insert_array(site,cell,None,antenna_type,s_num,c_num,e_tilt)  #(site,cell,status=None,antenna_type=None,s_num=None,c_num=None,e_tilt=None)
                    #insert_etilt_array(site,cell,e_tilt)

        #print title
        for i,j in enumerate(list_my):
            try:
                _s = ';'.join(j)
            except TypeError:
                continue
            f2.write("%s;" % _s)
            f2.write("\n")
    f2.close()

    
if __name__ == '__main__':
  main()

