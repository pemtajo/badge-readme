![alt text](https://github.com/pemtajo/badge-readme/blob/main/blob/screenshot-readme.png?raw=true)
# badge-readme
Add badges only from [Credly](https://www.credly.com/) (for now), in [your Readme](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme).

_Attention: the data access is public, but it is the individual responsibility of whoever shares the reported data_


## Prep Work

  - You need to update the markdown file(.md) with 2 comments. You can refer [here](#update-your-readme) for updating it.
  - You can follow either of the Two Examples according to your needs to get started with.


## Start point

1. Update your Readme profile - if your github user is pemtajo you have to build your url like https://github.com/pemtajo/pemtajo (ex.: `<username>/<username>`)

  Add a comment to your `README.md` like this:

  ```md
  <!--START_SECTION:badges-->
  <!--END_SECTION:badges-->
  ```

  Note:_ These lines will be our entry-points for the dev metrics._


2. Repository Profile

  _Note: If you're executing the workflow on your Profile Repository (`<username>/<username>`) you wouldn't need an GitHub Access Token since GitHub Actions already makes one for you. 
  In other words: if your Credly user is the same as your GitHub user, use the flow bellow, if not, go to step 3._

  - a. Open your repository profile `<username>/<username>`
  - b. Create a new file named `update-badges.yml` containing to following contents inside:

    ```yml
      name: Update badges
      on:
        schedule:
          # Runs at 2am UTC
          - cron: "0 2 * * *"
        workflow_dispatch:
          inputs:
            logLevel:
              description: 'Log level'     
              required: true
              default: 'warning'
            tags:
              description: 'Test scenario tags' 
      jobs:
        update-readme:
          name: Update Readme with badges
          runs-on: ubuntu-latest
          steps:
            - name: Badges - Readme
              uses: pemtajo/badge-readme@main
              with:
                GH_TOKEN: ${{ secrets.GH_TOKEN }}
                BADGE_SIZE: 100
                NUMBER_LAST_BADGES: 24
           ```   


3. Other Repository (not Profile)

  If you are executing the workflow in another  `repo ` other than `<username>/<username>`, you will need:
  A [GitHub Access Token] is required and you can also set it up through this link > (https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token).
  
  - a. GitHub API Token with `repo` scope from [here] - https://github.com/settings/tokens. _(note: if you not running the action in your Profile Repository)_
  - b. Also, you can use [this](#other-repository-not-profile) example to work it out.
  - c. On https://github.com/settings/tokens click on `Generate new Token`
  - d. Save your TOKEN in your the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>` by opening your repository profile [`<username>/<username>`](https://github.com/USERNAME/USERNAME/settings/secrets. Please replace the `USERNAME` with your own username.)
  - e. Go to Settings again > Secrets > Actions > NEW REPOSITORY SECRET > name it as GH_TOKEN and paste your TOKEN CODE in VALUE;   
  - f. Yet in your repository profile `<username>/<username>`, create a new file named `update-badges.yml` containing to following contents inside:
  - g. By default, the script will use the same username from github, but you can change it, and some others variables:

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

Here is Sample Workflow File for running it:

    ```yml
    name: Update badges

    on:
      schedule:
        # Runs at 2am UTC
        - cron: "0 2 * * *"
      workflow_dispatch:
        inputs:
          logLevel:
            description: 'Log level'     
            required: true
            default: 'warning'
        tags:
            description: 'Test scenario tags'
    jobs:
      update-readme:
        name: Update Readme with badges
        runs-on: ubuntu-latest
        steps:
          - name: Badges - Readme
           uses: pemtajo/badge-readme@main
            with:
            GH_TOKEN: ${{ secrets.GH_TOKEN }} *** CHANGES CAN BE MADE ***
              REPOSITORY: <username>/<username> # optional, By default, it will automatically use the repository who's executing the workflow.
              COMMIT_MESSAGE: "My commit message to update badges" # optional
              CREDLY_USER: <username_credly> # optional, but default will use the same from github
              CREDLY_SORT: RECENT or POPULAR # optional, this is the two forms from credly sort, more popular or recent first, by default use RECENT
              BADGE_SIZE: the resolution to the badges images # optional, 110x110 default
              NUMBER_LAST_BADGES: the maximum last badges to show # optional, will show the 48 in the first page


 
6. Go to Workflows menu (mentioned in step 1), click `Update badges`, click `Run workflow`.


7. Go to your profile page. you will be able to see it.


### Running Tests

Just run locally

```bash
python3 -m unittest discover -v -s tests
```

Or if the use of Docker is prefered, execute the following in the folder `tests`. (need `docker` and `docker-compose` installed):

```bash
docker-compose build && docker-compose up
```
 

 
## ADDITIONAL INFORMATION:

1. This script allows you run the workflow manually so you don't need to wait until the settled time to run it.


```yml
workflow_dispatch:
  inputs:
    logLevel:
      description: 'Log level'     
      required: true
      default: 'warning'
    tags:
      description: 'Test scenario tags' 
```   
