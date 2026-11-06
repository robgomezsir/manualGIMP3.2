### Task 1: Prefácio e primeira parte do índice

**Files:**
- Modify: `po/pt_BR/preface.po`
- Modify: `po/pt_BR/introduction.po`
- Modify: `po/pt_BR/gimp.po` (somente mensagens de `src/introduction.xml` alcançadas nesta parte)
- Modify: `po/pt_BR/concepts.po` (somente mensagens de `src/concepts/intro.xml`, `concepts.xml`, `basic-setup.xml` e `undo.xml`)
- Modify: `po/pt_BR/tutorial.po` (somente mensagens de `src/tutorial/quickies.xml`)
- Modify: `po/pt_BR/using.po` (somente mensagens de `src/using/getting-unstuck*.xml`)
- Modify, se necessário: `images/pt_BR/` com as capturas referenciadas por estas páginas

**Interfaces:**
- Consome: fontes incluídas pela seção `Getting Started` em `src/gimp.xml` e os POTs atuais dos seis catálogos listados.
- Produz: mensagens atuais revisadas para o prefácio e os capítulos Introduction, Starting GIMP, First Steps with GIMP e What to do if you are stuck.

- [ ] **Step 1: Extrair os catálogos atuais do lote**

Execute os alvos Meson `update-po-pt_BR-preface.po`, `update-po-pt_BR-gimp.po`, `update-po-pt_BR-introduction.po`, `update-po-pt_BR-concepts.po`, `update-po-pt_BR-tutorial.po` e `update-po-pt_BR-using.po` no build do preview. Compare as mensagens extraídas com o conteúdo das fontes indicado acima; trate cada ocorrência compartilhada sem remover traduções de outras partes.

- [ ] **Step 2: Traduzir e revisar todas as mensagens deste lote**

Atualize somente as ocorrências da primeira parte e do prefácio em `po/pt_BR`. Revise também as traduções não fuzzy quando divergirem do texto atual. Preserve os IDs de links, nomes de arquivos, teclas, comandos e marcação DocBook.

- [ ] **Step 3: Auditar as imagens das páginas deste lote**

Para cada imagem referenciada, confirme arquivo e hash. Use imagem PT-BR somente para captura que contenha interface textual e corresponda à fonte; não substitua ilustrações sem texto.

- [ ] **Step 4: Validar o lote**

Execute `msgfmt --check` para os seis catálogos, compare fuzzy/vazias com as ocorrências das fontes deste lote e compile o preview. Confira as páginas de prefácio, introdução, inicialização, primeiros passos e ajuda para problemas no navegador compartilhado.

- [ ] **Step 5: Commitar o lote**

```bash
git add -- po/pt_BR/preface.po po/pt_BR/introduction.po po/pt_BR/gimp.po po/pt_BR/concepts.po po/pt_BR/tutorial.po po/pt_BR/using.po
git commit -m "docs(pt_BR): traduz prefácio e primeiros passos" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Se houver imagens alteradas, adicione individualmente somente os caminhos exatos revisados neste lote antes do commit.

