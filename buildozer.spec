[app]
# Nome do pacote (sem espaços)
title = SistemaDeGerenciamento

# Nome da aplicação
package.name = sistema_gerenciamento

# Nome do domínio (inverso). Exemplo: org.seuprojeto.nome
package.domain = org.taskmanager

# Arquivo principal da aplicação (mude se for diferente)
source.main = main.py

# Pasta com o código fonte
source.dir = .

# Lista de módulos Python a incluir
requirements = python3,kivy,requests,pyrebase4,certifi

# Orientação da tela: 'portrait', 'landscape' ou 'all'
orientation = portrait

# Ícone do app (opcional, coloque o caminho se tiver)
icon.filename = %(source.dir)s/icon.png

# Armazena dados em local privado
android.private_storage = True

# Versionamento
version = 1.0.0
android.version_code = 1

# Permissões Android que sua aplicação precisa
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Inclui suporte a AndroidX
android.use_androidx = True

# Se usa pyjnius ou outras dependências nativas
# android.add_jars = 

# Arquivos adicionais a incluir no APK
# source.include_exts = py,png,jpg,kv,atlas,json

# Especificar arquitetura (se quiser)
# android.arch = armeabi-v7a, arm64-v8a, x86

# Se quiser logcat sempre que rodar
# log_level = 2

# App fullscreen ou não
fullscreen = 0

# Se usa Kivy, isso é obrigatório
use_kivy = 1

[buildozer]
# Pasta onde será gerado o APK e arquivos temporários
build_dir = ./.buildozer

# Pasta de cache (ajuda a acelerar builds futuras)
cache_dir = ./.buildozer/cache

# Evita limpar builds antigos (se quiser)
# buildozer.always_use_latest_android = True

# Diretório virtualenv, se usar
# venv = venv

# Se quiser depurar mais: --verbose
