from django import forms
from .models import cosmetics,ask



class cosmeticForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(cosmeticForm,self).__init__(*args,**kwargs)
        for item in asked.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    class Meta:
        model = cosmetics
        fields = ['id','title','caption','category','image','price']


class asked(forms.Form):
    def __init__(self, *args, **kwargs):
        super(asked, self).__init__(*args, **kwargs)
        for item in asked.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    title = forms.CharField(label='Title', max_length=200, required=True)
    caption = forms.CharField(label='Caption', required=True, widget=forms.Textarea())
    id = forms.IntegerField(label='', required=True, widget=forms.HiddenInput(), initial="0")
    product_id = forms.IntegerField(label='', required=True, widget=forms.HiddenInput())
