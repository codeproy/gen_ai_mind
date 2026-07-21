# AGENTS.md

## Repository State

This is a Jupyter notebook project for experimenting with LangChain, LangGraph, and CrewAI. The README describes an intended project structure but most directories and files (`src/`, `config/`, `examples/`, `tests/`) do not exist yet.

**Current actual structure:**
- `notebooks/get_started_script.ipynb` — main entrypoint
- `requirements.txt` — dependencies
- `.env` — keys (recently created, empty)

## Environment & Dependencies

- Python virtual environment at `.venv/`
- Activate: `source .venv/bin/activate`
- Dependencies include: openai, langchain, langgraph, langchain-openai, pydantic-settings, python-dotenv, tiktoken
- **No pyproject.toml** — uses `requirements.txt` only. Install with: `pip install -r requirements.txt`
- No formatter, linter, or type checker configured.

## Key Conventions

- Always load environment variables at the start of any script or notebook: `load_dotenv()` then `os.getenv(...)`
- Use `pydantic-settings` (BaseSettings) for config classes if creating config modules.
- Prefer `langchain-openai` ChatOpenAI over direct OpenAI API calls.
- If creating package code, follow the README's tree structure as a guide.
