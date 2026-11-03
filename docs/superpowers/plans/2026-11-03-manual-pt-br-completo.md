# Tradução integral do Manual do GIMP 3.2 para PT-BR — Plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Traduzir e revisar todo o conteúdo alcançável pelo índice principal do Manual do GIMP 3.2 em português brasileiro, incluindo suas referências e imagens com texto de interface.

**Architecture:** O manual usa fontes DocBook e 12 catálogos gettext; o trabalho atualizará somente os catálogos PT-BR e as variantes de imagem necessárias. A execução seguirá as partes do índice, com validação de cada lote por extração atualizada, gettext, compilação e preview, seguida de uma verificação global.

**Tech Stack:** DocBook XML, gettext (`msgmerge`, `msgfmt`, `msgattrib`), Meson/Ninja, HTML do manual e imagens PNG/SVG.

**Spec:** `docs/superpowers/specs/2026-11-03-manual-pt-br-completo-design.md`

## Global Constraints

- Concluir a tradução para português brasileiro de todo o conteúdo alcançável pelo índice principal do Manual do GIMP 3.2.
- Preservar tags DocBook, atributos, identificadores, links, placeholders, teclas de atalho, comandos, código, nomes próprios e termos de produto conforme o contexto.
- Usar variantes PT-BR com caminho, nome e hash corretos quando forem capturas que contenham texto de interface.
- Não alterar o texto-fonte em inglês nem outros idiomas como parte da tradução.
- Os lotes validados serão commitados e enviados a `origin/main`, mantendo as alterações restritas à tradução PT-BR.

## Review Focus

- **Mensagens atuais omitidas, vazias ou fuzzy:** em cada lote compare os IDs e ocorrências do POT recém-extraído para as fontes do lote com as traduções correspondentes; a checagem deve mostrar zero mensagens vazias/fuzzy nessas fontes.
- **Marcação DocBook, placeholders ou comandos protegidos alterados:** execute `msgfmt --check` nos catálogos tocados e compile o manual do lote; a compilação não deve apresentar erro de marcação ou placeholder.
- **Links internos e xrefs quebrados:** compile o livro inteiro e verifique no HTML gerado as páginas e âncoras de todos os itens do índice; nenhum link interno deve apontar para alvo ausente.
- **Caminho/hash de imagem incorreto ou captura localizada desatualizada:** para cada referência de imagem do lote, confira o caminho, a existência do arquivo e o MD5 contra o arquivo localizado; a compilação e a inspeção do preview devem exibir a variante esperada.
- **Inconsistência terminológica entre catálogos ou alterações fora de escopo:** revise os termos repetidos contra o contexto e compare `git diff --name-only` com os catálogos/imagens do lote; nenhum outro idioma ou texto-fonte pode aparecer no diff.

---

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

### Task 2: Parte “How do I Become a GIMP Wizard?”

**Files:**
- Modify: `po/pt_BR/concepts.po` (fontes `src/concepts/` incluídas nesta parte)
- Modify: `po/pt_BR/using.po` (fontes `src/using/` incluídas nesta parte)
- Modify, se necessário: `images/pt_BR/` com as capturas referenciadas por estas páginas

**Interfaces:**
- Consome: os termos estabelecidos no lote anterior e os POTs atuais de `concepts.po` e `using.po`.
- Produz: mensagens atuais revisadas para Getting Images into GIMP; Getting Images out of GIMP; Painting with GIMP; Combining Images; Text Management; Enhancing Photographs; Color Management with GIMP; Enrich my GIMP; e Scripting and writing plug-ins.

- [ ] **Step 1: Atualizar e delimitar as mensagens desta parte**

Gere os POTs atuais de `concepts.po` e `using.po`; selecione as ocorrências de todos os arquivos incluídos nos nove capítulos desta parte. Confirme se há mensagens compartilhadas com capítulos já concluídos e mantenha uma tradução coerente sem ampliar o diff para fontes não revisadas.

- [ ] **Step 2: Traduzir e revisar todas as mensagens da parte**

Revise as mensagens vazias, fuzzy, obsoletas e as traduções existentes que não correspondam às fontes atuais. Inclua as páginas sobre tipos e carregamento de imagens, formatos e Web, seleções e caminhos, camadas, texto, fotografia, gerenciamento de cores, personalização e scripts.

- [ ] **Step 3: Auditar as imagens da parte**

Verifique cada referência de imagem dos arquivos desta parte, corrigindo caminho e hash e localizando capturas com interface em português quando houver imagem-fonte verificável.

- [ ] **Step 4: Validar a parte**

Execute `msgfmt --check` para `concepts.po` e `using.po`; confirme zero mensagens vazias/fuzzy nas ocorrências desta parte; compile o manual e confira no preview as nove páginas de capítulo e seus links internos.

- [ ] **Step 5: Commitar o lote**

```bash
git add -- po/pt_BR/concepts.po po/pt_BR/using.po
git commit -m "docs(pt_BR): traduz capítulos de edição de imagens" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Se houver imagens alteradas, adicione individualmente somente os caminhos exatos revisados neste lote antes do commit.

### Task 3: Parte “Function Reference”

**Files:**
- Modify: `po/pt_BR/toolbox.po`
- Modify: `po/pt_BR/dialogs.po`
- Modify: `po/pt_BR/menus.po`
- Modify: `po/pt_BR/filters.po`
- Modify, se necessário: `images/pt_BR/` com as capturas referenciadas por estas páginas

**Interfaces:**
- Consome: os termos estabelecidos nas partes anteriores e os POTs atuais dos quatro catálogos.
- Produz: mensagens atuais revisadas para Tools, Dialogs, Menus e Filters, incluindo todas as páginas subordinadas incluídas em `src/gimp.xml`.

- [ ] **Step 1: Atualizar os quatro catálogos e delimitar ocorrências**

Gere os POTs atuais de `toolbox.po`, `dialogs.po`, `menus.po` e `filters.po`. Inclua todas as fontes de ferramentas, diálogos, menus e filtros apontadas pelos capítulos no índice.

- [ ] **Step 2: Traduzir e revisar a referência funcional**

Traduza todas as mensagens atuais e revise traduções existentes contra o texto-fonte. Preserve nomes de operações, parâmetros, identificadores, nomes de filtros, comandos, placeholders e referências cruzadas.

- [ ] **Step 3: Auditar as imagens da referência**

Verifique as imagens chamadas por ferramentas, diálogos, menus e filtros. Corrija hashes/caminhos obsoletos e localize apenas capturas com texto de interface.

- [ ] **Step 4: Validar a referência funcional**

Execute `msgfmt --check` nos quatro catálogos, confirme zero mensagens vazias/fuzzy nas ocorrências dos quatro capítulos e compile/inspecione no preview todas as páginas e links internos da referência.

- [ ] **Step 5: Commitar o lote**

```bash
git add -- po/pt_BR/toolbox.po po/pt_BR/dialogs.po po/pt_BR/menus.po po/pt_BR/filters.po
git commit -m "docs(pt_BR): traduz referência de ferramentas e menus" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Se houver imagens alteradas, adicione individualmente somente os caminhos exatos revisados neste lote antes do commit.

### Task 4: Conteúdo global, referências, glossário e apêndices

**Files:**
- Modify: `po/pt_BR/gimp.po` (mensagens restantes de `src/gimp.xml`, `src/key-reference.xml` e `src/help-missing.xml`)
- Modify: `po/pt_BR/glossary.po`
- Modify: `po/pt_BR/appendix.po`
- Modify, se necessário: `images/pt_BR/` com as capturas referenciadas por estas páginas

**Interfaces:**
- Consome: os termos estabelecidos nas tarefas anteriores e os POTs atuais dos três catálogos.
- Produz: mensagens atuais revisadas para os metadados restantes do livro, a referência de teclas, o glossário e todos os apêndices incluídos.

- [ ] **Step 1: Atualizar e delimitar as mensagens suplementares**

Gere os POTs atuais de `gimp.po`, `glossary.po` e `appendix.po`. Inclua o aviso legal e os títulos do livro, a referência de teclas, o glossário, bibliografia, bugs, contribuição, tutorial de tone mapping, licença FDL e ajuda ausente, conforme as inclusões atuais.

- [ ] **Step 2: Traduzir e revisar todas as mensagens suplementares**

Revise mensagens atuais vazias, fuzzy ou desatualizadas e preserve nomes formais, URLs, teclas, termos jurídicos e identificadores conforme o contexto.

- [ ] **Step 3: Auditar imagens das páginas suplementares**

Confirme as referências e hashes das imagens encontradas nesses arquivos e localize capturas com texto de interface quando aplicável.

- [ ] **Step 4: Validar as páginas suplementares**

Execute `msgfmt --check` nos três catálogos, confirme zero mensagens vazias/fuzzy nas ocorrências suplementares e compile/inspecione as páginas, referências e links no preview.

- [ ] **Step 5: Commitar o lote**

```bash
git add -- po/pt_BR/gimp.po po/pt_BR/glossary.po po/pt_BR/appendix.po
git commit -m "docs(pt_BR): traduz referências e apêndices" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Se houver imagens alteradas, adicione individualmente somente os caminhos exatos revisados neste lote antes do commit.

### Task 5: Auditoria global, build final e publicação

**Files:**
- Verify: os 12 catálogos em `po/pt_BR/`
- Verify: todas as fontes XML alcançáveis a partir de `src/gimp.xml`
- Verify: todas as referências em `images/pt_BR/`
- Modify, somente se a auditoria identificar correções pendentes: catálogos PT-BR ou imagens PT-BR dos lotes anteriores

**Interfaces:**
- Consome: os quatro lotes validados e commitados.
- Produz: um manual integral compilável, com cobertura atual completa e preview revisado.

- [ ] **Step 1: Comparar todos os catálogos com as fontes atuais**

Regere os 12 POTs por meio dos alvos Meson `update-po-pt_BR-appendix.po`, `update-po-pt_BR-concepts.po`, `update-po-pt_BR-dialogs.po`, `update-po-pt_BR-filters.po`, `update-po-pt_BR-gimp.po`, `update-po-pt_BR-glossary.po`, `update-po-pt_BR-introduction.po`, `update-po-pt_BR-menus.po`, `update-po-pt_BR-preface.po`, `update-po-pt_BR-toolbox.po`, `update-po-pt_BR-tutorial.po` e `update-po-pt_BR-using.po`. Confirme que cada mensagem ativa alcançável pelo livro tem tradução não vazia e não fuzzy; descarte entradas obsoletas sem remover mensagens válidas compartilhadas.

- [ ] **Step 2: Verificar todos os catálogos**

Execute `msgfmt --check` para cada arquivo de `po/pt_BR`. Confirme cobertura integral usando os POTs recém-gerados e revise tags/placeholders preservados.

- [ ] **Step 3: Verificar todas as imagens**

Compare as referências do livro com `images/C` e `images/pt_BR`; confirme existência e hash de cada arquivo referenciado. Revise visualmente as variantes localizadas que contêm texto de interface e registre qualquer captura que dependa de revisão externa da equipe de idioma.

- [ ] **Step 4: Compilar e inspecionar o manual integral**

Copie os catálogos PT-BR validados para as árvores de fonte e build do preview (`/root/manualGIMP3.2-preview-src-lf2` e `/root/manualGIMP3.2-preview-build-lf2`), execute `ninja -C /root/manualGIMP3.2-preview-build-lf2` e `ninja -C /root/manualGIMP3.2-preview-build-lf2 test`. Confira que o índice e todas as páginas geradas estão disponíveis em `http://127.0.0.1:8765/pt_BR/`, navegue por todos os itens do índice e confira seus links/âncoras e imagens.

- [ ] **Step 5: Corrigir e revalidar eventuais pendências**

Se a auditoria encontrar mensagens, links ou imagens inválidos, corrija somente os arquivos PT-BR responsáveis, repita as verificações afetadas e registre uma correção final:

Adicione somente os caminhos exatos de catálogos e imagens PT-BR corrigidos, revise o diff staged e crie o commit `docs(pt_BR): corrige pendências da tradução integral` com o trailer de coautoria obrigatório.

- [ ] **Step 6: Publicar e confirmar sincronização**

Envie os commits validados para `origin/main` com `git push origin main`; confirme com `git status --short --branch` que a branch está limpa e sincronizada com `origin/main`.
