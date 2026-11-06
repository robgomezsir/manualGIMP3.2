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
