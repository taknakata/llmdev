import pytest
from authenticator import Authenticator

# register() メソッドで、ユーザーが正しく登録される
def test_register_user_success():
    auth = Authenticator()
    auth.register("testuser", "password123")
    assert "testuser" in auth.users
    assert auth.users["testuser"] == "password123"

# register() メソッドで、すでに存在するユーザー名で登録を試みた場合に、エラーメッセージが出力されるか
def test_register_user_error():
    auth = Authenticator()
    auth.register("testuser", "password123")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        auth.register("testuser", "newpassword")

# login() メソッドで、正しいユーザー名とパスワードでログインできるか
def test_login_success():
    auth = Authenticator()
    auth.register("testuser", "password123")
    result = auth.login("testuser", "password123")
    assert result == "ログイン成功"

# login() メソッドで、誤ったパスワードでエラーが出るか
def test_login_error():
    auth = Authenticator()
    auth.register("testuser", "password123")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        auth.login("testuser", "wrongpassword")