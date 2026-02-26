# Usamos re para trabajar con regex
import re

# Abrimos el archivo original
with open("preproinsulin-seq.txt", "r") as file:
    raw_data = file.read()

# Eliminar la palabra ORIGIN (ignorando mayúsculas/minúsculas)
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

# Eliminar el terminador //
clean_data = clean_data.replace("//", "")

# Eliminar cualquier cosa que no sea letra
clean_data = re.sub("[^A-Za-z]", "", clean_data)

# Convertir todo a mayúsculas
clean_data = clean_data.upper()

# Sobrescribir el archivo original con la versión limpia
with open("preproinsulin-seq.txt", "w") as file:
    file.write(clean_data)

print("Longitud preproinsulina =", len(clean_data))

# Validar longitud esperada
if len(clean_data) != 110:
    print("ERROR: La secuencia no tiene 110 caracteres")
    exit()

# -----------------------------
# Extracción correcta de partes
# -----------------------------

# 0–23  (24 caracteres)
lsinsulin = clean_data[0:24]

# 24–53 (30 caracteres)
binsulin = clean_data[24:54]

# 54–88 (35 caracteres)
cinsulin = clean_data[54:89]

# 89–109 (21 caracteres)
ainsulin = clean_data[89:110]

# -----------------------------
# Guardar cada segmento
# -----------------------------

with open("lsinsulin-sec-clean.txt", "w") as file:
    file.write(lsinsulin)

with open("binsulin-sec-clean.txt", "w") as file:
    file.write(binsulin)

with open("cinsulin-sec-clean.txt", "w") as file:
    file.write(cinsulin)

with open("ainsulin-sec-clean.txt", "w") as file:
    file.write(ainsulin)

# -----------------------------
# Verificación de longitudes
# -----------------------------

print("lsinsulin =", len(lsinsulin))
print("binsulin =", len(binsulin))
print("cinsulin =", len(cinsulin))
print("ainsulin =", len(ainsulin))

# Insulina procesada (B + A)
insulin = binsulin + ainsulin

print("Insulina procesada =", len(insulin))
print("Secuencia de la insulina =", insulin)