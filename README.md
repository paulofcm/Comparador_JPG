# Desafio NExT from Cesar School<br>

https://www.cesar.school/next-nova-experiencia-de-trabalho/

## Mentores:<br>

* rqgomes [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/rqgomes)](https://github.com/rqgomes)<br>
* vfponcell [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/vfponcell)](https://github.com/vfponcell)<br>

## Desenvolvedores:<br>


<div class="Box-row clearfix d-flex flex-items-center js-repo-access-entry adminable">
            <input type="checkbox"
              class="js-bulk-actions-toggle"
              id="user-68691730"
              name="user_ids[]"
              value="68691730"
              aria-label="user Alexandre Carneiro Moreira"
              data-check-all-item >
            <div class="mx-3">
  <a href="/Alexandre1961">
    <img class="avatar avatar-user" data-hovercard-type="user" data-hovercard-url="/users/Alexandre1961/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" src="https://avatars.githubusercontent.com/u/68691730?s=64&amp;v=4" width="32" height="32" alt="@Alexandre1961" />
  </a>
</div>

<div class="d-flex flex-column flex-auto col-6">
  <a href="/Alexandre1961"><strong>Alexandre Carneiro Moreira</strong></a>
  <span class="f6 color-fg-muted">
      Alexandre1961
      &bull;
      
      Collaborator
  </span>
</div>


* Alexandre1961 [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/Alexandre1961)](https://github.com/Alexandre1961)<br>
* benjazaicaner [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/benjazaicaner)](https://github.com/benjazaicaner)<br>
* filipelustosaf [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/filipelustosaf)](https://github.com/filipelustosaf)<br>
* ManoelPedroza [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/ManoelPedroza)](https://github.com/ManoelPedroza)<br>
* paulofcm [![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/paulofcm)](https://github.com/paulofcm)<br>

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
https://github.com/KilianB/JImageHash)<br>
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
 
