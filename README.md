# Pacote de Provas Técnicas v3 (Profissional)

Este repositório gera provas técnicas por cargo e nível com questões originais, diagramas em PNG e DOCX final.

## Requisitos locais

- Python 3.10+
- graphviz (`dot`)
- pandoc

## Build determinístico

```bash
make exams
make diagrams
make docx
make zip
```

Ou use o atalho:

```bash
make build
```

### Semente

Para gerar com outra semente:

```bash
python tools/generate_exams.py --seed 123
```

## Saídas

- `provas_v3_profissional/` com Markdown e gabaritos.
- `provas_v3_profissional/assets/diagrams/` com PNGs.
- `provas_v3_profissional/docx/` com DOCX.
- `provas_v3_profissional/MANIFEST.json` com hashes e métricas.
- `provas_v3_profissional.zip` com o pacote final.
