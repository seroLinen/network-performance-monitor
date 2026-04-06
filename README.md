# 🏃‍♂️ Chaski-Link NPM
**Advanced Network Performance Monitor & Automated Logging Suite**

Chaski-Link is a lightweight, Python-based Network Performance Monitor (NPM) inspired by the ancient Incan messenger system. It performs automated health checks against global DNS infrastructure and provides real-time desktop telemetry.

---

## 🚀 Features
* **Automated Heartbeats:** Scheduled daily checks via GitHub Actions (17:00 UTC).
* **Layer 4 Monitoring:** Uses TCP Socket connections (Port 53) to bypass ICMP blocks and verify service availability.
* **Local Telemetry:** Integrated Windows Toast notifications for high-latency events (>100ms) or service timeouts.
* **Persistent Logging:** Maintains a historical `network_log.csv` for long-term stability analysis.

## 🛠️ Technical Stack
* **Language:** Python 3.9+
* **Automation:** GitHub Actions (CI/CD)
* **Libraries:** `plyer` (Desktop Notifications), `socket`, `csv`, `time`

## 📦 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/serolinen/chaski-link.git](https://github.com/serolinen/chaski-link.git)
   cd chaski-link
