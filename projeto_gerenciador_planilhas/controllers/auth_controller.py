from config import ADMIN_USERS, PERMISSIONS

def is_admin(user_email):
    """Verifica se o usuário é administrador."""
    return user_email in ADMIN_USERS

def has_permission(user_role, permission):
    """Verifica se o usuário possui permissão para uma ação específica."""
    return PERMISSIONS.get(user_role, {}).get(permission, False)
