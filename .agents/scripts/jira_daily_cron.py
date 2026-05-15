import requests
import datetime
import os
import json
from base64 import b64encode

# --- CONFIGURATION ---
JIRA_URL = "https://jira.sotatek.com"
EMAIL = "nga.tran2@sotatek.com"
# LƯU Ý: Tuyệt đối không hardcode Token ở đây. 
# Hãy set biến môi trường JIRA_API_TOKEN trên máy của bạn.
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "YOUR_TOKEN_HERE")
PROJECT_KEY = "LAMS"
REPORT_DIR = "../../report" # Đường dẫn tương đối từ thư mục script đến thư mục report

def fetch_bugs():
    jql = f'project = {PROJECT_KEY} AND issuetype = Bug AND status = "Ready for test"'
    url = f"{JIRA_URL}/rest/api/2/search"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    params = {
        "jql": jql,
        "maxResults": 50,
        "fields": "summary,status,priority"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("issues", [])
    except Exception as e:
        print(f"Error fetching bugs: {e}")
        return None

def generate_report(bugs):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    filename = f"daily-bug-notification_{date_str}.md"
    filepath = os.path.join(os.path.dirname(__file__), REPORT_DIR, filename)
    
    # Tạo thư mục nếu chưa có
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    content = f"# 🐞 JIRA DAILY BUG NOTIFICATION\n"
    content += f"**Dự án:** {PROJECT_KEY}\n"
    content += f"**Thời gian quét:** {timestamp}\n\n"
    content += f"---\n\n"
    
    if bugs is None:
        content += "❌ **Lỗi:** Không thể kết nối với Jira API. Vui lòng kiểm tra lại Network hoặc API Token.\n"
    elif len(bugs) == 0:
        content += "✅ **Trạng thái:** Không có Bug nào mới ở trạng thái `Ready for test` hoặc `Fixed`.\n"
    else:
        content += f"🚀 Tìm thấy **{len(bugs)}** Bug sẵn sàng để Re-test:\n\n"
        content += "| ID | Tiêu đề | Trạng thái | Ưu tiên | Link |\n"
        content += "| :--- | :--- | :--- | :--- | :--- |\n"
        for bug in bugs:
            key = bug["key"]
            summary = bug["fields"]["summary"]
            status = bug["fields"]["status"]["name"]
            priority = bug["fields"]["priority"]["name"]
            link = f"{JIRA_URL}/browse/{key}"
            content += f"| **{key}** | {summary} | `{status}` | {priority} | [Link]({link}) |\n"
            
    content += f"\n---\n*Report generated automatically by `jira_daily_cron.py`*"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Report saved to: {filepath}")

if __name__ == "__main__":
    print(f"Starting Jira Daily Scan at {datetime.datetime.now()}...")
    bugs_list = fetch_bugs()
    generate_report(bugs_list)
    print("Done.")
