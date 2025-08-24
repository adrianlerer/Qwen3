#!/bin/bash

# 🔒 SCRIPT DE MIGRACIÓN A REPOSITORIO PRIVADO
# Para resolver el problema de fork que no puede ser privado

set -e  # Salir en caso de error

echo "🔄 MIGRANDO QWEN3 ENHANCED A REPOSITORIO PRIVADO..."
echo "=================================================="

# Variables de configuración
OLD_REPO="adrianlerer/Qwen3"
NEW_REPO="adrianlerer/Qwen3-Enhanced-Private"
BRANCH="main"

# Función para mostrar status
show_status() {
    echo "✅ $1"
}

# Función para mostrar errores
show_error() {
    echo "❌ ERROR: $1"
    exit 1
}

# Verificar que estamos en el directorio correcto
if [ ! -d ".git" ]; then
    show_error "No estás en un directorio git. Ejecuta desde /home/user/webapp"
fi

show_status "Verificando estado del repositorio actual..."
git status --porcelain > /dev/null || show_error "Hay cambios sin commitear"

# Mostrar información actual
echo ""
echo "📊 ESTADO ACTUAL:"
echo "Directorio: $(pwd)"
echo "Branch actual: $(git branch --show-current)"
echo "Remotes actuales:"
git remote -v

echo ""
echo "🎯 CONFIGURACIÓN DE MIGRACIÓN:"
echo "Repositorio origen (fork): $OLD_REPO"  
echo "Repositorio destino (privado): $NEW_REPO"
echo "Branch: $BRANCH"

echo ""
read -p "¿Continuar con la migración? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Migración cancelada."
    exit 1
fi

echo ""
echo "🚀 INICIANDO MIGRACIÓN..."

# Paso 1: Crear backup del estado actual
show_status "Creando backup de configuración actual..."
git remote -v > .git_remotes_backup.txt
git branch -a > .git_branches_backup.txt

# Paso 2: Agregar el nuevo repositorio remoto
show_status "Configurando nuevo repositorio privado como remote..."
if git remote | grep -q "^private$"; then
    echo "   - Removiendo remote 'private' existente..."
    git remote remove private
fi

# URL del nuevo repositorio (será creado manualmente)
git remote add private "https://github.com/$NEW_REPO.git"

# Paso 3: Verificar que todos los cambios estén commiteados
show_status "Verificando que todos los cambios estén guardados..."
if [ -n "$(git status --porcelain)" ]; then
    show_error "Hay cambios sin commitear. Commitea primero todos los cambios."
fi

# Paso 4: Crear tag de backup
show_status "Creando tag de backup..."
BACKUP_TAG="backup-before-private-$(date +%Y%m%d-%H%M%S)"
git tag "$BACKUP_TAG"

echo ""
echo "📋 SIGUIENTE PASO MANUAL REQUERIDO:"
echo "=================================="
echo ""
echo "1. VE A: https://github.com/new"
echo "2. CONFIGURA EL REPOSITORIO:"
echo "   - Repository name: Qwen3-Enhanced-Private"  
echo "   - Description: Enhanced Qwen3 implementation with proprietary improvements"
echo "   - ✅ MARCAR COMO PRIVATE"
echo "   - ✅ Add a README file"
echo "   - ❌ NO agregar .gitignore (ya tenemos)"
echo "   - ❌ NO elegir licencia (es propietario)"
echo "3. CLICK 'Create repository'"
echo ""
echo "4. DESPUÉS DE CREAR EL REPOSITORIO, EJECUTA:"
echo "   ./complete_migration.sh"

# Crear script de continuación
cat > complete_migration.sh << 'EOF'
#!/bin/bash

set -e

echo "🔄 COMPLETANDO MIGRACIÓN A REPOSITORIO PRIVADO..."

NEW_REPO="adrianlerer/Qwen3-Enhanced-Private"
BRANCH="main"

# Verificar que el repositorio remoto existe
echo "🔍 Verificando que el repositorio privado existe..."
git ls-remote private > /dev/null 2>&1 || {
    echo "❌ ERROR: El repositorio privado no existe o no es accesible."
    echo "   Asegúrate de haber creado: https://github.com/$NEW_REPO"
    echo "   Y que sea PRIVADO desde el inicio."
    exit 1
}

# Push todo al repositorio privado
echo "📤 Subiendo todo el código al repositorio privado..."
git push private main --force

# Push todas las ramas si existen
echo "📤 Subiendo todas las ramas..."
git push private --all --force

# Push todos los tags
echo "🏷️  Subiendo todos los tags..."
git push private --tags --force

# Cambiar origin al repositorio privado
echo "🔄 Configurando repositorio privado como origin principal..."
git remote remove origin
git remote rename private origin

# Verificar la configuración final
echo ""
echo "✅ MIGRACIÓN COMPLETADA!"
echo "======================"
echo ""
echo "📊 CONFIGURACIÓN FINAL:"
echo "Repositorio privado: https://github.com/$NEW_REPO"
echo "Remotes actuales:"
git remote -v

echo ""
echo "🎯 PRÓXIMOS PASOS:"
echo "1. Verifica que el repositorio sea PRIVADO: https://github.com/$NEW_REPO"
echo "2. Configura colaboradores si necesario"
echo "3. Actualiza documentación con nueva URL"
echo "4. Considera archivar el fork original"

echo ""
echo "🛡️ TU PROPIEDAD INTELECTUAL AHORA ESTÁ PROTEGIDA! 🛡️"
EOF

chmod +x complete_migration.sh

echo ""
show_status "Script de migración preparado."
echo "Tag de backup creado: $BACKUP_TAG"
echo "Configuración guardada en: .git_remotes_backup.txt"
echo ""
echo "🎯 EJECUTA LOS PASOS MANUALES ARRIBA, LUEGO:"
echo "   ./complete_migration.sh"
echo ""
echo "🛡️ ¡Tu código mejorado estará protegido en repositorio privado!"