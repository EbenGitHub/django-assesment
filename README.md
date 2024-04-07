# Django-Assesment

Create a Django API with django rest framework

- [ ]  users with custom roles - admin, coach, agent, football player
- [ ]  sign up and social sign up (google, facebook)
- [ ]  login and social login
- [ ]  password reset



#
## instruction
- to install and run it
```shell
pip install pipenv
pipenv install
pipenv shell
pipenv run start
```
- rountes
    - `/admin/` admin site
    - `/auth/users/` to see lists of users (it requires admin role)
    - `/auth/profile/` to see your info (it requires authentication)
    - `/home/` home page
    - `/` home page
    - `/accounts` allauth routes
    - `/accounts/email/` change remove or add email address
    - `/accounts/logout/` logout
    - `/accounts/login/` login
    - `/accounts/signup/` sign up for new account
    - `/accounts/password/reset/` forgot password / password reset
    - `/api/doc/` swagger documentation
    - `/api/schema/` schema documentaion
    - `/api/redoc/` redoc documentation
- featers
    - social sso
    - role based resource access
    - password reset with allauth
    - signup with allauth