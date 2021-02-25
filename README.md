![alt text](https://github.com/pemtajo/badge-readme/blob/screenshot-readme.png?raw=true)
# badge-readme
Add a badges only from Acclaim (for now), in your Readme.

## Prep Work

1. You need to update the markdown file(.md) with 2 comments. You can refer [here](#update-your-readme) for updating it.

2. You can follow either of the Two Examples according to your needs to get started with.

## Update your Readme

Add a comment to your `README.md` like this:

```md
<!--START_SECTION:badges-->
<!--END_SECTION:badges-->
```

These lines will be our entry-points for the dev metrics.

### Profile Repository

_If you're executing the workflow on your Profile Repository (`<username>/<username>`)_

> You wouldn't need an GitHub Access Token since GitHub Actions already makes one for you.

- Create a new file named `update-badges.yml` with the following contents inside the workflows folder:


```yml
name: Update badges

on:
  schedule:
    # Runs at 0am UTC every day
    - cron: "0 0 * * *"
jobs:
  update-readme:
    name: Update Readme with badges
    runs-on: ubuntu-latest
    steps:
      - name: Badges - Readme
        uses: pemtajo/badge-readme@master
```

3. Add a comment to your `README.md` like this:

```md
<!--START_SECTION:badges-->
<!--END_SECTION:badges-->
```

4. But default, the script will use the same username from github, but will can change it, and some others variables:

| Option | Default Value | Description | Required |
|--------|--------|--------|--------|
|*GH_TOKEN*| - |GitHub access token with Repo scope|No|
|*REPOSITORY*| `<username>/<username> `|Your GitHub repository|No|
|*ACCLAIM_USER*| `<username>` |User name used in Acclaim|No|
|*ACCLAIM_SORT*| `RECENT` |The sort type for return acclaim badges [RECENT/POPULAR] |No|
|*GH_TOKEN*| `Updated README with new badges` |Add a commit message of your choice|No|

 Go to your repo secrets by hitting `Settings => Secrets` tab in your profile repo. You can also enter the url https://github.com/USERNAME/USERNAME/settings/secrets . Please replace the `USERNAME` with your own username.
 
5. Create a new `Secret`.  `Name`: `<VAR>`, `Value`

6. Go to Workflows menu (mentioned in step 1), click `Update badges`, click `Run workflow`.
7. Go to your profile page. you will be able to see it.

### Other Repository (not Profile)

You'll need a GitHub API Token with `repo` scope from [here](https://github.com/settings/tokens) if you're running the action not in your Profile Repository
   - You can use [this](#other-repository-not-profile) example to work it out

_If you're executing the workflow on another repo other than `<username>/<username>`_

You'll need to get a [GitHub Access Token](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) with a `repo` scope and save it in the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here is Sample Workflow File for running it:

```yml
name: Update badges

on:
  schedule:
    # Runs at 2am UTC
    - cron: "0 2 * * *"
jobs:
  update-readme:
    name: Update Readme with badges
    runs-on: ubuntu-latest
    steps:
      - name: Badges - Readme
        uses: pemtajo/badge-readme@master
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          REPOSITORY: <username/username> # optional, By default, it will automatically use the repository who's executing the workflow.
          COMMIT_MESSAGE: "My commit message to update badges" # optional
          ACCLAIM_USER: <username_acclaim> # optional, but default will use the same from github
          ACCLAIM_SORT: RECENT or POPULAR # optional, this is the two forms from acclaim sort, more popular or recent first, by default use RECENT
```

## Tests

### Running Tests

To run tests simply execute the following in the folder `tests`. (need `docker` and `docker-compose` installled):

```bash
docker-compose up
```
