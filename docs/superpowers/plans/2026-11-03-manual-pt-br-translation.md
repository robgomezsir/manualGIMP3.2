# Tradução inicial do Manual do GIMP — Plano de execução

> **Para agentes executores:** SUB-SKILL OBRIGATÓRIA: use `superpowers:subagent-driven-development` (recomendado) ou `superpowers:executing-plans` para executar o plano tarefa por tarefa. As etapas usam caixas de seleção (`- [ ]`) para acompanhamento.

**Objetivo:** Revisar a página inicial/índice e concluir a tradução atualizada do artigo “Bem-vindo ao GIMP” em PT-BR, validando a navegação e os recursos visuais.

**Arquitetura:** Manter o conteúdo-fonte DocBook e atualizar somente as entradas correspondentes no catálogo gettext existente. Validar o catálogo e compilar a versão `pt_BR` com o ambiente Meson/Ninja já configurado no WSL; cada tópico aprovado recebe seu próprio commit em PT-BR e push para `origin/main`.

**Pilha técnica:** XML DocBook, catálogos gettext `.po`, `msgfmt`, Meson/Ninja, build Linux no WSL e navegador local.

**Especificação:** [2026-11-03-manual-pt-br-translation-design.md](../specs/2026-11-03-manual-pt-br-translation-design.md)

## Restrições globais

- Usar os arquivos de catálogo gettext `.po` existentes em `po/pt_BR/`; não alterar o texto-fonte em XML para contornar uma tradução ausente.
- Manter IDs, URLs, destinos de links e referências cruzadas, nomes próprios, comandos, código, placeholders e marcação DocBook.
- Corrigir ou substituir traduções antigas e entradas fuzzy somente depois de compará-las com o XML atual.
- Para capturas de interface relevantes, usar a interface PT-BR do GIMP sempre que for possível produzir uma captura correta e legível. Guardar a variante em `images/pt_BR/` com a mesma estrutura relativa e o mesmo nome do recurso correspondente em `images/C/`, para que o mecanismo existente de localização por idioma a selecione.
- Não recriar ilustrações conceituais, mascotes ou exemplos independentes de idioma. Usar a imagem original como fallback quando não houver motivo para uma variante localizada.
- Se o tópico passar nas verificações, criar um commit com mensagem em PT-BR e enviá-lo para `origin/main`. Não incluir alterações de outros tópicos no mesmo commit.
- Falhas de build, validação ou envio devem ser reportadas explicitamente e corrigidas antes de declarar o tópico concluído. Não se deve fazer push forçado.

## Foco de revisão

- Entradas `.po` antigas ou fuzzy que não correspondam mais ao XML atual devem ser alinhadas e revisadas antes de compilar.
- Títulos e textos visíveis dos links devem estar em PT-BR, sem alterar IDs, URLs ou destinos; conferir os links no índice renderizado.
- Tags DocBook, placeholders, referências e comandos devem manter a mesma estrutura e sequência do texto-fonte.
- Nomes próprios, nomes de produtos e termos de licença devem permanecer corretos e consistentes.
- Imagens devem resolver pela variante `pt_BR` quando houver uma captura localizada correspondente; se não houver, o HTML deve exibir a imagem original de fallback sem caminho quebrado.

---

### Task 1: Revisar e finalizar a página inicial/índice

**Arquivos:**
- Ler: `src/gimp.xml`
- Modificar: `po/pt_BR/gimp.po`
- Validar: `po/pt_BR/gimp.po`

**Interfaces:**
- Consome a hierarquia, os títulos e as referências de capítulos definidos em `src/gimp.xml`.
- Produz o catálogo atualizado para os títulos e rótulos visíveis do índice em português.

- [ ] **Etapa 1: Comparar o índice-fonte com as traduções atuais**

  Conferir os títulos de livro, partes e capítulos de `src/gimp.xml` com as entradas correspondentes em `po/pt_BR/gimp.po`. Identificar entradas vazias, fuzzy ou antigas que apareçam na página inicial; deixar intactas entradas de outros artigos que não sejam necessárias para alinhar os rótulos do índice.

- [ ] **Etapa 2: Atualizar apenas as traduções necessárias do índice**

  Traduzir ou corrigir os `msgstr` dos rótulos exibidos na página inicial. Preservar cada `msgid`, referência `linkend`, tag e demais marcações. Não alterar a fonte XML.

- [ ] **Etapa 3: Validar o catálogo**

  Executar no PowerShell:

  ```powershell
  wsl -d Debian -- msgfmt --check -o /dev/null /mnt/c/Users/robgo/GIMP/manualGIMP3.2/po/pt_BR/gimp.po
  git diff --check
  ```

  Esperado: `msgfmt` termina sem erro de sintaxe/formatos e `git diff --check` não reporta whitespace inválido.

- [ ] **Etapa 4: Compilar e conferir o índice**

  Copiar o catálogo validado para o clone de build no WSL e compilar:

  ```powershell
  wsl -d Debian -- bash -lc "cp /mnt/c/Users/robgo/GIMP/manualGIMP3.2/po/pt_BR/gimp.po /root/gimp-help-buildsrc/po/pt_BR/gimp.po && meson compile -C /root/gimp-help-build"
  ```

  Abrir ou recarregar `http://127.0.0.1:8765/index.html`. Conferir o título da página, títulos e rótulos do índice, e abrir pelo menos o primeiro link para confirmar que a navegação funciona.

- [ ] **Etapa 5: Commitar somente as alterações do índice**

  Se houver correções necessárias:

  ```powershell
  git add po/pt_BR/gimp.po
  git commit -m "docs(pt_BR): revisa índice do manual" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
  ```

  Esperado: o commit contém somente correções do índice. Depois da revisão independente aprovar a tarefa, o controlador envia esse commit com `git push origin main` e confirma com `git status --short` e `git --no-pager log -1 --oneline`. Se a revisão confirmar que o índice já está completo e não houver diff, não criar commit vazio; registrar que o tópico foi validado e seguir para a próxima tarefa.

---

### Task 2: Atualizar o artigo “Bem-vindo ao GIMP”

**Arquivos:**
- Ler: `src/introduction.xml`
- Ler: `src/gimp.xml`
- Modificar: `po/pt_BR/gimp.po`
- Imagem de referência: `images/C/using/wilber.png` (reutilizar; não criar variante localizada)

**Interfaces:**
- Consome o texto, os títulos, as referências e a ilustração definidos em `src/introduction.xml`.
- Produz traduções PT-BR para as mensagens atuais do artigo, preservando a marcação e os destinos dos links.

- [ ] **Etapa 1: Conferir todas as mensagens atuais do artigo**

  Comparar as mensagens de `src/introduction.xml` com as entradas de `po/pt_BR/gimp.po`, incluindo título, parágrafos, nomes de seções, listas, legendas e links. Reavaliar traduções antigas ou fuzzy com base no texto-fonte atual; não presumir que traduções históricas ainda correspondam ao conteúdo.

- [ ] **Etapa 2: Traduzir e revisar o artigo**

  Atualizar somente as mensagens do artigo “Bem-vindo ao GIMP” em `po/pt_BR/gimp.po`. Usar português brasileiro natural e fiel; preservar nomes, URLs, referências cruzadas, tags DocBook e ordem dos elementos. Manter a ilustração compartilhada de Wilber, pois ela não é uma captura da interface.

- [ ] **Etapa 3: Validar a tradução e a estrutura**

  Executar:

  ```powershell
  wsl -d Debian -- msgfmt --check -o /dev/null /mnt/c/Users/robgo/GIMP/manualGIMP3.2/po/pt_BR/gimp.po
  git diff --check
  ```

  Conferir no diff que a estrutura/tags dos segmentos atualizados corresponde à fonte, que URLs e destinos de referência não mudaram, que nomes próprios e termos de licença correspondem à fonte e que nenhum `msgstr` do artigo está vazio ou marcado como fuzzy.

- [ ] **Etapa 4: Compilar e conferir a página e a ilustração**

  Copiar o catálogo atualizado para `/root/gimp-help-buildsrc/po/pt_BR/gimp.po`, executar `meson compile -C /root/gimp-help-build` no Debian WSL e abrir o artigo pelo índice em `http://127.0.0.1:8765/index.html`. Conferir os textos, links, carregamento da imagem de Wilber e ausência de conteúdo inesperadamente em inglês.

- [ ] **Etapa 5: Commitar somente o artigo**

  ```powershell
  git add po/pt_BR/gimp.po
  git commit -m "docs(pt_BR): traduz artigo de apresentação do GIMP" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
  ```

  Esperado: o commit contém somente as entradas do artigo. Depois da revisão independente aprovar a tarefa, o controlador envia esse commit com `git push origin main` e confirma com `git status --short` e `git --no-pager log -1 --oneline`. O worktree deve ficar limpo.
