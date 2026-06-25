# ============================================================================
#  Makefile - pintool resolutor del reto AES
#
#    make            compila el pintool .so
#    make run        compila (si hace falta) y lanza Pin sobre el binario,
#                    generando la password
#    make clean      limpia los artefactos
#
#  Variables (se pueden pasar en la linea de comandos):
#    PIN_ROOT   carpeta de Intel Pin (la que contiene el ejecutable 'pin').
#               Si ya la tienes exportada en el entorno, se usa esa.
#    TARGET     binario del reto a instrumentar      (def: ./encrypted_box)
#    PW         fichero de salida con la password    (def: password.bin)
#
#    Ejemplos:  make run 
#				make run TARGET=./challenge_name
#				make run PW=solution.bin
#				make run TARGET=./challenge_name PW=solution.bin
#
#  El pintool se construye delegando en la PROPIA infraestructura de Pin
#  (makefile.config + makefile.default.rules), asi los flags de compilacion y
#  enlace los pone Pin segun la version instalada (4.2 difiere de 3.x).
#  Las instrucciones AES-NI compilan gracias al atributo 'target' del fuente.
# ============================================================================

PIN_ROOT ?= /opt/pin
PIN_TOOL := obj-intel64/solver_pintool.so
TARGET   ?= ./encrypted_box
PW       ?= password.bin

# Target por defecto: construir el pintool.
pintool: $(PIN_TOOL)

# ---------------------------------------------------------------------------
#  Construccion del .so (solo se rehace si cambia el fuente).
#  Generamos al vuelo un makefile minimo que incluye la config de Pin.
# ---------------------------------------------------------------------------
$(PIN_TOOL): solver_pintool.cpp
	@mkdir -p obj-intel64
	@echo 'PIN_ROOT := $(PIN_ROOT)'                              >  .pintool.mk
	@echo 'CONFIG_ROOT := $$(PIN_ROOT)/source/tools/Config'      >> .pintool.mk
	@echo 'include $$(CONFIG_ROOT)/makefile.config'              >> .pintool.mk
	@echo 'include $$(TOOLS_ROOT)/Config/makefile.default.rules' >> .pintool.mk
	$(MAKE) -f .pintool.mk $(PIN_TOOL)
	@rm -f .pintool.mk
	@echo "Pintool construido: $(PIN_TOOL)"

# ---------------------------------------------------------------------------
#  Compilar (si hace falta) y ejecutar bajo Pin.
# ---------------------------------------------------------------------------
run: $(PIN_TOOL)
	@test -x "$(PIN_ROOT)/pin" || { echo "ERROR: no encuentro $(PIN_ROOT)/pin (ajusta PIN_ROOT)"; exit 1; }
	@test -e "$(TARGET)"       || { echo "ERROR: no encuentro el binario: $(TARGET) (pasa TARGET=...)"; exit 1; }
	@echo ">> Lanzando Pin sobre $(TARGET) (password -> $(PW))"
	"$(PIN_ROOT)/pin" -t $(PIN_TOOL) -o $(PW) -- $(TARGET)

clean:
	rm -rf obj-intel64 .pintool.mk

.PHONY: pintool run clean
