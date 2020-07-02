#! Python3
# login_form.py

from django import forms
from django.core.files.storage import default_storage

class ImageForm(forms.Form):
    user_img = forms.ImageField(label="社員画像", required=False, upload_to='../static/Employee/images', blank=True, null=True)

    def uploadFileToTempDir(self):
        print("model form")
        print(self.user_img.name)
#        upload_file = self.cleaned_data['user_img']
#        print(upload_file)
        file_name = default_storage.save(self.user_img.name, self.user_img)
        print(file_name)
        return default_storage.url(file_name)