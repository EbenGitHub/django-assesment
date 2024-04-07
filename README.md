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
    - `/home/` home page
    - `/accounts` allauth routes
    - `api/doc` swagger documentation
    - `/auth/*` authentication route
- featers
    - social sso
    - role based resource access
    - password reset with allauth
    - signup with allauth