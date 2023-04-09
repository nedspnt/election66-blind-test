# election66-blind-test
Which party will you select if you only consider their policies? A streamlit app

### Prepare an environment
```buildoutcfg
virtualenv venv-election66
source venv-election66/bin/activate
pip install -r requirements.txt
```

### Test on local machine

Test with streamlit run
```buildoutcfg
streamlit run app.py
```
By default, this should open http://localhost:8501

Test with Docker
```
docker build -t election66-blind-test:latest .
docker run -p 8501:8501 election66-blind-test:latest
```
It is expected that the urls won't be accessible, since it's running on the container. See https://discuss.streamlit.io/t/application-doesnt-open-on-network-and-external-url/19568 for more details.

### Run on a Cloud Run on GCP

After creating a project, and enable Cloud Run API
```
gcloud auth login
gcloud config set project <PROJECT_ID>
```

```
gcloud auth configure-docker
```


Config the cloudbuild.yaml file
```
 gcloud builds submit --region=<REGION>
```