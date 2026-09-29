import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, filedialog
import threading, socket, subprocess, platform, ipaddress, csv
import concurrent.futures
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ACCENT = "#4da3ff"
BG_DARK = "#1a1a1d"
SURFACE = "#242428"
SURFACE2 = "#2e2e33"
FG = "#e6e6e6"
FG_DIM = "#9a9aa0"
OK = "#7ee787"
WARN = "#ffa657"


class NetScanner(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NetScan — Sector 7G")
        self.geometry("1080x720")
        self.minsize(900, 600)
        self.results = []
        self.build_ui()

    def build_ui(self):
        # ---- header ----
        header = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(header, text="NETSCAN",
                     font=("Segoe UI", 18, "bold"),
                     text_color=ACCENT).pack(side="left", padx=16, pady=10)
        ctk.CTkLabel(header, text="network discovery + port scan",
                     font=("Consolas", 11),
                     text_color=FG_DIM).pack(side="left", pady=10)
        ctk.CTkButton(header, text="Toggle Theme", width=110,
                      command=self.toggle_theme).pack(side="right", padx=12, pady=8)

        # ---- target bar ----
        top = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=8)
        top.pack(fill="x", padx=12, pady=(10, 6))

        ctk.CTkLabel(top, text="Subnet:", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=0, padx=(12, 6), pady=12, sticky="w")
        self.subnet = ctk.CTkEntry(top, width=200, height=32,
                                   fg_color=SURFACE2, border_color=SURFACE2)
        self.subnet.insert(0, self.default_subnet())
        self.subnet.grid(row=0, column=1, padx=4, pady=12)

        ctk.CTkLabel(top, text="Ports:", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=2, padx=(20, 6), sticky="w")
        self.ports = ctk.CTkEntry(top, height=32, fg_color=SURFACE2, border_color=SURFACE2)
        self.ports.insert(0, "21,22,23,25,53,80,110,135,139,143,443,445,1433,3306,3389,5432,8080,8443")
        self.ports.grid(row=0, column=3, padx=4, pady=12, sticky="ew")

        ctk.CTkLabel(top, text="Timeout:", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=4, padx=(20, 6), sticky="w")
        self.timeout = ctk.CTkEntry(top, width=60, height=32,
                                    fg_color=SURFACE2, border_color=SURFACE2)
        self.timeout.insert(0, "0.5")
        self.timeout.grid(row=0, column=5, padx=(4, 12), pady=12)
        top.grid_columnconfigure(3, weight=1)

        # ---- action bar ----
        btns = ctk.CTkFrame(self, fg_color="transparent")
        btns.pack(fill="x", padx=12, pady=4)
        self.scan_btn = ctk.CTkButton(btns, text="Start Scan", width=130, height=36,
                                      fg_color=ACCENT, text_color="#000",
                                      hover_color="#7bbaff",
                                      font=("Segoe UI", 12, "bold"),
                                      command=self.start_scan)
        self.scan_btn.pack(side="left", padx=(0, 6))
        ctk.CTkButton(btns, text="Clear", width=90, height=36,
                      fg_color=SURFACE2, hover_color=SURFACE,
                      command=self.clear).pack(side="left", padx=6)
        ctk.CTkButton(btns, text="Export CSV", width=110, height=36,
                      fg_color=SURFACE2, hover_color=SURFACE,
                      command=self.export_csv).pack(side="left", padx=6)

        self.status = ctk.CTkLabel(btns, text="Ready.",
                                   font=("Consolas", 11), text_color=FG_DIM)
        self.status.pack(side="right", padx=8)

        # ---- progress ----
        self.progress = ctk.CTkProgressBar(self, height=6, corner_radius=0,
                                           progress_color=ACCENT)
        self.progress.pack(fill="x", padx=12, pady=(6, 2))
        self.progress.set(0)

        # ---- results table ----
        table_frame = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=8)
        table_frame.pack(fill="both", expand=True, padx=12, pady=8)

        cols = ("ip", "hostname", "ports")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=10)
        for c, w in zip(cols, (160, 260, 580)):
            self.tree.heading(c, text=c.upper())
            self.tree.column(c, width=w, anchor="w")
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=6, pady=6)
        vsb.pack(side="right", fill="y", pady=6, padx=(0, 6))

        # ---- log ----
        log_frame = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=8)
        log_frame.pack(fill="x", padx=12, pady=(0, 12))
        ctk.CTkLabel(log_frame, text="LOG", font=("Segoe UI", 10, "bold"),
                     text_color=ACCENT).pack(anchor="w", padx=10, pady=(8, 0))
        self.log = ctk.CTkTextbox(log_frame, height=140,
                                  font=("Consolas", 11),
                                  fg_color=SURFACE2, border_width=0)
        self.log.pack(fill="x", padx=10, pady=(4, 10))
        self.log.configure(state="disabled")

        self.apply_tree_theme()

    def apply_tree_theme(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Treeview",
                        background=SURFACE, fieldbackground=SURFACE,
                        foreground=FG, rowheight=28,
                        borderwidth=0, relief="flat",
                        font=("Consolas", 10))
        style.configure("Treeview.Heading",
                        background=SURFACE2, foreground=ACCENT,
                        relief="flat", borderwidth=0,
                        font=("Segoe UI", 10, "bold"))
        style.map("Treeview",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", "#000")])
        style.map("Treeview.Heading",
                  background=[("active", SURFACE2)])

    def toggle_theme(self):
        cur = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Light" if cur == "Dark" else "Dark")

    def default_subnet(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return str(ipaddress.ip_network(ip + "/24", strict=False))
        except Exception:
            return "192.168.1.0/24"

    def logline(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        self.log.configure(state="normal")
        self.log.insert("end", f"[{ts}] {msg}\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def set_status(self, text, color=FG_DIM):
        self.status.configure(text=text, text_color=color)

    def clear(self):
        self.tree.delete(*self.tree.get_children())
        self.results.clear()
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        self.progress.set(0)
        self.set_status("Cleared.")

    def start_scan(self):
        self.scan_btn.configure(state="disabled")
        self.progress.configure(mode="indeterminate")
        self.progress.start()
        self.set_status("Scanning...", WARN)
        threading.Thread(target=self.scan, daemon=True).start()

    def scan(self):
        try:
            subnet = self.subnet.get().strip()
            ports = [int(p.strip()) for p in self.ports.get().split(",") if p.strip()]
            timeout = float(self.timeout.get())
            self.logline(f"Scanning {subnet} on {len(ports)} ports, timeout={timeout}s")
            hosts = self.ping_sweep(subnet)
            self.logline(f"Found {len(hosts)} live hosts")
            for ip in hosts:
                hn = self.resolve(ip)
                op = self.scan_ports(ip, ports, timeout)
                self.results.append((ip, hn, op))
                self.tree.insert("", "end", values=(
                    ip, hn or "-",
                    ", ".join(map(str, op)) if op else "-"))
                self.logline(f"{ip} | {hn or '-'} | {len(op)} open")
        except Exception as e:
            self.logline(f"ERROR: {e}")
            self.set_status("Error.", WARN)
        finally:
            self.after(0, self.progress.stop)
            self.after(0, lambda: self.progress.configure(mode="determinate"))
            self.after(0, lambda: self.progress.set(1))
            self.after(0, lambda: self.scan_btn.configure(state="normal"))
            self.after(0, lambda: self.set_status("Done.", OK))
            self.logline("Scan complete.")

    def ping_sweep(self, subnet):
        net = ipaddress.ip_network(subnet, strict=False)
        ips = [str(ip) for ip in net.hosts()]
        win = platform.system().lower() == "windows"
        param = "-n" if win else "-c"
        wait = "-w" if win else "-W"

        def ping(ip):
            try:
                r = subprocess.run(["ping", param, "1", wait, "500", ip],
                                   capture_output=True, timeout=2)
                return ip if r.returncode == 0 else None
            except Exception:
                return None

        live = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=64) as ex:
            for res in ex.map(ping, ips):
                if res:
                    live.append(res)
        return live

    def scan_ports(self, ip, ports, timeout):
        opened = []

        def check(p):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)
                if s.connect_ex((ip, p)) == 0:
                    opened.append(p)
                s.close()
            except Exception:
                pass

        with concurrent.futures.ThreadPoolExecutor(max_workers=64) as ex:
            list(ex.map(check, ports))
        return sorted(opened)

    def resolve(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except Exception:
            return ""

    def export_csv(self):
        if not self.results:
            self.set_status("Nothing to export.", WARN)
            return
        fname = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile=f"netscan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        if not fname:
            return
        with open(fname, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ip", "hostname", "open_ports"])
            for ip, hn, op in self.results:
                w.writerow([ip, hn, ";".join(map(str, op))])
        self.logline(f"Exported {fname}")
        self.set_status("Exported.", OK)


if __name__ == "__main__":
    NetScanner().mainloop()