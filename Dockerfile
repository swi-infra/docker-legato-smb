FROM dperson/samba

RUN apk --no-cache upgrade && \
    apk add --no-cache py-pip \
                       py3-pip \
                       python3-dev

COPY scripts/update_farm_host.py /update_farm_host.py

ENV SAMBA_ARGS=""

ENTRYPOINT [ \
        "/bin/sh", "-c", \
        "python3 /update_farm_host.py && /sbin/tini -- /usr/bin/samba.sh ${SAMBA_ARGS}" \
]
