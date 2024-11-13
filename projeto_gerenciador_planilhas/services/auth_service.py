from config import ADMIN_USERS, PERMISSIONS

def is_admin(user_email):
    """Verifica se o usuário é um administrador."""
    return user_email in ADMIN_USERS

def get_user_permissions(user_role):
    """Retorna as permissões para o perfil de usuário especificado."""
    return PERMISSIONS.get(user_role, {})

def has_permission(user_role, action):
    """Verifica se o perfil do usuário tem permissão para a ação."""
    return PERMISSIONS.get(user_role, {}).get(action, False)