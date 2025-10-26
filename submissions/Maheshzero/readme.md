# maheshzero-flask
# maheshzero-flask

CI/CD Pipeline Challenge Submission

Author: Mahesh S (@mahes)

---

## Docker image

Docker Hub: https://hub.docker.com/repository/docker/maheshzero/maheshzero-flask

Pull the image:

```powershell
docker pull maheshzero/maheshzero-flask:latest
```

Run the container (this project runs Gunicorn on port 8000):

```powershell
docker run --rm -p 8000:8000 -e SECRET_KEY="your-secret" maheshzero/maheshzero-flask:latest
```

If you want a quick development run with the built-in dev secret (not for production):

```powershell
docker run --rm -p 8000:8000 -e FLASK_DEBUG=true maheshzero/maheshzero-flask:latest
```

## CI/CD pipeline overview

The Jenkins pipeline implemented for this challenge includes the following stages:

1. Checkout — clone the repository from GitHub
2. Build — build a Docker image (tagged `maheshzero/maheshzero-flask:latest`)
3. Test — run pytest inside the container
4. Push — push the image to Docker Hub
5. Deploy — run the container (in the challenge this was demonstrated locally)

All pipeline stages ran successfully for this submission and tests passed.

## Screenshots

Screenshots showing the pipeline and container run are included in the `screenshots/` folder next to this README.

- `screenshots/dockherhub-success.png` — image push to Docker Hub
- `screenshots/jenskinsfile-succes.png` — Jenkinsfile execution success
- `screenshots/pipeline-stages.png` — pipeline stages overview
- `screenshots/test-runapp.png` — running the app and test output

You can view them locally by opening the files in `submissions/Maheshzero/screenshots/`.

---


