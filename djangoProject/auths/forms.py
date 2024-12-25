from django import forms


class Login(forms.Form):
    def __init__(self, *args , **kwargs):
        super(Login,self).__init__(*args , **kwargs)
        for item in Login.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    UserName=forms.CharField(required=True,label="username")
    Password=forms.CharField(required=True,label="password",widget=forms.PasswordInput)

class Register(forms.Form):
    def __init__(self, *args , **kwargs):
        super(Register,self).__init__(*args , **kwargs)
        for item in Login.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    UserName = forms.CharField(required=True, label="username")
    Email= forms.CharField(required=True,label="Email")
    Password= forms.CharField(required=True,label="password",widget=forms.PasswordInput)
