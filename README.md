# Find and delete empty GitHub repositories

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/fanyang89/find-empty-github-repo.git
cd find-empty-github-repo
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Prepare GitHub token

Create the classic token at [Personal access tokens (classic)](https://github.com/settings/tokens)
with the `repo` and `delete_repo` scope.

Then create the `.env` file:

```
echo "GITHUB_TOKEN=your_github_token" > .env
```

### 4. Run the script

```bash
uv run main.py --user-name <your-name>
```

and review the output

### 5. Delete them

```bash
uv run main.py --user-name <your-name> --delete
```
