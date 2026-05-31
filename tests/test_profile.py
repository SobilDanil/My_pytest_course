def test_profile_page_for_admin(admin_user):
    assert admin_user.name == "admin"
    assert admin_user.is_admin()