# Design: tradução do Manual do GIMP para PT-BR

## Objetivo

Completar progressivamente a tradução do Manual do GIMP para português brasileiro, começando pela página inicial/índice e seguindo a ordem de leitura. Cada tópico deve ser fiel ao conteúdo atual em inglês, preservar a estrutura e os links, incluir imagens pertinentes e ser commitado e enviado após a conclusão.

## Escopo e limites

- Traduzir títulos, texto corrido, legendas e rótulos visíveis ao leitor.
- Usar os arquivos de catálogo gettext `.po` existentes em `po/pt_BR/`; não alterar o texto-fonte em XML para contornar uma tradução ausente.
- Manter IDs, URLs, destinos de links e referências cruzadas, nomes próprios, comandos, código, placeholders e marcação DocBook.
- Corrigir ou substituir traduções antigas e entradas fuzzy somente depois de compará-las com o XML atual.
- Avançar por tópico na ordem do manual. O primeiro bloco cobre a página inicial/índice e o artigo “Bem-vindo ao GIMP”; cada bloco posterior cobre um artigo delimitado.

## Imagens

- Preservar as referências de imagem existentes no XML.
- Para capturas de interface relevantes, usar a interface PT-BR do GIMP sempre que for possível produzir uma captura correta e legível. Guardar a variante em `images/pt_BR/` com a mesma estrutura relativa e o mesmo nome do recurso correspondente em `images/C/`, para que o mecanismo existente de localização por idioma a selecione.
- Não recriar ilustrações conceituais, mascotes ou exemplos independentes de idioma. Usar a imagem original como fallback quando não houver motivo para uma variante localizada.
- Conferir no HTML gerado que as imagens referenciadas carregam e que as capturas correspondem aos passos descritos.
- No primeiro bloco, a ilustração do Wilber já referenciada pelo artigo não exige uma nova captura de interface.

## Fluxo por tópico

1. Identificar os arquivos XML de origem, as entradas correspondentes no catálogo `.po` e as imagens referenciadas.
2. Comparar cada entrada do catálogo com o XML atual; traduzir ou revisar somente o tópico selecionado e preservar a estrutura da mensagem.
3. Validar acentos, terminologia PT-BR, números, comandos, tags, placeholders, links e referências.
4. Executar as verificações gettext disponíveis, `git diff --check` e o build do idioma; abrir a página resultante no navegador para conferir texto, navegação e imagens.
5. Se o tópico passar nas verificações, criar um commit com mensagem em PT-BR e enviá-lo para `origin/main`. Não incluir alterações de outros tópicos no mesmo commit.
6. Confirmar o resultado do envio e o estado do repositório antes de avançar.

Falhas de build, validação ou envio devem ser reportadas explicitamente e corrigidas antes de declarar o tópico concluído. Não se deve fazer push forçado.

## Critérios de aceitação

- Todo texto traduzível do tópico selecionado corresponde à versão atual do XML e está em PT-BR natural e fiel.
- Nenhum link, destino de referência, placeholder, comando ou marcação é perdido ou alterado acidentalmente.
- A página compilada exibe o conteúdo esperado e as imagens carregam; capturas de interface presentes são PT-BR quando isso é viável e relevante.
- As verificações aplicáveis passam, e o commit/push contém somente o tópico concluído.

## Estado inicial e primeira etapa

O repositório está na branch `main`, limpo, no commit `8ae8e58`, já enviado a `origin`. A página inicial aparece em português, mas o artigo “Bem-vindo ao GIMP” tem traduções antigas no catálogo que precisam ser confrontadas com o XML atual antes de serem consideradas completas. Há imagens localizadas existentes em `images/pt_BR`; o script de build seleciona uma imagem localizada por idioma quando o arquivo correspondente existe e usa a imagem de `images/C` como fallback.

A primeira etapa é revisar o índice e traduzir/revisar o artigo “Bem-vindo ao GIMP” com base em `src/gimp.xml`, `src/introduction.xml` e nas mensagens correspondentes em `po/pt_BR/gimp.po`. A ilustração do Wilber usa o recurso compartilhado existente. Em seguida, o trabalho continua pela ordem de leitura do manual, um artigo por commit.
