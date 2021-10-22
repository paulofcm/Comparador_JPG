Contexto<br>
Para realização de auditoria de imagens fornecidas como prova de execução de um serviço de reparo em equipamentos, existe a necessidade de um serviço que realize a comparação de imagens em uma base de imagens e que identifique similaridade entre elas.

Objetivo<br>
Implementar uma API que fornece operações necessárias para:

Requisitos:<br>
 - Adicionar e remover uma imagem no banco de imagens.
 - Receber duas imagens e retornar o percentual de similaridade entre elas.
 - Receber uma imagem e retornar a imagem com maior percentual de similaridade do banco.
 Pré-requisitos:
 - Somente imagens do tipo JPG serão aceitas.
 - Checar se a imagem não está corrompida.
 Possíveis melhorias:
 - Usar JPA para salvar imagens e seus hashes.


Referências
https://github.com/KilianB/JImageHash
https://github.com/krishnact/jphash
https://spring.io/guides/tutorials/rest/
https://pypi.org/project/ImageHash/
https://flask.palletsprojects.com


1 - checar o tipo do arquivo<br>
2 - checar se arquivo jpg esta corrompido<br>
3 - comparar dois jpg<br>
4 - (add/remove) arquivos para pasta propia(banco)<br>
5 - retornar imagem(banco) com maior similaridade<br>
6 - salvar hash dos arquivos<br>
7 - usar hash dos arquivos na comparação<br>
8 - migrar armazemamento dos arquivos para JPA<br>
 
