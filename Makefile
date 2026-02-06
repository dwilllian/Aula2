SHELL := /bin/bash

.PHONY: exams diagrams docx zip build

exams:
	python tools/generate_exams.py

diagrams:
	python tools/render_diagrams.py

docx:
	python tools/md_to_docx.py

zip:
	zip -r provas_v3_profissional.zip provas_v3_profissional

build: exams diagrams docx zip
