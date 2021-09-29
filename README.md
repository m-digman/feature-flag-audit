# feature-flag-audit
Audit LaunchDarkly feature flags to understand what to clean up

# Dependencies
- Python 3.9
- See requirements.txt (use: pip install -r requirements.txt)

# Configuration Setup
The LaunchDarkly authentication and project settings are stored in ff_config.yaml

To stop any changes to this file getting back into Git use:
```
# use --no-skip-worktree to undo
git update-index --skip-worktree ff_config.yaml
```
## LaunchDarkly authentication
Create a personal API access token against your LaunchDarkly account and store it somewhere safe:
https://docs.launchdarkly.com/home/account-security/api-access-tokens

Edit ff_config.yaml and set the token. Example:
```yaml
- launchdarkly:
    token: api-my-token
    project: my-project
    environment: my-environment
```