# Tradução integral do Manual do GIMP 3.2 para PT-BR

## Objetivo

Concluir a tradução para português brasileiro de todo o conteúdo alcançável pelo
índice principal do Manual do GIMP 3.2, preservando a estrutura DocBook, os
links internos, a terminologia da interface e a apresentação visual. A cobertura
deve incluir o prefácio, todas as partes e capítulos, as referências, o
glossário e os apêndices incluídos pelo livro.

## Estado inicial

Na auditoria de 3 de novembro de 2026:

- `src/gimp.xml` contém 3 partes e 17 capítulos.
- A árvore de inclusões do livro alcança 762 arquivos XML.
- Os 12 catálogos em `po/pt_BR` têm 6.536 mensagens ativas: 4.745 sem marca
  fuzzy e com tradução preenchida (72,6%), 1.119 fuzzy e 672 sem tradução.
- `images/C` contém 1.951 arquivos de imagem; `images/pt_BR` contém 98.
- A árvore de trabalho está limpa, na branch `main`, sincronizada com
  `origin/main`.

Esses números são uma linha de base; a cobertura final será calculada a partir
das mensagens atuais extraídas das fontes, não apenas dos catálogos históricos.

## Escopo

1. Percorrer o conteúdo na ordem do índice principal e comparar cada catálogo
   com as fontes XML atuais.
2. Traduzir mensagens vazias e revisar traduções fuzzy, obsoletas ou
   incompatíveis com o texto atual. Revisar também mensagens já marcadas como
   traduzidas quando a leitura do contexto revelar erro ou inconsistência.
3. Preservar tags DocBook, atributos, identificadores, links, placeholders,
   teclas de atalho, comandos, código, nomes próprios e termos de produto
   conforme o contexto. Corrigir referências de interface somente quando a
   localização adotada pelo projeto for inequívoca.
4. Auditar todas as referências a imagens. Usar variantes PT-BR com caminho,
   nome e hash corretos quando forem capturas que contenham texto de interface;
   criar ou atualizar capturas localizadas apenas quando houver uma fonte
   correspondente verificável. Manter imagens ilustrativas e conteúdo visual
   sem texto quando não houver motivo de localização.
5. Não alterar o texto-fonte em inglês nem outros idiomas como parte da tradução.

## Abordagem

O trabalho será executado em lotes pequenos na ordem do índice, agrupados por
parte ou capítulo e respeitando os catálogos gettext existentes. Cada lote
deverá atualizar as mensagens para os identificadores atuais da fonte,
preservar traduções compartilhadas entre páginas e descartar entradas
obsoletas sem modificar conteúdo fora do escopo.

As capturas de tela devem manter os caminhos e nomes esperados pelo manual e o
tema visual da versão em inglês. O README do projeto determina revisão pela
equipe de idioma antes de uma submissão de capturas ao projeto upstream; essa
aprovação externa não será presumida por este trabalho.

## Validação e conclusão

Cada lote deverá passar por:

- verificação gettext dos catálogos (`msgfmt --check`) e de ausência de
  mensagens atuais vazias ou fuzzy no escopo concluído;
- verificação de tags, placeholders, links e referências de imagem;
- compilação do manual para PT-BR e inspeção das páginas no preview
  `http://127.0.0.1:8765`;
- conferência de que links internos do índice e do conteúdo resolvem no HTML
  gerado e de que capturas localizadas renderizam corretamente.

O trabalho estará completo quando todas as mensagens atuais alcançáveis pelo
índice principal estiverem traduzidas e revisadas, os problemas de build e
links introduzidos pela tradução forem resolvidos, e as imagens com conteúdo
textual localizado tiverem variantes corretas ou uma limitação explicitamente
registrada. Os lotes validados serão commitados e enviados a `origin/main`,
mantendo as alterações restritas à tradução PT-BR.

## Fora de escopo

- Reescrever ou atualizar o conteúdo técnico original em inglês.
- Alterar funcionalidades do GIMP ou a estrutura do sistema de build.
- Traduzir imagens puramente ilustrativas ou recriar imagens sem texto de
  interface.
- Declarar que capturas foram aprovadas pela equipe upstream sem a revisão
  correspondente.
