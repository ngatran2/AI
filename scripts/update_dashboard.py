import os
import re
import datetime

# --- CONFIGURATION ---
BASE_DIR = r"d:\AI\Newtemplate"
DASHBOARD_DIR = os.path.join(BASE_DIR, "report")
REQUIREMENTS_DIR = os.path.join(BASE_DIR, "requirements")
SCENARIOS_DIR = os.path.join(BASE_DIR, "scenarios")
TESTCASES_DIR = os.path.join(BASE_DIR, "testcases")
EXECUTION_DIR = os.path.join(BASE_DIR, "execution")

UC_PATTERN = re.compile(r"UC-[A-Z0-9-]+")
VERSION_PATTERN = re.compile(r"_v(\d+)")

def get_feature_name(uc_id):
    path = os.path.join(REQUIREMENTS_DIR, uc_id)
    if not os.path.exists(path): return uc_id
    files = sorted([f for f in os.listdir(path) if "_audited" in f])
    if not files: return uc_id
    try:
        with open(os.path.join(path, files[-1]), "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"# (.*)", content)
            if match:
                name = match.group(1).split(":")[-1].strip()
                return name if len(name) < 50 else name[:47] + "..."
    except: pass
    return uc_id

def get_latest_version(directory, uc_id, suffix):
    if not os.path.exists(directory): return None
    uc_path = os.path.join(directory, uc_id)
    target_dir = uc_path if os.path.exists(uc_path) else directory
    files = [f for f in os.listdir(target_dir) if uc_id in f and suffix in f]
    if not files: return None
    latest_v = -1
    for f in files:
        match = VERSION_PATTERN.search(f)
        if match:
            v = int(match.group(1))
            if v > latest_v: latest_v = v
    return f"✅ v{latest_v}" if latest_v != -1 else "✅ Done"

def get_testcase_status(uc_id):
    path = os.path.join(TESTCASES_DIR, uc_id)
    if not os.path.exists(path): return "⏳ Pending"
    files = os.listdir(path)
    hl = any("-hl" in f for f in files)
    det = any("-det" in f for f in files)
    if hl and det: return "✅ HL/DET"
    if hl: return "✅ HL"
    if det: return "✅ DET"
    return "⏳ Pending"

def get_exec_status(uc_id):
    report_path = os.path.join(EXECUTION_DIR, uc_id, "reports")
    if not os.path.exists(report_path): return "⏳ Pending"
    files = sorted([f for f in os.listdir(report_path) if "res_" in f])
    if not files: return "⏳ Pending"
    latest = files[-1]
    if "PASS" in latest.upper(): return "✅ PASS"
    return "✅ Executed"

def update_dashboard():
    ucs = []
    if os.path.exists(REQUIREMENTS_DIR):
        ucs = [d for d in os.listdir(REQUIREMENTS_DIR) if os.path.isdir(os.path.join(REQUIREMENTS_DIR, d)) and UC_PATTERN.match(d)]
    
    rows = []
    completed_count = 0
    for uc in sorted(ucs):
        feature_name = get_feature_name(uc)
        audit = get_latest_version(REQUIREMENTS_DIR, uc, "_audited") or "⏳ Pending"
        scenario = get_latest_version(SCENARIOS_DIR, uc, "_scenarios") or "⏳ Pending"
        testcase = get_testcase_status(uc)
        exec_status = get_exec_status(uc)
        
        status = "✅ Completed" if exec_status.startswith("✅") else "🔄 In Progress"
        if audit == "⏳ Pending": status = "⏳ Pending"
        elif exec_status == "⏳ Pending" and testcase != "⏳ Pending": status = "🔄 Ready to Test"
        
        if status == "✅ Completed": completed_count += 1
        rows.append(f"| **{uc}** | {feature_name} | {status} | {audit} | {scenario} | {testcase} | {exec_status} | ⏳ Pending |")

    dashboards = sorted([f for f in os.listdir(DASHBOARD_DIR) if "PROJECT_MASTER_DASHBOARD" in f])
    latest_dash = os.path.join(DASHBOARD_DIR, dashboards[-1])
    with open(latest_dash, "r", encoding="utf-8") as f:
        content = f.read()

    # Update Progress
    total_ucs = len(ucs) if ucs else 1
    progress_pct = int((completed_count / total_ucs) * 100)
    filled = progress_pct // 10
    progress_bar = "[" + "█" * filled + "░" * (10 - filled) + "]"
    content = re.sub(r"Overall Progress:\*\* \[.*?\] \d+%", f"Overall Progress:** {progress_bar} {progress_pct}%", content)

    matrix_header = "| UC-ID | Feature Name | Status | Audit | Scenario | Test Case | Functional Exec | Performance |"
    matrix_sep = "| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |"
    pattern = re.compile(re.escape(matrix_header) + r"\n" + re.escape(matrix_sep) + r".*?\n\n", re.DOTALL)
    new_matrix = matrix_header + "\n" + matrix_sep + "\n" + "\n".join(rows) + "\n\n"
    updated_content = pattern.sub(new_matrix, content)
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    updated_content = re.sub(r"\*\*Ngày cập nhật:\*\* \d{4}-\d{2}-\d{2}", f"**Ngày cập nhật:** {today}", updated_content)
    match = re.search(r"\*\*Phiên bản:\*\* v(\d+)", updated_content)
    if match:
        v = int(match.group(1)) + 1
        updated_content = re.sub(r"\*\*Phiên bản:\*\* v\d+", f"**Phiên bản:** v{v}", updated_content)
        new_v = v
    else: new_v = 1

    new_filename = f"PROJECT_MASTER_DASHBOARD_{today.replace('-', '')}_v{new_v}.md"
    new_path = os.path.join(DASHBOARD_DIR, new_filename)
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"Dashboard updated: {new_path}")
    return new_path

if __name__ == "__main__":
    update_dashboard()
