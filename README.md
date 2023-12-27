# **Proyek-Analisa-Data-Python**

## Set up Environment:
pipenv --python 3.11
pipenv --venv | ForEach-Object { . $_\Scripts\activate }
pipenv shell
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
exit

## Run Streamlit App:
streamlit run dashboard.py

## Requirements.txt:
pip install pipreqs
pipreqs .

Happy Analyze!