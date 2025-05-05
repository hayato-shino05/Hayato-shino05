import requests
import os

USERNAME = "Hayato-shino05"
REPOS = [
    "Grok-Fun-Mode",
    "tim-kiem-thanh-le-hom-nay",
    "Happy-Birthday-Website"
]

def get_repo_info(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return {
            "name": data["name"],
            "description": data["description"],
            "stars": data["stargazers_count"],
            "url": data["html_url"]
        }
    return None

def main():
    featured_md = "## 🔥 Featured Projects\n\n"
    for repo in REPOS:
        info = get_repo_info(USERNAME, repo)
        if info:
            featured_md += f"- [{info['name']}]({info['url']})  \n"
            featured_md += f"  ![Stars](https://img.shields.io/github/stars/{USERNAME}/{repo}?style=social)  \n"
            featured_md += f"  {info['description']}\n\n"

    # Đọc README.md hiện tại
    with open("README.md", encoding="utf-8") as f:
        content = f.read()

    # Thay thế phần Featured Projects cũ
    import re
    new_content = re.sub(
        r"## 🔥 Featured Projects[\s\S]*?(?=\n## |\Z)",
        featured_md.strip(),
        content,
        flags=re.MULTILINE
    )

    # Ghi lại README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    main()
