# Overview
Simple FastAPI application with CI/CD pipeline, includes 4 stages:
- python lint
- smoke test
- build docker image
- deployment to heroku
# Add some features:
- new ep with environ variable $CI_COMMIT_SHA or default value
- sed it code? build arg to docker?
- Test this?  
- add new jobs: docker push to registry, teardown heroku runtime
