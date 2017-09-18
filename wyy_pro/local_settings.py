AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = [
    "user.auth_backend.UserAuthBackend",
]
APPEND_SLASH=False