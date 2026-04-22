# 🌐 Website Health Monitor (Discord & WhatsApp Alerts)

[English Version](#english) | [Version Française](#française)

---

<a name="english"></a>
## 🇬🇧 English Version

### 📝 Description
A Python-based automation tool that monitors website availability in real-time. If a server error is detected (e.g., HTTP 500), the script instantly triggers alerts via Discord Webhooks and the Twilio WhatsApp API.

### 🚀 Key Features
- **Continuous Monitoring**: Checks URL status every 60 seconds.
- **Multi-Channel Alerting**: Integrated with Discord and WhatsApp.
- **Security First**: Uses environment variables (`.env`) to protect API credentials.
- **Compliance Aware**: Pivoted to WhatsApp to comply with French ARCEP regulations regarding A2P (Application-to-Person) traffic.

### 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: `requests`, `twilio`, `python-dotenv`
- **APIs**: Discord Webhooks, Twilio WhatsApp Sandbox

---

<a name="française"></a>
## 🇫🇷 Version Française

### 📝 Description
Un outil d'automatisation en Python qui surveille la disponibilité d'un site web en temps réel. Si une erreur serveur est détectée (ex: Code 500), le script déclenche instantanément des alertes via les Webhooks Discord et l'API WhatsApp de Twilio.

### 🚀 Fonctionnalités Clés
- **Surveillance Continue** : Vérification de l'état de l'URL toutes les 60 secondes.
- **Alertes Multi-Canaux** : Intégration directe avec Discord et WhatsApp.
- **Sécurité** : Utilisation de variables d'environnement (`.env`) pour sécuriser les clés API.
- **Respect de la Conformité** : Adaptation vers WhatsApp pour respecter les régulations de l'ARCEP sur le trafic A2P en France.

### 🛠️ Technologies Utilisées
- **Langage** : Python 3.x
- **Bibliothèques** : `requests`, `twilio`, `python-dotenv`
- **APIs** : Discord Webhooks, Twilio WhatsApp Sandbox