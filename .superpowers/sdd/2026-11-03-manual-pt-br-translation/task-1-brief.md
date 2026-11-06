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

