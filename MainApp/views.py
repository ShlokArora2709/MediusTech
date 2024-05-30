from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd

def home(request):
    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            df=pd.read_excel(file,0)
            mod_df=df.groupby(['Cust State','DPD']).size().reset_index(name='Count')
            df_html = mod_df.to_html(index=False)
            return render(request, 'index.html', {'form': form,'df_html': df_html})
    else:
        form = UploadFileForm()
        return render(request, 'index.html', {'form': form})