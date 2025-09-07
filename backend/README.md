## ConnectInno Notes - Backend (FastAPI)

FastAPI backend. Kimlik dogrulama Firebase ID Token ile, veri saklama Firestore uzerinden yapilir.

### Kurulum

1. Python 3.10+ kurulu olmali.
2. Sanal ortam ve kutuphaneler:

```
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt
```

3. Ortam degiskenleri icin `.env` olusturun(Ben example olarak bıraktım şuan) :

```
FIREBASE_PROJECT_ID=connectinno-notes-baea3
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-fbsvc@connectinno-notes-baea3.iam.gserviceaccount.com
OPENAI_API_KEY=
```

### Calistirma

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Endpointler

- GET `/health`
- GET `/notes/`
- POST `/notes/`
- PUT `/notes/{note_id}`
- DELETE `/notes/{note_id}`

Tum notes endpointleri Authorization ile koruyoruz.

Mehmet Emin Tok
mhmtmntok@gmail.com
+90 534 211 9155
