FROM python:3.13.14-slim-trixie

WORKDIR /

#downloading uv
# RUN pip install uv #also works but slow compared to the binary installation.
#installing uv by copying the binary from the official distroless docker image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

#installing the requirements
RUN uv sync --frozen

#copying the rest of the application files
COPY . .

#providing the default command
CMD ["uv","run","python","-m","main"]