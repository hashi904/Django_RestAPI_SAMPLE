from accounts.serializer import UserSerializer

#ログイン時にトークンとユーザー情報を返す
def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }