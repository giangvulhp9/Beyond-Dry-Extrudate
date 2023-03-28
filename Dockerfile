FROM python:3.8.10-slim as compile-image
RUN apt-get update \
    && apt-get install -y git ssh libgl1-mesa-dev --no-install-recommends

WORKDIR /usr/src/app

# don't write pyc files
# don't buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt

# Copy in Github SSH Key to access private repositories with pip, run pip install, then remove SSH Key
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts && \
    pip install --upgrade pip setuptools wheel --no-cache-dir && \
    pip install -r requirements.txt --no-cache-dir && \
    rm -rf /root/.ssh

# The build image is separate from the compiled image to ensure no private
# layers are exposed
FROM python:3.8.10-slim AS build-image
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 libvips --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=compile-image /usr/local /usr/local

WORKDIR /usr/app/
COPY ./ ./

ENV PYTHONUNBUFFERED 1
EXPOSE 80

LABEL org.opencontainers.image.source=https://github.com/giangvulhp9/Beyond-Dry-Extrudate

RUN find /usr/local/lib/python3.8/site-packages/streamlit -type f \( -iname \*.py -o -iname \*.js \) -print0 | xargs -0 sed -i 's/healthz/health-check/g'

ENTRYPOINT ["streamlit", "run", "Source_Code.py", "--browser.gatherUsageStats=false", "--logger.level=info"]
