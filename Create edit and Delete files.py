# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:48:35 2019

@author: dvbckle
"""
# code snips to create, edit and delete files

def main():
    _file = 'my_create_and_delete_file.txt'
    _CreateFile(_file)
    _WriteToFile(_file)
    _ReadandPrintFromFile(_file)
    _AppendToFile(_file)
    _ReadandPrintFromFile(_file)
    _DeleteFile(_file)
    
    print('\nEnd of Main')
    

    # Create a file
def _CreateFile(_file):
    print('\nCreating file: ',_file)
    f = open(_file, 'w')
        
    # Write to a file  
def _WriteToFile(_file):
    print('\nWriting to file: ',_file)
    l = ['hi', 'there', 'I', 'am', 'writing', 'in', 'a', 'file']
    with open(_file, 'w') as f:
        for s in l:
            f.write(s + '\n')
            
     #Read from a file
def _ReadandPrintFromFile(_file):
    print('\nReading and Printing from file: ',_file)
    with open(_file, 'r') as f:
        for line in f:
            print(line, end='')
       
    #Append to a file
def _AppendToFile(_file):
    print('\nAppending to file: ',_file)
    with open(_file, 'a') as f:
        f.write('Bye\n')
        
    #Delete a file
def _DeleteFile(_file):
    print('\nDeleting file: ',_file)
    permission = input('\nAre you sure you want to delete '+_file + ' ,To Proceed, enter Yes')
    if permission == 'Yes':
        import os
        os.remove(_file) 
        print('\nFile: ' + _file + ' has been deleted')
    else:
        print ('\nOK, ' +_file + 'will not be deleted')
        return
    
   
main()
  
