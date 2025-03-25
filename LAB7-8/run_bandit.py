import os
import subprocess
import git

# Increase Git buffer size to prevent failures when cloning large repositories
subprocess.run(["git", "config", "--global", "http.postBuffer", "524288000"])

# List of repositories to analyze
repos = {
    "django": "https://github.com/django/django",
    "celery": "https://github.com/celery/celery",
    "flask": "https://github.com/pallets/flask"  # Replaced Sentry with Flask
}

# Create a directory for storing reports
os.makedirs("bandit_reports", exist_ok=True)

for repo_name, repo_url in repos.items():
    print(f"\nCloning {repo_name}...")
    repo_path = os.path.join(os.getcwd(), repo_name)

    # Clone the repository
    if os.path.exists(repo_path):
        print(f"Repository {repo_name} already exists. Skipping clone...")
    else:
        git.Repo.clone_from(repo_url, repo_path, depth=1)

    # Open the repo using GitPython
    repo = git.Repo(repo_path)
    
    # Get the last 100 non-merge commits
    commits = [commit.hexsha for commit in repo.iter_commits("main", max_count=100, no_merges=True)]

    for commit in commits:
        print(f"Analyzing commit {commit} in {repo_name}...")
        repo.git.checkout(commit)

        # Define output report path
        report_path = f"bandit_reports/bandit_report_{repo_name}_{commit}.txt"
        
        # Run Bandit and save the output
        with open(report_path, "w") as report_file:
            subprocess.run(["bandit", "-r", "."], cwd=repo_path, stdout=report_file, stderr=report_file)

    print(f"Finished analysis for {repo_name}.\n")

    # Cleanup: Switch back to main branch and remove the repo to save space
    repo.git.checkout("main")
    subprocess.run(["rm", "-rf", repo_path])

print("Analysis complete! Reports are saved in the 'bandit_reports' directory.")
