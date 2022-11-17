# EasyEncoder
* Transforma Qualquer tipo de codificação em UTF-8 (Pode ser alterado). Para tornar mais acessível é gerado um arquivo executável com um input do diretório onde os arquivos que precisam do tratamento estão e o diretório para onde serão remanejados após o tratamento.  


* Bibliotecas utilizadas: PySimpleGUI,os,codecs,chardet (Lembre de instalar todas elas e suas depências com o pip install)


* Não é necessário identificar os arquivos de entrada (Existe uma função para isso)


* Para especificar outro encode de saída é so fazer alterações nas linhas 27,34-39,44-45 .decode('DecodeDesejado') para o tipo de codificação desejado, descomentar a linha 40 e adicionar a codificação desejada nela também.


* Para o arquivo .EXE ser gerado utilizei a biblioteca PySimpleGUI, caso você queira gerar um novo executável após modificações basta abrir o terminal e digitar pyinstaller --onefile -w NomeDoSeuArquivo.py. O .EXE será gerado na pasta dist.



![image](https://user-images.githubusercontent.com/84941525/202456763-09104504-1f89-451b-b69e-199d84b02d99.png)

