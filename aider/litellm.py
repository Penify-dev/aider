import os
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

os.environ["OR_SITE_URL"] = "http://aider.chat"
os.environ["OR_APP_NAME"] = "Aider"

# Try to import litellm, but provide a fallback if it's not available
try:
    import litellm  # noqa: E402
    litellm.suppress_debug_info = True
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False

    # Create a mock litellm module with stub implementations
    class MockLiteLLM:
        """Mock litellm module for when the package is not properly installed."""

        suppress_debug_info = True
        model_cost = {}

        def validate_environment(self, model):
            """Stub implementation that returns a basic response."""
            return {
                "keys_in_environment": False,
                "missing_keys": []
            }

        def get_model_info(self, model):
            """Stub implementation that returns None (no model info available)."""
            return None

        def __getattr__(self, name):
            """Handle any other attribute access gracefully."""
            def stub_method(*args, **kwargs):
                # Don't print warning for every call, just return None
                return None
            return stub_method

    litellm = MockLiteLLM()
    print(
        "Warning: litellm is not properly installed. "
        "Functionality that requires it (e.g., pricing lookup or "
        "non-Ollama providers) is disabled.",
        file=sys.stderr
    )

__all__ = ["litellm", "LITELLM_AVAILABLE"]
