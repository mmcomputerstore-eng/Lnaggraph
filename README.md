# LangGraph Learning Project

A hands-on learning repository exploring **multiple approaches, state patterns, and workflow architectures in LangGraph**. Each script focuses on a distinct LangGraph concept—ranging from state schema definitions and sequential pipelines to parallel fan-out execution, conditional RAG routing, cyclic writer-reviewer loops with tool calling, and a Streamlit chat interface.

---

## What This Project Covers

| File | Pattern / Approach | Key Concepts Demonstrated |
| :--- | :--- | :--- |
| `states.py` | **State Schema Approaches** | Comparing `TypedDict`, Pydantic `BaseModel` (with `@field_validator`), Python `@dataclass`, and LangGraph's `MessagesState` |
| `project.py` | **Sequential Workflow** | Linear node-to-node pipeline (`START → editor → scriptwriter → translator → END`) for copyediting, scripting, and Hinglish localization |
| `parallel_workflow.py` | **Parallel Workflow (Fan-Out)** | Concurrent execution of 3 safety-check branches (`toxicity_node`, `copyright_check`, `culture_node`) merged via a custom `Annotated` dictionary reducer (`merge_score_dicts`) |
| `conditional_rag.py` | **Conditional Routing + RAG (CLI)** | Query classification (`academic`, `fee`, `general`), `add_conditional_edges` routing, FAISS vector retrieval over PDFs (`academics_handbook.pdf`, `fee_structure.pdf`), and programme-aware CLI chat |
| `iterative_workflow.py` | **Iterative / Cyclic Workflow + Tools** | Feedback-driven LinkedIn post generator & reviewer loop (max 3 attempts) combining tool calling (`TavilySearch` via `ToolNode`), Gemini (`ChatGoogleGenerativeAI`), and Groq (`ChatGroq`) |
| `app.py` | **Streamlit UI for Conditional RAG** | Interactive web chat UI for the College Assistant graph with cached FAISS retrievers, programme selector (`BCA`, `BBA`, `B.Com (H)`), conversation state, and route badges |

---

## Project Structure

```text
.
├── app.py                     # Streamlit College Assistant UI (Conditional RAG)
├── conditional_rag.py         # CLI version of the Conditional RAG workflow
├── iterative_workflow.py      # Writer–Reviewer cyclic graph with Tavily web search
├── parallel_workflow.py       # Parallel fan-out safety analyzer with custom state reducer
├── project.py                 # 3-stage sequential content transformation pipeline
├── states.py                  # Reference examples of 4 LangGraph state schema styles
├── academics_handbook.pdf     # Sample knowledge base for academic queries
├── fee_structure.pdf          # Sample knowledge base for fee queries
├── requirements.txt           # Python dependencies
└── .env.example               # Template for required API keys
```

---

## Tech Stack

- **Orchestration:** `langgraph`, `langchain`
- **LLM Providers:** `langchain-groq` (`ChatGroq`), `langchain-google-genai` (`ChatGoogleGenerativeAI`)
- **RAG & Embeddings:** `langchain-community` (`PyPDFLoader`, `FAISS`), `langchain-huggingface`, `sentence-transformers` (`all-MiniLM-L6-v2`), `faiss-cpu`, `pypdf`, `langchain-text-splitters`
- **Tools:** `langchain-tavily` (`TavilySearch`)
- **UI & Utilities:** `streamlit`, `pydantic`, `python-dotenv`

---

## Setup & Installation

1. **Clone the repository and enter the project directory:**
   ```bash
   git clone <your-repo-url>
   cd Lnaggraph
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   # venv\Scripts\activate         # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and add your API keys:
   ```bash
   cp .env.example .env
   ```
   Variables defined in `.env.example`:
   - `GROQ_API_KEY` — required for `ChatGroq` workflows (`project.py`, `parallel_workflow.py`, `conditional_rag.py`, `iterative_workflow.py`, `app.py`)
   - `TAVILY_API_KEY` — required for web search in `iterative_workflow.py`
   - `GEMINI_API_KEY` — required for `ChatGoogleGenerativeAI` in `iterative_workflow.py`
   - `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT` — optional for LangSmith tracing

---

## Usage

### 1. Run the Streamlit College Assistant (`app.py`)
```bash
streamlit run app.py
```
Select your programme (`BCA`, `BBA`, or `B.Com (H)`) in the sidebar and ask questions about academics, fees, or general topics.

### 2. Run Individual Workflow Scripts
- **Sequential Pipeline:**
  ```bash
  python project.py
  ```
- **Parallel Safety Analyzer:**
  ```bash
  python parallel_workflow.py
  ```
- **Iterative LinkedIn Post Generator:**
  ```bash
  python iterative_workflow.py
  ```
- **Conditional RAG CLI:**
  ```bash
  python conditional_rag.py
  ```
  > **Note:** `conditional_rag.py` currently references absolute PDF paths (`/home/mubeen/Documents/genrative AI/Lnaggraph/*.pdf`). If running from another location, update those paths to `"academics_handbook.pdf"` and `"fee_structure.pdf"` (as used in `app.py`).
