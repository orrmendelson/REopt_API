FROM reopt/py38

# Install NREL root certs for machines running on NREL's network.
ARG NREL_ROOT_CERT_URL_ROOT=""
RUN set -x && if [ -n "$NREL_ROOT_CERT_URL_ROOT" ]; then curl -fsSLk -o /usr/local/share/ca-certificates/nrel_root.crt "${NREL_ROOT_CERT_URL_ROOT}/nrel_root.pem" && curl -fsSLk -o /usr/local/share/ca-certificates/nrel_xca1.crt "${NREL_ROOT_CERT_URL_ROOT}/nrel_xca1.pem" &&  update-ca-certificates; fi
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

ENV SRC_DIR=/opt/reopt/reo/src
# Use RUN to define and append to LD_LIBRARY_PATH properly
RUN export LD_LIBRARY_PATH="/opt/reopt/reo/src:${LD_LIBRARY_PATH}"
# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    gfortran \
    libgfortran5 \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    wget \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*


# Copy all code
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /opt/reopt

# Install python packages
WORKDIR /opt/reopt

COPY bin/wait-for-it.bash /opt/reopt/bin/
COPY start_system.sh /opt/reopt/start_system.sh
RUN chmod +x /opt/reopt/start_system.sh

COPY requirements.txt /opt/reopt/
RUN ["pip", "install", "-r", "requirements.txt"]

# RUN python manage.py migrate && \
#     python manage.py collectstatic --noinput && \
#     python manage.py createsuperuser --noinput || true

RUN python manage.py createsuperuser --noinput || true

EXPOSE 8000

ENTRYPOINT ["/opt/reopt/start_system.sh"]
# ENTRYPOINT ["/opt/reopt/start_celery_django.sh"]
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
