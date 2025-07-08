# 🏦 Multi-Agent Meta-Tool Hedge Fund Analysis System

A cutting-edge, modular AI system for advanced financial analysis—built using the Strands Agents SDK and leveraging state-of-the-art LLMs (Claude 4 Sonnet, Claude 3 Haiku, Amazon Nova Lite) via AWS Bedrock. This project demonstrates a full-stack, agentic approach to automating investment analysis with human-in-the-loop controls, meta-tooling, detailed observability, and code execution.

---
### Architecture

<img src="https://github.com/akankshakusf/Project-Strands-Multi-Agent-System--Bedrock/blob/master/img/Architecture.png" width="100%" />

## 🚀 Overview

This repository showcases a **hierarchical Multi-Agent Collaboration (MAC)** system for **hedge fund-style financial analysis**. Powered by the Strands Agents SDK, the system employs a _Lead Analyst_ (meta-coordinator) and multiple specialized financial agents as tools, integrating real-time data and dynamic tool creation for a comprehensive investment research workflow.

---

## 🏗️ Architecture

### Agent Hierarchy

- **Lead Analyst Agent (Meta-Coordinator)**
  - **Model:** Claude 4 Sonnet
  - **Role:** Synthesizes insights, routes queries, dynamically loads tools, manages HITL approvals
  - **Features:** Dynamic tool creation, meta-tooling, human-in-the-loop, observability, logging

- **Fundamental Analyst Agent**
  - **Model:** Claude 3 Haiku
  - **Focus:** Income statements, balance sheets, cash flow, ratios, valuation

- **Technical Analyst Agent**
  - **Model:** Amazon Nova Lite
  - **Focus:** Price data, technical indicators (RSI, MACD, SMA, EMA), chart patterns, signals

- **Market Analyst Agent**
  - **Model:** Claude 3 Haiku
  - **Focus:** Options chain, insider trades, news aggregation, sentiment



---

## 🛠️ Key Features

- **Agent-as-Tools Pattern:** Each sub-agent acts as a callable tool under the meta-agent.
- **Meta-Tooling:** Dynamic creation/loading of tools, code execution, shell and editor access.
- **Human-in-the-Loop (HITL):** Interactive approval required for sensitive tool calls (e.g., insider trades, news).
- **Observability & Logging:** Full traces, logs, and context management for every operation.
- **Multi-Model Orchestration:** Combines Claude 4 Sonnet (supervisor), Claude 3 Haiku, and Amazon Nova Lite.
- **Advanced Data Integration:** Pulls real-time and historical data (APIs: income, balance, cash flow, options, news, insider).
- **Safe Code Execution:** On-demand code generation and controlled execution with timeouts.
- **Pre-Built & Custom Tools:** Calculator, file read, Python REPL, journal, mem0 memory, time/date, plus all custom financial tools.

---

## 🔌 Custom Tool Ecosystem

- `get_income_statements`: Income statement retrieval
- `get_balance_sheets`: Balance sheet data
- `get_cash_flow_statements`: Cash flow details
- `get_stock_prices`: Historical price data
- `get_current_stock_price`: Real-time quote
- `get_technical_indicators`: RSI, MACD, SMA, EMA
- `get_options_chain`: Options contract data
- `get_insider_trades`: Insider trading info
- `get_news`: News & sentiment
- `generate_and_execute_code`: Dynamic Python code/visualization
- **Prebuilt:** calculator, file_read, python_repl, journal, mem0_memory, current_time

---

## 👤 Human-in-the-Loop (HITL) Design

Sensitive tool calls (e.g., insider trading, news access) trigger an approval prompt:
- Approve, edit, or deny the operation in real time
- Full review/edit context before execution

---

## 🧩 Example Workflow

1. **User Query:**  
   "What is the current outlook for Apple (AAPL)?"

2. **Meta-Agent Routing:**  
   Lead Analyst coordinates which sub-agents/tools to call.

3. **Specialist Agents:**  
   - Fundamental: Income, balance, cash flow
   - Technical: Trends, indicators
   - Market: Options, news, sentiment

4. **Meta-Tooling:**  
   If custom analysis or code is required, the system generates and executes Python snippets safely.

5. **Human-in-the-Loop:**  
   For sensitive data, requests are paused for approval.

6. **Aggregation & Report:**  
   Results are synthesized into a markdown summary/report.

---

