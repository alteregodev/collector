import argparse

from collector.modules.find_inn import find

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('FIO', type=str, help='ФИО цели')
    parser.add_argument('--save-txt', dest='FILENAME', type=str, help='сохранить результаты в формате .txt в определенной директории под определенным названием')

    args = parser.parse_args()

    fio = args.FIO
    filename = args.FILENAME

    banner = '''
                 888 888                   888                    
                 888 888                   888                    
                 888 888                   888                    
 .d8888b .d88b.  888 888  .d88b.   .d8888b 888888 .d88b.  888d888 
d88P"   d88""88b 888 888 d8P  Y8b d88P"    888   d88""88b 888P"   
888     888  888 888 888 88888888 888      888   888  888 888     
Y88b.   Y88..88P 888 888 Y8b.     Y88b.    Y88b. Y88..88P 888     
 "Y8888P "Y88P"  888 888  "Y8888   "Y8888P  "Y888 "Y88P"  888     
 
 *****************************************************************************'''
    
    print(banner)

    find(fio)
