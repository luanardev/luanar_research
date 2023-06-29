from authlib.integrations.django_client import OAuth
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.contrib import auth
from account.models import User

STATE_CODE_LENGTH = 20

# Init the OAuth
oauth = OAuth()

oauth.register(
    name='luanar',
    client_id='995c312b-2302-4d74-a948-f047346075c8',
    client_secret='JGipgTJ3cNh0pBXUcIn1z2pu0Lpiz62GcHvGljjn',
    access_token_url='https://accounts.luanar.ac.mw/oauth/token',
    access_token_params=None,
    authorize_url='https://accounts.luanar.ac.mw/oauth/authorize',
    authorize_params=None,
    client_kwargs={'scope': 'view-user'},
)


def login(request):
    redirect_uri = 'https://research.luanar.ac.mw/oauth/authorize'
    state = get_random_string(STATE_CODE_LENGTH)
    request.session['session_state'] = state
    extra_para = {'state': state}
    return oauth.luanar.authorize_redirect(request, redirect_uri, **extra_para)


def authorize(request):  
    token = oauth.luanar.authorize_access_token(request)
    response = oauth.luanar.get('https://accounts.luanar.ac.mw/api/staff', token=token)
    response.raise_for_status()
    userinfo = response.json()
    
    user = User.objects.filter(email=userinfo['email']).first()
    if(user is None):
        user = save_user(userinfo)
    
    auth.login(request, user)
    return redirect('dashboard')
  
  
def save_user(userinfo):
 
    user = User.objects.create_user(
        email=userinfo['email'], 
        username=userinfo['email'],
        title=userinfo['title'],
        first_name=userinfo['firstname'], 
        last_name=userinfo['lastname'],
        position=userinfo['position'],
        department_code=userinfo['department_code'],
        campus_code=userinfo['campus_code'],
        image_path=userinfo['profile_photo_url'] 
    )
    
    user.set_password(None)
    user.save()
    return user

   
    

    