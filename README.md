# feature-flag-audit
Extract LaunchDarkly feature flags to understand what to clean up

# Dependencies
- Python 3.9

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

Set the project and envronment values to the keys that are configured in LaunchDarkly.

## audit.py
Extracts the following data for each feature flag configured in LaunchDarkly
- Key
- On
- Last modified (days)
- Last evaluated (days)
- Created
- Updated
- Owner 
- Description
- Tags

The owner is taken from the first part of the email address, everything before @domain. Last modified days is calcuated from today. If a feature flag has never been evaluated, then the Last evaluated value will be blank and 0 means it was evaluated today.

# Run
Generates a .CSV file listing the feature flags configured in LaunchDarkly, for the project and environment defined in ff_config.yaml
```python
py audit.py
```