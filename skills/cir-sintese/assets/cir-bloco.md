# Contrato do bloco local v1

A projeção canônica vai num único bloco cercado json cir-sintese-v1 em 06-blocos.md. Cada bloco: id, secao, origem {arquivo, commit completo, sha256 do arquivo, item}. A origem é registro JSON/projeção Markdown com schema_version 1 e itens [{id,tipo,tema,subetapa,registro,texto,dados}]. Texto e dados são copiados desse objeto, não reescritos no manifesto. Superado_por aponta a sucessor existente. O registrar.py real precisa adotar/adaptar o contrato; este arquivo não instala a integração.
