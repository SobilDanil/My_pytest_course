def test_settings_access(admin_user):
    if admin_user.is_admin():
        print("Доступ к настройкам разрешен")
    assert admin_user.role == "admin"