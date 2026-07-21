# Gen AI Mind

A comprehensive generative AI project leveraging cutting-edge frameworks and libraries to build intelligent, autonomous systems powered by large language models (LLMs).

## Overview

This project demonstrates the integration of modern AI frameworks to create sophisticated applications with capabilities including:

- **Chains & Workflows**: Complex multi-step reasoning pipelines using LangChain
- **Agent Orchestration**: Multi-agent systems with LangGraph for distributed decision-making
- **Collaborative Intelligence**: Crew-based AI agents with specialized roles using CrewAI
- **Memory & Context**: Intelligent context management and conversation history
- **Tool Integration**: Seamless integration with external APIs and custom tools

## Tech Stack

### Core Frameworks

- **[LangChain](https://www.langchain.com/)** - Framework for developing applications with language models
  - Chain orchestration
  - Prompt management
  - Memory systems
  - Document processing and retrieval

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Agentic framework for building multi-agent systems
  - State management
  - Graph-based workflows
  - Complex reasoning patterns
  - Conditional routing

- **[CrewAI](https://www.crewai.com/)** - Multi-agent collaboration framework
  - Specialized agent roles
  - Task management
  - Inter-agent communication
  - Hierarchical task execution

### Additional Components

- **LLM Providers**: OpenAI, Anthropic, Hugging Face, local models
- **Vector Databases**: Pinecone, Weaviate, Chroma, FAISS
- **RAG**: Retrieval-Augmented Generation for enhanced context
- **Monitoring**: Structured logging and performance tracking

## Project Structure

```
gen_ai_mind/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── settings.py
│   └── models.py
├── src/
│   ├── chains/
│   │   ├── __init__.py
│   │   └── workflows.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── crew_agents.py
│   │   └── langraph_agents.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── custom_tools.py
│   ├── memory/
│   │   ├── __init__.py
│   │   └── context_manager.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── examples/
│   ├── simple_chain.py
│   ├── multi_agent_workflow.py
│   └── crew_collaborative_task.py
└── tests/
    ├── __init__.py
    └── test_workflows.py
```

## Quick Start

### Prerequisites

- Python 3.10+
- pip or poetry for package management
- API keys for LLM providers (OpenAI, Anthropic, etc.)

### Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd gen_ai_mind
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

## Key Concepts

### Chains (LangChain)

Chains represent sequences of LLM calls and external tools:

```python
from langchain import OpenAI, LLMChain, PromptTemplate

llm = OpenAI(temperature=0.7)
prompt = PromptTemplate(template="...", input_variables=["topic"])
chain = LLMChain(llm=llm, prompt=prompt)
```

### Agents (LangGraph)

Agents make decisions and take actions based on observations:

```python
from langgraph.graph import StateGraph

graph = StateGraph(State)
graph.add_node("research", research_node)
graph.add_node("analyze", analyze_node)
graph.add_conditional_edges("research", route_to_next)
```

### Crews (CrewAI)

Multiple agents collaborate on complex tasks:

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Researcher", goal="...", tools=[...])
analyst = Agent(role="Analyst", goal="...", tools=[...])
crew = Crew(agents=[researcher, analyst], tasks=[...])
```

## Usage Examples

### Example 1: Simple LLM Chain

```bash
python examples/simple_chain.py
```

### Example 2: Multi-Agent Workflow

```bash
python examples/multi_agent_workflow.py
```

### Example 3: Crew-Based Collaboration

```bash
python examples/crew_collaborative_task.py
```

## Configuration

Configure your project via `config/settings.py`:

- **Model Selection**: Choose your primary LLM
- **Temperature & Sampling**: Control model creativity
- **API Keys**: Manage credentials securely
- **Tool Configuration**: Define available tools and integrations
- **Memory Settings**: Configure persistence and retrieval strategies

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

## Performance Optimization

- Use streaming where applicable for real-time responses
- Implement caching for frequently used queries
- Batch operations for improved throughput
- Monitor token usage and costs
- Optimize prompt engineering for better results

## Best Practices

1. **Prompt Engineering**: Craft clear, specific prompts for better LLM responses
2. **Error Handling**: Implement robust error handling and retry logic
3. **Monitoring**: Log all operations for debugging and analysis
4. **Security**: Never commit API keys; use environment variables
5. **Testing**: Thoroughly test chains and agents before production
6. **Versioning**: Track model versions and prompt iterations

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact & Support

For questions, issues, or suggestions, please:
- Open an issue on GitHub
- Create a discussion thread
- Contact the project maintainers

---

**Last Updated**: April 2026
