# W4_Task:4- 
# Project:4. Log Analysis System (Starter Code)
'''
def analyze_log(file_path):
    ip_count = {}
    url_count = {}
    code_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) < 9:
                    continue  # skip malformed lines
                ip = parts[0]
                url = parts[6]
                code = parts[8]

                ip_count[ip] = ip_count.get(ip, 0) + 1
                url_count[url] = url_count.get(url, 0) + 1
                code_count[code] = code_count.get(code, 0) + 1

        print("Top IPs:", sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5])
        print("Top URLs:", sorted(url_count.items(), key=lambda x: x[1], reverse=True)[:5])
        print("Response Codes:", code_count)

    except FileNotFoundError:
        print("Log file not found.")
'''
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

def analyze_log(file_path):
    ip_count = {}
    url_count = {}
    code_count = {}

    try:
        if os.path.getsize(file_path) > 100 * 1024 * 1024:
            messagebox.showerror("File Too Large", "File size exceeds 100MB.")
            return None

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_num, line in enumerate(file, 1):
                parts = line.split()
                if len(parts) < 9:
                    continue
                ip = parts[0]
                url = parts[6]
                code = parts[8]

                ip_count[ip] = ip_count.get(ip, 0) + 1
                url_count[url] = url_count.get(url, 0) + 1
                code_count[code] = code_count.get(code, 0) + 1

        return ip_count, url_count, code_count

    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The selected log file was not found.")
        return None


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt")])
    if file_path:
        result_text.delete(1.0, tk.END)
        analysis = analyze_log(file_path)

        if analysis:
            ip_count, url_count, code_count = analysis

            result_text.insert(tk.END, "🔝 Top 5 IP Addresses:\n")
            for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]:
                result_text.insert(tk.END, f"{ip}: {count} times\n")

            result_text.insert(tk.END, "\n🔝 Top 5 URLs:\n")
            for url, count in sorted(url_count.items(), key=lambda x: x[1], reverse=True)[:5]:
                result_text.insert(tk.END, f"{url}: {count} times\n")

            result_text.insert(tk.END, "\n📟 Response Codes:\n")
            for code, count in code_count.items():
                result_text.insert(tk.END, f"{code}: {count} times\n")


# ---------------- Tkinter UI Setup ----------------
root = tk.Tk()
root.title("Log Analysis System")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="📊 Log File Analyzer", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

desc = tk.Label(root, text="Upload a server log file (max 100MB) to analyze IPs, URLs, and response codes.", bg="#f0f0f0", font=("Arial", 11))
desc.pack()

browse_btn = tk.Button(root, text="📂 Browse Log File", command=browse_file, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
browse_btn.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=80, height=25, font=("Courier", 10))
result_text.pack(padx=10, pady=10)

root.mainloop()
