Aim: To check for further optimisation by removing redundant operation in the file [setup_chrome.sh]

timed the current docker build time 

it comes to 
```@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build -t "hello" .
[+] Building 294.1s (16/16) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 888B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       2.7s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                    0.0s
 => [ 1/10] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd              11.9s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.2s
 => => sha256:3f4e87e951c98244725ea4091ad03f25a74487b5e95c9077d22851f5d03abe88 26.69MB / 26.69MB                                                   4.6s
 => => sha256:10487245a8aa8553a15e03dd034bdf587d83b26bba680a92e085971b9d3229ab 12.34MB / 12.34MB                                                   2.0s
 => => sha256:a6e80813257d3fdcf4f042c5d2d78c823190075e0d513c74bb77a6f7756c4829 249B / 249B                                                         0.6s
 => => sha256:606f83be173854196a130115198021e2aea50af13cf2d67480e5d3fdbe0a47ea 1.29MB / 1.29MB                                                     0.7s
 => => sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a 29.79MB / 29.79MB                                                   5.0s 
 => => extracting sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a                                                          3.2s
 => => extracting sha256:606f83be173854196a130115198021e2aea50af13cf2d67480e5d3fdbe0a47ea                                                          0.2s
 => => extracting sha256:10487245a8aa8553a15e03dd034bdf587d83b26bba680a92e085971b9d3229ab                                                          1.0s
 => => extracting sha256:a6e80813257d3fdcf4f042c5d2d78c823190075e0d513c74bb77a6f7756c4829                                                          0.0s
 => => extracting sha256:3f4e87e951c98244725ea4091ad03f25a74487b5e95c9077d22851f5d03abe88                                                          1.0s
 => [internal] load build context                                                                                                                  0.5s
 => => transferring context: 1.84MB                                                                                                                0.2s
 => [ 2/10] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     && rm -  27.8s
 => [ 3/10] WORKDIR /app                                                                                                                           0.4s
 => [ 4/10] COPY pyproject.toml uv.lock ./                                                                                                         0.1s
 => [ 5/10] RUN uv sync --frozen --no-install-project                                                                                              5.8s
 => [ 6/10] COPY . .                                                                                                                               0.9s
 => [ 7/10] RUN chmod +x setup_chrome.sh                                                                                                           0.6s
 => [ 8/10] RUN ./setup_chrome.sh                                                                                                                138.2s
 => [ 9/10] RUN uv run python test_chromedriver.py                                                                                                 8.7s
 => [10/10] RUN ls -la                                                                                                                             0.5s
 => exporting to image                                                                                                                            96.0s
 => => exporting layers                                                                                                                           62.7s
 => => exporting manifest sha256:d71a8770937096ce4167002f237c7e8322e07c2cb7d1e044ce04689925dd2202                                                  0.0s
 => => exporting config sha256:53064adc8d42d7cc79e4f494892e5d9c55058ac2112f4556b0585781331285aa                                                    0.0s
 => => exporting attestation manifest sha256:b65057d97d9b666f21d4fc1443ed03c945f30dd7000ba5a8e7e7d2ef47577528                                      0.0s
 => => exporting manifest list sha256:b4f39ad2f41343f385f413b132347bdacd3bcd10efc368e5406f3e43e8b7a4d8                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                33.1s

real    4m54.512s
user    0m1.084s
sys     0m0.977s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```

and i am rebuilding it again so that (just to check the rebuilds time)

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build -t "hello" .
[+] Building 164.6s (16/16) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 888B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       4.9s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                    0.0s
 => [ 1/10] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd               0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.0s
 => [internal] load build context                                                                                                                  0.1s
 => => transferring context: 21.14kB                                                                                                               0.1s
 => CACHED [ 2/10] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     &  0.0s
 => CACHED [ 3/10] WORKDIR /app                                                                                                                    0.0s
 => CACHED [ 4/10] COPY pyproject.toml uv.lock ./                                                                                                  0.0s 
 => CACHED [ 5/10] RUN uv sync --frozen --no-install-project                                                                                       0.0s
 => [ 6/10] COPY . .                                                                                                                               0.4s
 => [ 7/10] RUN chmod +x setup_chrome.sh                                                                                                           0.3s
 => [ 8/10] RUN ./setup_chrome.sh                                                                                                                 69.1s
 => [ 9/10] RUN uv run python test_chromedriver.py                                                                                                 7.9s
 => [10/10] RUN ls -la                                                                                                                             0.3s
 => exporting to image                                                                                                                            81.1s
 => => exporting layers                                                                                                                           49.9s
 => => exporting manifest sha256:400a6b0e7b1765c11e2f2ce99c1fe8397e6f6b303fc9d54f4da2d96c3bab6f33                                                  0.0s
 => => exporting config sha256:d86555d4af2ceb54c7daee48b917a4ff75c290eabe2a6dad85d3d9f98c389975                                                    0.0s
 => => exporting attestation manifest sha256:85e3d747c4e76d2cb16382de8e7f8c1b9d8fd1ebcb6279f359f24f1966867212                                      0.0s
 => => exporting manifest list sha256:a6c62f42e55a3d184eec4a95274d29cde2723435837d7bdedc55501a5658bb41                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.1s
 => => unpacking to docker.io/library/hello:latest                                                                                                30.3s

real    2m45.197s
user    0m0.568s
sys     0m0.530s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```

so i want to add a layer because instead of COPY . . and then setup.sh i waana do COPY setup.sh and then run setup.sh and then run COPY . . 

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build -t "hello" .
[+] Building 161.8s (17/17) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 916B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       0.8s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                    0.0s
 => [ 1/11] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd               0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.0s
 => [internal] load build context                                                                                                                  0.1s
 => => transferring context: 26.74kB                                                                                                               0.1s
 => CACHED [ 2/11] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     &  0.0s
 => CACHED [ 3/11] WORKDIR /app                                                                                                                    0.0s
 => CACHED [ 4/11] COPY pyproject.toml uv.lock ./                                                                                                  0.0s
 => CACHED [ 5/11] RUN uv sync --frozen --no-install-project                                                                                       0.0s
 => [ 6/11] COPY setup_chrome.sh /app/                                                                                                             0.0s
 => [ 7/11] RUN chmod +x setup_chrome.sh                                                                                                           0.8s
 => [ 8/11] RUN ./setup_chrome.sh                                                                                                                 68.9s
 => [ 9/11] COPY . .                                                                                                                               0.5s
 => [10/11] RUN uv run python test_chromedriver.py                                                                                                 7.3s
 => [11/11] RUN ls -la                                                                                                                             0.4s
 => exporting to image                                                                                                                            82.6s
 => => exporting layers                                                                                                                           50.7s
 => => exporting manifest sha256:2531cb29982417d28ba9252922dec74c9f0ebf7681df53bc867a2ff3a8ce1730                                                  0.0s
 => => exporting config sha256:7719a77df4fe2574d9930f0e7c64be24536c77e47c531d5668da60651affe684                                                    0.0s
 => => exporting attestation manifest sha256:0617a461b8a6dec2b90d057390b23ce13ccd27d727ed2b900a26e73401e5d293                                      0.1s
 => => exporting manifest list sha256:23cb46b47e341eef2d59552c9f80524716b25137d7b92a90e2d0030c40659f9c                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                31.6s

real    2m42.115s
user    0m0.601s
sys     0m0.466s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```

as we can see we get only 3 sec of speedup it is during COPY . . later is making layers lighter and therey increasing speed

but the rebuilds now happening in 
```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build -t "hello" .
[+] Building 12.4s (17/17) FINISHED                                                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 872B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       0.8s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 116B                                                                                                                  0.0s
 => [ 1/11] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd               0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.0s
 => [internal] load build context                                                                                                                  0.0s
 => => transferring context: 1.34kB                                                                                                                0.0s
 => CACHED [ 2/11] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     &  0.0s
 => CACHED [ 3/11] WORKDIR /app                                                                                                                    0.0s
 => CACHED [ 4/11] COPY pyproject.toml uv.lock ./                                                                                                  0.0s
 => CACHED [ 5/11] RUN uv sync --frozen --no-install-project                                                                                       0.0s
 => CACHED [ 6/11] COPY setup_chrome.sh /app/                                                                                                      0.0s
 => CACHED [ 7/11] RUN chmod +x setup_chrome.sh                                                                                                    0.0s
 => CACHED [ 8/11] RUN ./setup_chrome.sh                                                                                                           0.0s
 => [ 9/11] COPY . .                                                                                                                               0.0s
 => [10/11] RUN uv run python test_chromedriver.py                                                                                                 8.0s
 => [11/11] RUN ls -la                                                                                                                             0.4s
 => exporting to image                                                                                                                             2.9s
 => => exporting layers                                                                                                                            2.4s
 => => exporting manifest sha256:8bcee915e89cc3691bceb9c828be846c39c446bbccb327904ea9166c9f075ad3                                                  0.0s
 => => exporting config sha256:72d8cf7bbc5f437018aa85a205cc15eb465abf1bb0ab19d45644fc1ff830543f                                                    0.0s
 => => exporting attestation manifest sha256:117cc339f43ec5b5648afa915474692214079f6d586de06ba172e4451ff907f5                                      0.0s
 => => exporting manifest list sha256:12c160316c7b455c0c21a2968ecc5b02fc2f2e273fc68bb1237363172ae4e2a6                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                 0.4s

real    0m12.710s
user    0m0.189s
sys     0m0.107s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build -t "hello" .
[+] Building 10.5s (16/16) FINISHED                                                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 872B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       0.3s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                    0.0s
 => [ 1/11] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd               0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.0s
 => [internal] load build context                                                                                                                  0.2s
 => => transferring context: 1.74MB                                                                                                                0.2s
 => CACHED [ 2/11] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     &  0.0s
 => CACHED [ 3/11] WORKDIR /app                                                                                                                    0.0s
 => CACHED [ 4/11] COPY pyproject.toml uv.lock ./                                                                                                  0.0s
 => CACHED [ 5/11] RUN uv sync --frozen --no-install-project                                                                                       0.0s 
 => CACHED [ 6/11] COPY setup_chrome.sh /app/                                                                                                      0.0s
 => CACHED [ 7/11] RUN chmod +x setup_chrome.sh                                                                                                    0.0s
 => CACHED [ 8/11] RUN ./setup_chrome.sh                                                                                                           0.0s
 => [ 9/11] COPY . .                                                                                                                               0.3s
 => [10/11] RUN uv run python test_chromedriver.py                                                                                                 6.1s
 => [11/11] RUN ls -la                                                                                                                             0.4s
 => exporting to image                                                                                                                             3.0s
 => => exporting layers                                                                                                                            2.2s
 => => exporting manifest sha256:29eb280839a1b13bbfc0e555274f4611be3d07ea10f1b3ed1feeba6e0730ad00                                                  0.0s
 => => exporting config sha256:603e160a734d986feff3f7b4d7395757d22ce798cadac8c597de317e64f1860c                                                    0.0s
 => => exporting attestation manifest sha256:335ececa8372b1ec6ce2bedd9bcf5a9e91a05081cd258d5e7f60192e2c52644e                                      0.0s
 => => exporting manifest list sha256:81ffbb7f6afdf99416cd8756ec47a5c9238a25938e763a64f8c4c915c2fa4036                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                 0.6s

real    0m10.823s
user    0m0.161s
sys     0m0.123s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
``` 
this is because new codechanges not triggering the full installation from chromium 

let me also do a cacheless build so as to get another basepoint before further optimisation 
```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build --no-cache -t "hello" .
[+] Building 194.8s (17/17) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 872B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       0.8s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                    0.0s
 => CACHED [ 1/11] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd        0.1s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.1s
 => [internal] load build context                                                                                                                  0.1s
 => => transferring context: 40.60kB                                                                                                               0.1s
 => [ 2/11] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     && rm -  13.8s
 => [ 3/11] WORKDIR /app                                                                                                                           0.1s 
 => [ 4/11] COPY pyproject.toml uv.lock ./                                                                                                         0.0s 
 => [ 5/11] RUN uv sync --frozen --no-install-project                                                                                              3.0s
 => [ 6/11] COPY setup_chrome.sh /app/                                                                                                             0.1s
 => [ 7/11] RUN chmod +x setup_chrome.sh                                                                                                           0.3s
 => [ 8/11] RUN ./setup_chrome.sh                                                                                                                 78.4s
 => [ 9/11] COPY . .                                                                                                                               0.4s
 => [10/11] RUN uv run python test_chromedriver.py                                                                                                 7.6s
 => [11/11] RUN ls -la                                                                                                                             0.3s
 => exporting to image                                                                                                                            88.5s
 => => exporting layers                                                                                                                           55.7s
 => => exporting manifest sha256:8c35b0772d5683c455bb7508bb83fa18ce04748a6f534fe32d16a56fc2e50b34                                                  0.0s
 => => exporting config sha256:ef2a06a69ad60dd9ea1c08032466ec97056f9bb3ab52d978a4eadf9b6a97c8d4                                                    0.0s
 => => exporting attestation manifest sha256:5ebd9af3093729b0b0a8d5a24fa31a3d6ae3d393ee571c9a0142b625fd16478d                                      0.0s
 => => exporting manifest list sha256:816aefe66b054488ee4e9b88cb7aaec5fc45f8ce213a31a6c876ffd493975e3e                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                32.7s

real    3m14.985s
user    0m0.670s
sys     0m0.577s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ 
```
so nocache build also did an update of 4m54 to 3m14 i think 100 sec of speed up 

also got doubt that as we dont have dockerignore file we are including all the blobs the md files etc which are not necessary removing them may increase the speed so tested the docker image using 

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker run -it --entrypoint sh hello
# ls
Dockerfile  README_MIGRATION.md  blob                githubRepo.py   readme_migration2.md  setup_chrome.sh       uv.lock
LICENSE     __init__.py          credly.py           main.py         requirements.txt      test_chromedriver.py
README.md   action.yml           docker-compose.yml  pyproject.toml  settings.py           tests
# ls -la
total 224
drwxr-xr-x 1 root root  4096 Jun 27 18:10 .
drwxr-xr-x 1 root root  4096 Jun 27 18:19 ..
-rw-rw-rw- 1 root root   205 Jun 27 17:46 .env.example
drwxrwxrwx 8 root root  4096 Jun 27 18:10 .git
-rw-rw-rw- 1 root root   110 Jun 27 17:46 .gitignore
drwxr-xr-x 1 root root  4096 Jun 27 17:49 .venv
-rw-rw-rw- 1 root root   877 Jun 27 18:10 Dockerfile
-rw-rw-rw- 1 root root  1079 Jun 27 17:46 LICENSE
-rw-rw-rw- 1 root root 12102 Jun 27 17:46 README.md
-rw-rw-rw- 1 root root 10660 Jun 27 17:46 README_MIGRATION.md
-rw-rw-rw- 1 root root     0 Jun 27 17:46 __init__.py
-rw-rw-rw- 1 root root   976 Jun 27 17:46 action.yml
drwxrwxrwx 2 root root  4096 Jun 27 17:46 blob
-rw-rw-rw- 1 root root 14081 Jun 27 17:46 credly.py
-rw-rw-rw- 1 root root   250 Jun 27 17:46 docker-compose.yml
-rw-rw-rw- 1 root root  1145 Jun 27 17:46 githubRepo.py
-rw-rw-rw- 1 root root   634 Jun 27 17:46 main.py
-rw-rw-rw- 1 root root   372 Jun 27 17:46 pyproject.toml
-rw-rw-rw- 1 root root 10810 Jun 27 18:09 readme_migration2.md
-rw-rw-rw- 1 root root   757 Jun 27 17:46 requirements.txt
-rwxrwxrwx 1 root root   529 Jun 27 17:46 settings.py
-rw-rw-rw- 1 root root  1165 Jun 27 17:46 setup_chrome.sh
-rw-rw-rw- 1 root root  1480 Jun 27 17:46 test_chromedriver.py
drwxrwxrwx 4 root root  4096 Jun 27 17:46 tests
-rw-rw-rw- 1 root root 98278 Jun 27 17:46 uv.lock
```

my doubt is correct adding dockerignore now and doing cache less build

```
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ time docker build --no-cache -t "hello" .
[+] Building 206.2s (17/17) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                               0.0s
 => => transferring dockerfile: 872B                                                                                                               0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:python3.14-trixie-slim                                                                       0.9s
 => [auth] astral-sh/uv:pull token for ghcr.io                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                  0.0s
 => => transferring context: 122B                                                                                                                  0.0s
 => CACHED [ 1/11] FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd        0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.14-trixie-slim@sha256:2b2e474b3a72e84c92b18a2f011a14adcb045fb361f7d8667ed1f8f55eefdafd                 0.0s
 => [internal] load build context                                                                                                                  0.0s
 => => transferring context: 417B                                                                                                                  0.0s
 => [ 2/11] RUN apt-get update && apt-get install -y     wget     curl     unzip     gnupg2     ca-certificates     && apt-get clean     && rm -  11.7s
 => [ 3/11] WORKDIR /app                                                                                                                           0.2s 
 => [ 4/11] COPY pyproject.toml uv.lock ./                                                                                                         0.1s 
 => [ 5/11] RUN uv sync --frozen --no-install-project                                                                                              3.5s
 => [ 6/11] COPY setup_chrome.sh /app/                                                                                                             0.1s
 => [ 7/11] RUN chmod +x setup_chrome.sh                                                                                                           0.3s
 => [ 8/11] RUN ./setup_chrome.sh                                                                                                                 77.8s
 => [ 9/11] COPY . .                                                                                                                               0.3s
 => [10/11] RUN uv run python test_chromedriver.py                                                                                                 8.4s
 => [11/11] RUN ls -la                                                                                                                             0.4s
 => exporting to image                                                                                                                           101.5s
 => => exporting layers                                                                                                                           59.2s
 => => exporting manifest sha256:9b8af0873fe58777fa14e03b91c2af2f2876e7a3341ce4c416b9a4dff8cece3e                                                  0.0s
 => => exporting config sha256:b896a8756671c9386f9ffa568ef9a9e951f5902204ff572706078af3f31feab1                                                    0.0s
 => => exporting attestation manifest sha256:232df1022495e1f01769369d6e08a50228912f409c0b5dd48c7dcfea6cd3dc51                                      0.0s
 => => exporting manifest list sha256:8bbec7d0434663ea34ac5765177c2d177c510ddc4d39b450284ef09c9b912a83                                             0.0s
 => => naming to docker.io/library/hello:latest                                                                                                    0.0s
 => => unpacking to docker.io/library/hello:latest                                                                                                41.9s

real    3m27.124s
user    0m0.678s
sys     0m0.653s
@SigireddyBalasai ➜ /workspaces/badge-readme (main) $ docker run -it --entrypoint sh hello
l# s
Dockerfile   action.yml  docker-compose.yml  main.py         settings.py      test_chromedriver.py
__init__.py  credly.py   githubRepo.py       pyproject.toml  setup_chrome.sh  uv.lock
# ls -la
total 164
drwxr-xr-x 1 root root  4096 Jun 27 18:49 .
drwxr-xr-x 1 root root  4096 Jun 27 19:00 ..
-rw-rw-rw- 1 root root    82 Jun 27 18:49 .dockerignore
drwxr-xr-x 1 root root  4096 Jun 27 18:56 .venv
-rw-rw-rw- 1 root root   833 Jun 27 18:17 Dockerfile
-rw-rw-rw- 1 root root     0 Jun 27 17:46 __init__.py
-rw-rw-rw- 1 root root   976 Jun 27 17:46 action.yml
-rw-rw-rw- 1 root root 14081 Jun 27 17:46 credly.py
-rw-rw-rw- 1 root root   250 Jun 27 17:46 docker-compose.yml
-rw-rw-rw- 1 root root  1145 Jun 27 17:46 githubRepo.py
-rw-rw-rw- 1 root root   634 Jun 27 17:46 main.py
-rw-rw-rw- 1 root root   372 Jun 27 17:46 pyproject.toml
-rwxrwxrwx 1 root root   529 Jun 27 17:46 settings.py
-rw-rw-rw- 1 root root  1165 Jun 27 17:46 setup_chrome.sh
-rw-rw-rw- 1 root root  1480 Jun 27 17:46 test_chromedriver.py
-rw-rw-rw- 1 root root 98278 Jun 27 17:46 uv.lock
# 
```
so completing removal of git directory tests directory and blobs directory so i think the image size reduced but i forgot to note is so now metrics to test now 

commiting and pushing for now will need to do more optimisations later and do another pull request 

Thank You

If you want to contact me you can contact on discord id : balasaisigireddy