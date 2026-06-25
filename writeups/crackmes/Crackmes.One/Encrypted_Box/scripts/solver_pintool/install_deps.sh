#!/usr/bin/env bash
#
# install_deps.sh - Instala todo lo necesario para compilar y ejecutar el
#                   pintool resolutor del reto AES.
#
#   Dependencias:
#     - g++ / make            (desde el gestor de paquetes del sistema)
#     - Intel Pin 4.2         (se descarga de Intel; no esta en los repos)
#
#   Uso:
#     ./install_deps.sh
#
#   Variables que puedes sobreescribir:
#     PIN_NAME          nombre del kit (carpeta y tarball, sin .tar.gz)
#     PIN_URL           URL completa del .tar.gz
#     PIN_INSTALL_DIR   donde extraer Pin (por defecto /opt)
#
#   Solo Linux x86-64.
#
set -euo pipefail

# ----------------------------------------------------------------------------
# Configuracion (Intel Pin 4.2)
# ----------------------------------------------------------------------------
PIN_NAME="${PIN_NAME:-pin-external-4.2-99776-g21d818fa2-gcc-linux}"
PIN_URL="${PIN_URL:-https://software.intel.com/sites/landingpage/pintool/downloads/${PIN_NAME}.tar.gz}"
PIN_INSTALL_DIR="${PIN_INSTALL_DIR:-/opt}"
PIN_ROOT="${PIN_INSTALL_DIR}/${PIN_NAME}"

# sudo solo si no somos root
if [ "$(id -u)" -eq 0 ]; then SUDO=""; else SUDO="sudo"; fi

log()  { printf '\033[1;32m[+]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[!]\033[0m %s\n' "$*"; }
err()  { printf '\033[1;31m[x]\033[0m %s\n' "$*" >&2; }

# ----------------------------------------------------------------------------
# 1. Comprobaciones previas
# ----------------------------------------------------------------------------
if [ "$(uname -s)" != "Linux" ] || [ "$(uname -m)" != "x86_64" ]; then
    err "Este script es solo para Linux x86-64 (detectado: $(uname -s) $(uname -m))."
    exit 1
fi

# ----------------------------------------------------------------------------
# 2. Herramientas de compilacion (segun el gestor de paquetes)
# ----------------------------------------------------------------------------
install_build_tools() {
    log "Instalando herramientas de compilacion..."
    if   command -v apt-get >/dev/null; then
        $SUDO apt-get update
        $SUDO apt-get install -y --no-install-recommends build-essential wget tar ca-certificates
    elif command -v dnf >/dev/null; then
        $SUDO dnf install -y gcc gcc-c++ make wget tar ca-certificates
    elif command -v yum >/dev/null; then
        $SUDO yum install -y gcc gcc-c++ make wget tar ca-certificates
    elif command -v pacman >/dev/null; then
        $SUDO pacman -Sy --needed --noconfirm base-devel wget tar ca-certificates
    elif command -v zypper >/dev/null; then
        $SUDO zypper install -y gcc gcc-c++ make wget tar ca-certificates
    else
        err "No reconozco el gestor de paquetes. Instala manualmente: g++, make, wget, tar."
        exit 1
    fi
}

# ----------------------------------------------------------------------------
# 3. Intel Pin
# ----------------------------------------------------------------------------
install_pin() {
    if [ -x "${PIN_ROOT}/pin" ]; then
        log "Pin ya esta instalado en ${PIN_ROOT}, no lo descargo de nuevo."
        return
    fi

    log "Descargando Pin desde: ${PIN_URL}"
    local tmp
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' RETURN

    if command -v wget >/dev/null; then
        wget -q --show-progress -O "${tmp}/pin.tar.gz" "${PIN_URL}"
    else
        curl -fL -o "${tmp}/pin.tar.gz" "${PIN_URL}"
    fi

    log "Extrayendo en ${PIN_INSTALL_DIR}..."
    $SUDO mkdir -p "${PIN_INSTALL_DIR}"
    $SUDO tar -xzf "${tmp}/pin.tar.gz" -C "${PIN_INSTALL_DIR}"

    # El kit conserva el uid/gid y los permisos del empaquetador de Intel, que
    # pueden dejar la carpeta inaccesible para tu usuario. La normalizamos:
    # dueño root y lectura/traverse para todos (X = +x solo en dirs/ejecutables).
    if [ -d "${PIN_ROOT}" ]; then
        $SUDO chown -R 0:0 "${PIN_ROOT}" 2>/dev/null || true
        $SUDO chmod -R a+rX "${PIN_ROOT}"
    fi

    if [ ! -x "${PIN_ROOT}/pin" ]; then
        err "No encuentro un 'pin' ejecutable en ${PIN_ROOT}."
        err "Comprueba como se llamo la carpeta extraida:"
        err "    ls -d ${PIN_INSTALL_DIR}/pin*"
        err "y reejecuta con  PIN_NAME=<carpeta>  si difiere de PIN_NAME."
        exit 1
    fi
    log "Pin instalado en ${PIN_ROOT}"
}

# ----------------------------------------------------------------------------
# 4. Variable de entorno PIN_ROOT (persistente en ~/.bashrc)
# ----------------------------------------------------------------------------
setup_env() {
    local line="export PIN_ROOT=\"${PIN_ROOT}\""
    local rc added=0

    # Escribimos en los rc que existan (la sintaxis 'export' vale en bash y zsh).
    for rc in "${HOME}/.zshrc" "${HOME}/.bashrc"; do
        [ -f "${rc}" ] || continue
        if ! grep -qsF "${line}" "${rc}"; then
            printf '\n# Intel Pin (anadido por install_deps.sh)\n%s\n' "${line}" >> "${rc}"
            log "PIN_ROOT anadido a ${rc}"
        fi
        added=1
    done

    if [ "${added}" -eq 0 ]; then
        warn "No vi ~/.zshrc ni ~/.bashrc. Anade esta linea a tu shell rc:"
        warn "    ${line}"
    fi
    export PIN_ROOT
}

# ----------------------------------------------------------------------------
# Ejecucion
# ----------------------------------------------------------------------------
install_build_tools
install_pin
setup_env

log "Dependencias listas."
echo
echo "  PIN_ROOT = ${PIN_ROOT}"
echo
echo "  Compilar el pintool:"
echo "    make pintool PIN_ROOT=\"${PIN_ROOT}\""
echo
echo "  Lanzar el binario bajo Pin (genera password.txt):"
echo "    \"${PIN_ROOT}/pin\" -t obj-intel64/solver_pintool.so -o password.txt -- ./binario_reto"
echo
warn "Pin necesita ptrace sobre el proceso objetivo. Si al lanzarlo ves"
warn "'Unable to PTRACE', habilitalo en esta sesion con:"
warn "    sudo sysctl -w kernel.yama.ptrace_scope=0"
echo
warn "Abre una terminal nueva (o ejecuta 'source ~/.bashrc') para que PIN_ROOT"
warn "este disponible automaticamente."
