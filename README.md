# Desafio NExT from Cesar School<br>

## Mentores:<br>

[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/vfponcell){:target="_blank"}](vfponcell)<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/rqgomes){:target="_blank"}](rqgomes)<br>

## Desenvolvedores:<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/Alexandre1961){:target="_blank"}](Alexandre1961)<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/benjazaicaner){:target="_blank"}](benjazaicaner)<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/filipelustosaf){:target="_blank"}](filipelustosaf)<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/ManoelPedroza){:target="_blank"}](ManoelPedroza)<br>
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/paulofcm){:target="_blank"}](paulofcm)<br>

## Contexto<br>
Para realização de auditoria de imagens fornecidas como prova de execução de um serviço de reparo em equipamentos, existe a necessidade de um serviço que realize a comparação de imagens em uma base de imagens e que identifique similaridade entre elas.

## Objetivo<br>
Implementar uma API que fornece operações necessárias para:<br>

## Requisitos:<br>
 - Adicionar e remover uma imagem no banco de imagens.<br>
 - Receber duas imagens e retornar o percentual de similaridade entre elas.<br>
 - Receber uma imagem e retornar a imagem com maior percentual de similaridade do banco.<br>

## Pré-requisitos:<br>
 - Somente imagens do tipo JPG serão aceitas.<br>
 - Checar se a imagem não está corrompida.<br>

## Possíveis melhorias:<br>
 - Usar JPA para salvar imagens e seus hashes.<br>

## Referências:<br>
[go](https://github.com/KilianB/JImageHash){:target="_blank"}<br>
https://github.com/krishnact/jphash<br>
https://spring.io/guides/tutorials/rest/<br>
https://pypi.org/project/ImageHash/<br>
https://flask.palletsprojects.com<br>

## Implementações:<br>
1 - checar o tipo do arquivo<br>
2 - checar se arquivo jpg esta corrompido<br>
3 - comparar dois jpg<br>
4 - (add/remove) arquivos para pasta propia(banco)<br>
5 - retornar imagem(banco) com maior similaridade<br>
6 - salvar hash dos arquivos<br>
7 - usar hash dos arquivos na comparação<br>
 
