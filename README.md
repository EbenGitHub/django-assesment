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
- feature
    - home page implemented at `/home/`. `/`also redirects to home page `/home/`
    - email and password based authentication for both sign up and login
    - remember me 
    - social sso authentication using google and facebook, for both signup and login
    - forgot password, password reset, and the email message to be sent will be logged in the terminal
    - change email, add another email, make primary email, resend verification, remove email
    - change password
    - if the logged in user has admin role, in home page there will be button to see all lists of users
    - if non admin users access that page, it will return unauthorized page because that route has authenticated and role based access.
    - customized and stylyzed the look and feel of default allauth template with bootstrap4 and crispyform
    - added swagger documentation using drf spectacular, custom decorators, custom user model, and serializer
    - used pipenv for package management.. all used package is found in pipefile, and make custom scripts to run for repetitive tasks such as running server, making migrations and applying migrations
    - ad
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