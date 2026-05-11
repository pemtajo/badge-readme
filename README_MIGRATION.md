Tinking why don't we migrated to uv first we need to convert to uv with creating uv.lock and pyproject.toml files 


did 

```
uv init 
```

now i need to install all the packages in the codespace did 

```
uv add -r requirements.txt
```

and now we need to check how to replace the docker images 

we are currently using 

the image python:3.14.2-slim-trixie and the similar image uv can offer is ghcr.io/astral-sh/uv:python3.14-trixie-slim so we are checking sbom of both the images to check if direct replacement is possible just to make sure not to add a manual copy from the ghcr repo of docker 


adding docker sbom using command 

```
curl -sSfL https://raw.githubusercontent.com/docker/sbom-cli-plugin/main/install.sh | sh -s --
```

did 
```
docker sbom ghcr.io/astral-sh/uv:python3.14-trixie-slim > uv-image
```

also did 
```
docker sbom python:3.14.2-slim-trixie > python-image
```

did diff and found 

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ diff -qs <(sort uv-image) <(sort python-image)
Files /dev/fd/63 and /dev/fd/62 are identical
```
i dont know how it is possible but i cecked raw also and found that uv as an excequtable will not be found by sbom so i am checking that layers of the 

```
ghcr.io/astral-sh/uv:python3.14-trixie-slim
```

borh images checked the docker image layers with 

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker image history ghcr.io/astral-sh/uv:python3.14-trixie-slim
IMAGE          CREATED      CREATED BY                                      SIZE      COMMENT
8fa3e5682aef   3 days ago   CMD ["/usr/local/bin/uv"]                       0B        buildkit.dockerfile.v0
<missing>      3 days ago   ENTRYPOINT []                                   0B        buildkit.dockerfile.v0
<missing>      3 days ago   ENV UV_TOOL_BIN_DIR=/usr/local/bin              0B        buildkit.dockerfile.v0
<missing>      3 days ago   COPY /uv /uvx /usr/local/bin/ # buildkit        53.2MB    buildkit.dockerfile.v0
<missing>      5 days ago   CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;  for src in idle3 p…   0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;   savedAptMark="$(a…   36.5MB    buildkit.dockerfile.v0
<missing>      5 days ago   ENV PYTHON_SHA256=ce543ab854bc256b61b71e9b27…   0B        buildkit.dockerfile.v0
<missing>      5 days ago   ENV PYTHON_VERSION=3.14.2                       0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;  apt-get update;  a…   3.79MB    buildkit.dockerfile.v0
<missing>      5 days ago   ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      7 days ago   # debian.sh --arch 'amd64' out/ 'trixie' '@1…   78.6MB    debuerreotype 0.17
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker image history python:3.14.2-slim-trixie
IMAGE          CREATED      CREATED BY                                      SIZE      COMMENT
4d1be9816453   5 days ago   CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;  for src in idle3 p…   0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;   savedAptMark="$(a…   36.5MB    buildkit.dockerfile.v0
<missing>      5 days ago   ENV PYTHON_SHA256=ce543ab854bc256b61b71e9b27…   0B        buildkit.dockerfile.v0
<missing>      5 days ago   ENV PYTHON_VERSION=3.14.2                       0B        buildkit.dockerfile.v0
<missing>      5 days ago   RUN /bin/sh -c set -eux;  apt-get update;  a…   3.79MB    buildkit.dockerfile.v0
<missing>      5 days ago   ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      7 days ago   # debian.sh --arch 'amd64' out/ 'trixie' '@1…   78.6MB    debuerreotype 0.17
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```


checked the hashes of the layers to double sure of the common base image 

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker inspect ghcr.io/astral-sh/uv:python3.14-trixie-slim
[
    {
        "Id": "sha256:8fa3e5682aeffed4e5f0528d0ef0e7e189299c6f8812a218006482d1373b6f69",
        "RepoTags": [
            "ghcr.io/astral-sh/uv:python3.14-trixie-slim"
        ],
        "RepoDigests": [
            "ghcr.io/astral-sh/uv@sha256:db47f5ddd6353c9bee566eba8b8b902a8c664bc4cb53a05d22709ac4abb1e668"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-15T20:28:49.394399645Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 172121377,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e70be3b05c44b567fc4601c0f61f9c6dc94400b1cd8013e3672c357fcbd23c7d/diff:/var/lib/docker/overlay2/b2f37b939393637d5a458f3cf53ab33549e723d55ea75e0c7b6ad57c9e3103f3/diff:/var/lib/docker/overlay2/9c8b161973a0b1762368afa8fdf4acfe654401475140774e2f11c69a9f6c16df/diff:/var/lib/docker/overlay2/1acd382504b54af5acb0c5fcd7c0d56938ac36356b3fe7976808bbb1fd3aa2b2/diff",
                "MergedDir": "/var/lib/docker/overlay2/61b590b897f44ca37f30965a6f3dfecdeef1265556c9f072e549461537c912e0/merged",
                "UpperDir": "/var/lib/docker/overlay2/61b590b897f44ca37f30965a6f3dfecdeef1265556c9f072e549461537c912e0/diff",
                "WorkDir": "/var/lib/docker/overlay2/61b590b897f44ca37f30965a6f3dfecdeef1265556c9f072e549461537c912e0/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e50a58335e1366e2581fe61794c1651afe2fe04e881e795aa166f24f4fc78d92",
                "sha256:2549f43c1133f94d64e98af14733f1d84112cc49bc7b1290906063312f730c16",
                "sha256:9e3d10d225711c5cdda5acb47deb30f535592f45b48b8835cfe13d7aa409845b",
                "sha256:f54de68722a85d978d19e803fd61f017be19c1fd282308d170f25d25f06cb849",
                "sha256:73949b59d6bb39ed496146fb9ade65fefabf4f8d3a364d7746aa66134125fa4d"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        },
        "Config": {
            "ArgsEscaped": true,
            "Cmd": [
                "/usr/local/bin/uv"
            ],
            "Entrypoint": null,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "PYTHON_VERSION=3.14.2",
                "PYTHON_SHA256=ce543ab854bc256b61b71e9b27f831ffd1bfd60a479d639f8be7f9757cf573e9",
                "UV_TOOL_BIN_DIR=/usr/local/bin"
            ],
            "Labels": {
                "org.opencontainers.image.created": "2026-01-15T20:28:29.954Z",
                "org.opencontainers.image.description": "An extremely fast Python package and project manager, written in Rust.",
                "org.opencontainers.image.licenses": "Apache-2.0",
                "org.opencontainers.image.revision": "ee4f0036283a350681a618176484df6bcde27507",
                "org.opencontainers.image.source": "https://github.com/astral-sh/uv",
                "org.opencontainers.image.title": "uv",
                "org.opencontainers.image.url": "https://github.com/astral-sh/uv",
                "org.opencontainers.image.version": "0.9.26-python3.14-trixie-slim"
            },
            "OnBuild": null,
            "User": "",
            "Volumes": null,
            "WorkingDir": ""
        }
    }
]
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker inspect python:3.14.2-slim-trixie
[
    {
        "Id": "sha256:4d1be9816453b0d88b81443163658ee1886320257b05b412d30135888c278555",
        "RepoTags": [
            "python:3.14.2-slim-trixie"
        ],
        "RepoDigests": [
            "python@sha256:9b81fe9acff79e61affb44aaf3b6ff234392e8ca477cb86c9f7fd11732ce9b6a"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-13T03:09:45.195848938Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 118919273,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/b2f37b939393637d5a458f3cf53ab33549e723d55ea75e0c7b6ad57c9e3103f3/diff:/var/lib/docker/overlay2/9c8b161973a0b1762368afa8fdf4acfe654401475140774e2f11c69a9f6c16df/diff:/var/lib/docker/overlay2/1acd382504b54af5acb0c5fcd7c0d56938ac36356b3fe7976808bbb1fd3aa2b2/diff",
                "MergedDir": "/var/lib/docker/overlay2/e70be3b05c44b567fc4601c0f61f9c6dc94400b1cd8013e3672c357fcbd23c7d/merged",
                "UpperDir": "/var/lib/docker/overlay2/e70be3b05c44b567fc4601c0f61f9c6dc94400b1cd8013e3672c357fcbd23c7d/diff",
                "WorkDir": "/var/lib/docker/overlay2/e70be3b05c44b567fc4601c0f61f9c6dc94400b1cd8013e3672c357fcbd23c7d/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e50a58335e1366e2581fe61794c1651afe2fe04e881e795aa166f24f4fc78d92",
                "sha256:2549f43c1133f94d64e98af14733f1d84112cc49bc7b1290906063312f730c16",
                "sha256:9e3d10d225711c5cdda5acb47deb30f535592f45b48b8835cfe13d7aa409845b",
                "sha256:f54de68722a85d978d19e803fd61f017be19c1fd282308d170f25d25f06cb849"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        },
        "Config": {
            "Cmd": [
                "python3"
            ],
            "Entrypoint": null,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "PYTHON_VERSION=3.14.2",
                "PYTHON_SHA256=ce543ab854bc256b61b71e9b27f831ffd1bfd60a479d639f8be7f9757cf573e9"
            ],
            "Labels": null,
            "OnBuild": null,
            "User": "",
            "Volumes": null,
            "WorkingDir": ""
        }
    }
]
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```

now do the build and it is done 

now we need to test the docker before and after 

did a git stash and docker compose build to build the previous code got over 1.18 gb of image will pop and test

this is also 1.18 gb 

the docker build on new image time is 
```
real    1m20.370s
user    0m0.296s
sys     0m0.325s
```
the build time for the old one is 
```
real    1m40.093s
user    0m0.354s
sys     0m0.363s
```