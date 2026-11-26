# TM Forum Open API – Virtual Service (VS)

This is a **Reference Implementation (RI)** for simulating a TM Forum Open API and understanding the API.

It is based on the OpenAPI specification and can be used to **mock the behavior** of the API when a real implementation is not yet available.

This is ideal for:
- Testing client applications early in development
- Frontend/backend decoupling
- Contract-based integration validation
- Viewing a sunny-day result

---

## Prerequisites

- **Docker Desktop** is installed and running.
- On **Windows 11**, ensure:
  - Virtualization is enabled in BIOS
  - WSL 2 is installed and set as default

Make sure the folder includes:
- `docker-compose.yaml`
- `run.sh` or `run.bat` (launcher scripts)

---

## Start the Virtual Service

### Linux/macOS:
```bash
chmod +x run.sh
./run.sh
```

### Windows:
```cmd
run.bat
```

Once started, the service will simulate the API and respond to incoming requests.

---

## Proxy Configuration

If your environment requires outbound traffic to go through a corporate or network proxy, the RI Docker image can be configured by adding values to the `.env` file supplied with the RI.
Note: `.env` is a hidden file and is usually edited from the command line.

- for example:
```env
HTTP_PROXY=http://proxy-host:3128
HTTPS_PROXY=http://proxy-host:3128
```

Hosts that should bypass the proxy are specified by setting the `NO_PROXY` variable. These typically include localhost, loopback addresses, and services running on the same Docker network.
- for example
```env
NO_PROXY="localhost,127.0.0.1,tmf,tmf620-ri"
```

If these environment variables are not set, the default values will be used.

## Other Docker Networks

If your implementation is running on a different network and does not expose a reachable URL (host IP, DNS name, or published port), then the RI will need to join the same network.
This can be done by adjusting the `docker-compose.yaml` file supplied.
- for example
```yaml
networks:
  tmf:
    external: true
  ri_net:
    external: true

services:
  ri:
    ...
    networks:
      - tmf
      - ri_net
```

---

### View and test the API

You can browse the API documentation and test available endpoints. 

Open: `http://localhost:8[api-number]/docs`


You can now make HTTP requests to this address using:
- Postman
- curl
- Any API client or application under development

The RI will generate **mock responses** based on the API contract and conformance profile, ensuring that the behavior is predictable and spec-compliant.

---


## Questions?

Contact: [openapi@tmforum.org](mailto:openapi@tmforum.org)
