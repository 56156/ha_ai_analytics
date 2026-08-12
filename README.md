# 🤖 Home Assistant AI 交互分析中心 (HA AI Analytics)

[![GitHub Release](https://img.shields.io/github/v/release/56156/ha_ai_analytics)](https://github.com/56156/ha_ai_analytics/releases)
[![HA Version](https://img.shields.io/badge/Home%20Assistant-2024.6%2B-blue)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/56156/ha_ai_analytics)](LICENSE)

**English** | [**中文**](#中文版)

---

## 🇬🇧 English

### Overview
**HA AI Analytics** is a fully-featured custom integration for Home Assistant that automatically tracks, stores, and analyzes your AI conversation history (e.g., conversations with Assist, ChatGPT, or other AI agents).

Instead of just logging raw text, it provides meaningful insights through dedicated sensors, persistent storage across reboots, and a user-friendly configuration interface.

---

### ✨ Key Features
- **📊 Multi-Dimensional Sensors** – Real-time tracking of **Total Commands**, **Today's Commands**, and the **Top (Most Frequent) Intent**.
- **⚙️ UI Configuration Flow** – Configure maximum history entries and add custom **exclude words** directly via Home Assistant's Settings UI.
- **💾 Persistent Storage** – All data is saved to disk. You won't lose your chat history after restarting Home Assistant.
- **🛠 Custom Services** – Two built-in services: `clear_history` (erase all data) and `export_history` (export recent records to a notification).
- **🔒 Privacy First** – All data stays locally in your Home Assistant instance. No external API calls.

---

### 📥 Installation

#### Method 1: HACS (Recommended)
1. Ensure [HACS](https://hacs.xyz/) is installed in your Home Assistant.
2. Go to HACS → Integrations → Click the three dots (top right) → **Custom repositories**.
3. Add `https://github.com/56156/ha_ai_analytics` as a custom repository with category **Integration**.
4. Click **Download** and restart Home Assistant.

#### Method 2: Manual Installation
1. Download the `custom_components/ha_ai_analytics` folder from this repository.
2. Copy the `ha_ai_analytics` folder into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.

---

### ⚙️ Configuration
1. Go to **Settings** → **Devices & Services** → Click **+ Add Integration**.
2. Search for **"AI 交互分析中心" (AI Analytics)** and click it.
3. Configure the options:
   - **Max Entries** (Default: 200): The maximum number of chat records to store. Older entries will be automatically removed.
   - **Exclude Words** (Optional): Comma-separated keywords (e.g., `password,secret`) to filter out sensitive commands from being recorded.
4. Click **Submit**. The integration will start tracking immediately.

---

### 📊 Available Sensors
After setup, the following sensors will be created automatically:

| Sensor ID | Name | Description |
| :--- | :--- | :--- |
| `sensor.ai_total_commands` | AI 总指令数 (Total Commands) | Total count of all recorded AI interactions. |
| `sensor.ai_today_commands` | AI 今日指令数 (Today's Commands) | Count of interactions that occurred today. |
| `sensor.ai_top_intent` | AI 最常用意图 (Top Intent) | The most frequently used intent in the last 100 interactions. |

> ℹ️ The `sensor.ai_top_intent` also includes an attribute `recent_commands` showing the last 5 raw texts.

---

### 🛠 Services
You can call these services via **Developer Tools → Services**:

- **`ha_ai_analytics.clear_history`**  
  *Clears all stored interaction history and resets counters.*

- **`ha_ai_analytics.export_history`**  
  *Exports the latest 50 records as JSON and displays them in a Home Assistant persistent notification.*

---

### 🤝 Contributing & Support
This project is actively maintained by [@56156](https://github.com/56156).  
If you encounter any issues or have feature requests, please open an [Issue](https://github.com/56156/ha_ai_analytics/issues) or submit a Pull Request. Your contributions are highly welcome!

---

---

## 🇨🇳 中文版

### 项目简介
**HA AI Analytics（Home Assistant AI 交互分析中心）** 是一个功能完整的自定义集成，用于自动追踪、存储和分析你在 Home Assistant 中的 AI 对话历史（例如与 Assist、ChatGPT 或其他 AI 助手的对话）。

它不仅仅是记录原始文本，还通过专属传感器、重启不丢失的持久化存储以及友好的配置界面，为你提供有意义的洞察数据。

---

### ✨ 功能特点
- **📊 多维度传感器** – 实时追踪 **总指令数**、**今日指令数** 和 **最常用意图**（高频意图）。
- **⚙️ UI 配置界面** – 直接在 Home Assistant 的设置界面中配置最大历史条数以及自定义 **排除关键词**。
- **💾 持久化存储** – 所有数据自动存入磁盘，重启 Home Assistant 后历史记录不丢失。
- **🛠 自定义服务** – 内置两项服务：`clear_history`（一键清空数据）和 `export_history`（导出记录到通知）。
- **🔒 隐私优先** – 所有数据完全存储在本地 Home Assistant 实例中，无任何外部 API 调用。

---

### 📥 安装方法

#### 方式一：HACS（推荐）
1. 确保已安装 [HACS](https://hacs.xyz/)。
2. 进入 HACS → 集成 → 点击右上角三个点 → **自定义存储库**。
3. 添加 `https://github.com/56156/ha_ai_analytics`，类别选择 **集成**。
4. 点击 **下载**，然后重启 Home Assistant。

#### 方式二：手动安装
1. 从本仓库下载 `custom_components/ha_ai_analytics` 文件夹。
2. 将 `ha_ai_analytics` 文件夹复制到你的 Home Assistant 的 `custom_components` 目录下。
3. 重启 Home Assistant。

---

### ⚙️ 配置方法
1. 进入 **设置** → **设备与服务** → 点击 **+ 添加集成**。
2. 搜索 **"AI 交互分析中心"（AI Analytics）** 并点击。
3. 配置选项：
   - **最大条目数**（默认 200）：存储的最大聊天记录条数，超出会自动删除旧记录。
   - **排除词**（可选）：用英文逗号分隔的关键词（例如 `password,secret`），包含这些词的指令将不会被记录。
4. 点击 **提交**。集成将立即开始追踪。

---

### 📊 可用传感器
配置完成后，系统会自动创建以下传感器：

| 传感器 ID | 名称 | 描述 |
| :--- | :--- | :--- |
| `sensor.ai_total_commands` | AI 总指令数 | 记录的所有 AI 交互总数。 |
| `sensor.ai_today_commands` | AI 今日指令数 | 今天发生的交互数量。 |
| `sensor.ai_top_intent` | AI 最常用意图 | 最近 100 条交互中出现频率最高的意图。 |

> ℹ️ `sensor.ai_top_intent` 还附带有 `recent_commands` 属性，显示最近 5 条原始文本。

---

### 🛠 自定义服务
你可以在 **开发者工具 → 服务** 中调用以下服务：

- **`ha_ai_analytics.clear_history`**  
  *清空所有存储的交互历史并重置计数器。*

- **`ha_ai_analytics.export_history`**  
  *将最近 50 条记录导出为 JSON 格式，并通过 Home Assistant 的持久通知展示。*

---

### 🤝 贡献与支持
本项目由 [@56156](https://github.com/56156) 积极维护。  
如果你遇到任何问题或有功能建议，欢迎提交 [Issue](https://github.com/56156/ha_ai_analytics/issues) 或发起 Pull Request。非常期待你的参与！

---

**🎉 Enjoy tracking your AI interactions with ease! / 轻松追踪你的 AI 交互数据！**

# ha_ai_analytics
Home Assistant AI 交互分析中心 - 追踪对话总量/今日/高频意图，支持数据过滤与导出 / AI Chat Analytics with total/today/top-intent sensors, filtering &amp; export
