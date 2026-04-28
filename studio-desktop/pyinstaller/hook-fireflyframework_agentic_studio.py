"""PyInstaller hidden-imports hook for fireflyframework-agentic.

Ensures that all runtime-discovered sub-packages and optional
dependencies are bundled into the frozen executable.
"""

hiddenimports = [
    # Studio server
    "fireflyframework_agentic_studio",
    "fireflyframework_agentic_studio.cli",
    "fireflyframework_agentic_studio.server",
    "fireflyframework_agentic_studio.config",
    "fireflyframework_agentic_studio.projects",
    "fireflyframework_agentic_studio.api.assistant",
    "fireflyframework_agentic_studio.api.checkpoints",
    "fireflyframework_agentic_studio.api.codegen",
    "fireflyframework_agentic_studio.api.execution",
    "fireflyframework_agentic_studio.api.files",
    "fireflyframework_agentic_studio.api.monitoring",
    "fireflyframework_agentic_studio.api.projects",
    "fireflyframework_agentic_studio.api.registry",
    "fireflyframework_agentic_studio.api.settings",
    "fireflyframework_agentic_studio.api.evaluate",
    "fireflyframework_agentic_studio.api.experiments",
    "fireflyframework_agentic_studio.settings",
    "fireflyframework_agentic_studio.evaluation",
    "fireflyframework_agentic_studio.codegen.generator",
    "fireflyframework_agentic_studio.codegen.models",
    "fireflyframework_agentic_studio.execution.compiler",
    "fireflyframework_agentic_studio.execution.runner",
    "fireflyframework_agentic_studio.execution.checkpoint",
    # Pipeline engine
    "fireflyframework_agentic.pipeline.builder",
    "fireflyframework_agentic.pipeline.context",
    "fireflyframework_agentic.pipeline.dag",
    "fireflyframework_agentic.pipeline.engine",
    "fireflyframework_agentic.pipeline.steps",
    # Agent framework
    "fireflyframework_agentic.agents.base",
    "fireflyframework_agentic.agents.registry",
    "fireflyframework_agentic.agents.context",
    "fireflyframework_agentic.agents.middleware",
    # Tools & reasoning
    "fireflyframework_agentic.tools.registry",
    "fireflyframework_agentic.reasoning.registry",
    # Config
    "fireflyframework_agentic.config",
    # Web server dependencies
    "uvicorn",
    "uvicorn.logging",
    "uvicorn.loops",
    "uvicorn.loops.auto",
    "uvicorn.protocols",
    "uvicorn.protocols.http",
    "uvicorn.protocols.http.auto",
    "uvicorn.protocols.websockets",
    "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan",
    "uvicorn.lifespan.on",
    "fastapi",
    "starlette",
    "starlette.staticfiles",
    "pydantic",
    "pydantic_settings",
    "httpx",
]
