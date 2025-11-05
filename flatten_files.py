import os
import shutil
import sys


def count_files(folder):
    """Cuenta el número total de archivos en una carpeta recursivamente."""
    total = 0
    for _, _, files in os.walk(folder):
        total += len(files)
    return total


def safe_copy(src_file, dst_file, duplicate_mode="rename"):
    """
    Copia un archivo resolviendo duplicados según el modo:
    - 'rename': renombra (archivo_1.ext)
    - 'overwrite': sobrescribe
    - 'skip': ignora si ya existe
    """
    if os.path.exists(dst_file):
        if duplicate_mode == "skip":
            return False
        elif duplicate_mode == "overwrite":
            pass  # shutil.copy2 sobrescribirá
        elif duplicate_mode == "rename":
            name, ext = os.path.splitext(os.path.basename(src_file))
            counter = 1
            while os.path.exists(dst_file):
                dst_file = os.path.join(
                    os.path.dirname(dst_file), f"{name}_{counter}{ext}"
                )
                counter += 1
        else:
            raise ValueError("Modo de duplicado no válido.")

    try:
        shutil.copy2(src_file, dst_file)
        return True
    except (OSError, IOError) as e:
        print(f"\n❌ Error al copiar '{src_file}': {e}", file=sys.stderr)
        return False


def flatten_and_copy(src, dst, duplicate_mode="rename", show_progress=True):
    """Copia todos los archivos de src a dst sin subcarpetas."""
    if not os.path.exists(src):
        raise ValueError(f"La carpeta de origen no existe: {src}")
    os.makedirs(dst, exist_ok=True)

    total = count_files(src)
    if total == 0:
        if show_progress:
            print("⚠️  No se encontraron archivos para copiar.")
        return 0

    copied = 0
    current = 0

    for root, _, files in os.walk(src):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst, file)

            if safe_copy(src_file, dst_file, duplicate_mode):
                copied += 1

            current += 1
            if show_progress:
                percent = (current / total) * 100
                bar = "█" * int(percent / 2) + "░" * (50 - int(percent / 2))
                sys.stdout.write(f"\r[{bar}] {percent:.1f}% ({current}/{total})")
                sys.stdout.flush()

    if show_progress:
        print()  # Nueva línea al final
    return copied


def interactive_mode():
    print("=== Aplanar y copiar archivos ===\n")
    src = input("Ruta de la carpeta original: ").strip()
    while not os.path.exists(src):
        print("❌ La carpeta no existe. Intente de nuevo.")
        src = input("Ruta de la carpeta original: ").strip()

    dst = input("Ruta de la carpeta de destino: ").strip()

    print("\n¿Qué hacer con archivos duplicados?")
    print("1) Renombrar (predeterminado)")
    print("2) Sobrescribir")
    print("3) Saltar")
    choice = input("Seleccione (1/2/3): ").strip()
    mode_map = {"1": "rename", "2": "overwrite", "3": "skip"}
    mode = mode_map.get(choice, "rename")

    try:
        copied = flatten_and_copy(src, dst, duplicate_mode=mode, show_progress=True)
        print(f"\n✅ ¡Listo! {copied} archivos copiados.")
    except Exception as e:
        print(f"\n💥 Error fatal: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) == 1:
        # Modo interactivo
        interactive_mode()
    elif len(sys.argv) in (3, 4):
        # Modo CLI: script.py origen destino [modo]
        src = sys.argv[1]
        dst = sys.argv[2]
        mode = sys.argv[3] if len(sys.argv) == 4 else "rename"
        if mode not in ("rename", "overwrite", "skip"):
            print("Modo debe ser: rename, overwrite o skip", file=sys.stderr)
            sys.exit(1)
        try:
            copied = flatten_and_copy(src, dst, duplicate_mode=mode, show_progress=False)
            print(f"Éxito: {copied} archivos copiados a '{dst}'", file=sys.stderr)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Uso:", file=sys.stderr)
        print("  Interactivo: python flatten_copy.py", file=sys.stderr)
        print("  CLI: python flatten_copy.py <origen> <destino> [rename|overwrite|skip]", file=sys.stderr)
        sys.exit(1)

    input("Presione Enter para salir...")  # Solo en modo interactivo, al final


if __name__ == "__main__":
    main()