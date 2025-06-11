import os, json, requests, subprocess

# —— 配置 ——  
GQL_URL = "https://api.github.com/graphql"
USERNAME = "BiorelaxA"
OUTPUT_JSON = "stats.json"   # 会推到 gh-pages/main 分支根目录
# ——————

token = "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"
headers = {"Authorization": f"bearer {token}"}
query = """
query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
    }
  }
}
"""
resp = requests.post(GQL_URL, json={"query": query, "variables": {"login": USERNAME}}, headers=headers)
data = resp.json()["data"]["user"]["contributionsCollection"]

# 写入 JSON
with open(OUTPUT_JSON, "w") as f:
    json.dump({
        "commits": data["totalCommitContributions"],
        "prs":    data["totalPullRequestContributions"]
    }, f, indent=2)

# 提交并推送到你 GitHub Pages 用的分支
subprocess.run(["git", "add", OUTPUT_JSON], check=True)
subprocess.run(["git", "commit", "-m", "chore: 更新 GitHub 贡献统计"], check=True)
subprocess.run(["git", "push"], check=True)