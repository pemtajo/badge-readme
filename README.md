![alt text](https://github.com/pemtajo/badge-readme/blob/main/blob/screenshot-readme.png?raw=true)
# badge-readme
Add badges only from [Credly](https://www.credly.com/) (for now), in [your Readme](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).

_Attention: the data access is public, but it is the individual responsibility of whoever shares the reported data_

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
    permissions:
      contents: write
    steps:
      - name: Badges - Readme
        uses: pemtajo/badge-readme@main
```

3. Add a comment to your `README.md` like this:

```md
<!--START_SECTION:badges-->
<!--END_SECTION:badges-->
```

4. But default, the script will use the same username from github, but will can change it, and some others variables:

| Option | Default Value | Description | Required |
|--------|--------|--------|--------|
|*GH_TOKEN*| - |GitHub access token with Repo scope|Yes|
|*GH_API_URL*| `https://api.github.com` | GitHub API (can be enterprise API)|No|
|*REPOSITORY*| `<username>/<username> `|Your GitHub repository|No|
|*CREDLY_USER*| `<username>` |User name used in Credly|No|
|*CREDLY_SORT*| `RECENT` |The sort type for return credly badges [RECENT/POPULAR] |No|
|*COMMIT_MESSAGE*| `Updated README with new badges` |Add a commit message of your choice|No|
|*BADGE_SIZE*| `110` |Defines the badge dimension.|No|
|*NUMBER_LAST_BADGES*|`0`|the number of the last badges that need to show - (0 to not set limit) |No

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
        uses: pemtajo/badge-readme@main
        with:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          REPOSITORY: <username>/<username> # optional, By default, it will automatically use the repository who's executing the workflow.
          COMMIT_MESSAGE: "My commit message to update badges" # optional
          CREDLY_USER: <username_credly> # optional, but default will use the same from github
          CREDLY_SORT: RECENT or POPULAR # optional, this is the two forms from credly sort, more popular or recent first, by default use RECENT
          BADGE_SIZE: the resolution to the badges images # optional, 110x110 default
          NUMBER_LAST_BADGES: the maximum last badges to show # optional, will show the 48 in the first page
```

## Tests

### Running Tests

Just run locally

```bash
python3 -m unittest discover -v -s tests
```

Or if prefere using docker, execute the following in the folder `tests`. (need `docker` and `docker-compose` installed):

```bash
docker-compose build && docker-compose up
```


