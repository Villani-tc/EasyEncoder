
from PySimpleGUI import PySimpleGUI as sg
import os
import codecs, chardet

def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
        type_data = chardet.detect(rawdata)['encoding']
    return type_data


def encoder(path_source, path_target):
    files = os.listdir(path_source)

    for f in files:
        if os.path.isdir(f'{path_source}/{f}'):
            print("pasta")
            if not os.path.exists(f'{path_target}/{f}'):
                os.mkdir(f'{path_target}/{f}')
            encoder(f'{path_source}/{f}', f'{path_target}/{f}')
        else:

            encode = get_encoding_type(f'{path_source}/{f}')
            print(f)
            with codecs.open(path_source + '/' + f, "r+b", encoding=encode, errors='ignore') as sourceFile:
                with codecs.open(path_target + '/' + f, "w+b", "utf-8", errors='ignore') as targetFile:
                    for line in sourceFile:
                        try:
                            # remove caracteres unicode

                            line = line.encode('unicode', 'ignore').decode('ascii')
                            # converte de iso-8859-1 para utf-8
                            line = line.encode('utf-16').decode('utf-8-sig')

                            print(line.encode('iso-8859-1').decode('utf-8-sig'))
                            line = line.encode('iso-8859-1').decode('utf-8-sig')
                            line = line.encode('windows-1252').decode('utf-8-sig')
                            line = line.encode('utf-8').decode('utf-8-sig')
                            targetFile.write(line)
                        except Exception as e:
                            # falhou então converte de windows-1252 para utf-8-sig
                            try:
                                print(line.encode('windows-1252').decode('utf-8-sig'))
                                targetFile.write(line.encode('windows-1252').decode('utf-8-sig'))
                            except:
                                targetFile.write(line)

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Path Source'), sg.Input(key='path_source')],
    [sg.Text('Path Target'), sg.Input(key='path_target')],
    [sg.Button('Executar')]

]
# Janela
janela = sg.Window('Encoder', layout)
# Leitura do EXE
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Executar':
        path_source = valores['path_source']
        path_target = valores['path_target']
        print(path_source)
        print(path_target)
        break

if __name__ == '__main__':
    encoder(path_source, path_target)
