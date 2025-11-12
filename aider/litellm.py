import os
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

os.environ["OR_SITE_URL"] = "http://aider.chat"
os.environ["OR_APP_NAME"] = "Aider"


class LiteLLMExceptionsStub:
    """Stub for litellm.exceptions when litellm is not available"""
    
    class APIConnectionError(Exception):
        pass
    
    class APIError(Exception):
        pass
    
    class RateLimitError(Exception):
        pass
    
    class ServiceUnavailableError(Exception):
        pass
    
    class Timeout(Exception):
        pass
    
    class BadRequestError(Exception):
        pass


class LiteLLMStub:
    """Stub implementation when litellm is not available"""
    
    suppress_debug_info = True
    model_cost = {}
    exceptions = LiteLLMExceptionsStub()
    
    def __init__(self):
        self._import_error = None
    
    def get_model_info(self, model):
        """Return empty dict when litellm is not available"""
        return {}
    
    def validate_environment(self, model):
        """Return validation failure when litellm is not available"""
        return {
            "keys_in_environment": False,
            "missing_keys": ["LITELLM_NOT_INSTALLED"]
        }
    
    def encode(self, model, text):
        """Fallback tokenizer - rough estimate"""
        # Rough estimate: ~4 characters per token
        return [0] * (len(text) // 4)
    
    def _should_retry(self, status_code):
        """Stub for retry logic"""
        return status_code in [429, 500, 502, 503, 504]
    
    def completion(self, **kwargs):
        """Stub for completion - raises error"""
        error_msg = (
            "litellm is not installed or failed to import; "
            "cannot make API calls without litellm.\n"
            "Please install litellm with: pip install litellm"
        )
        if self._import_error:
            error_msg += f"\n\nOriginal import error: {self._import_error}"
        raise ImportError(error_msg)
    
    def transcription(self, **kwargs):
        """Stub for transcription - raises error"""
        error_msg = (
            "litellm is not installed or failed to import; "
            "cannot make transcription calls without litellm.\n"
            "Please install litellm with: pip install litellm"
        )
        if self._import_error:
            error_msg += f"\n\nOriginal import error: {self._import_error}"
        raise ImportError(error_msg)
    
    def __getattr__(self, name):
        """Raise helpful error for any other attribute access"""
        error_msg = (
            "litellm is not installed or failed to import; "
            "functionality that requires it (e.g., pricing lookup or non-Ollama providers) is disabled.\n"
            "Please install litellm with: pip install litellm"
        )
        if self._import_error:
            error_msg += f"\n\nOriginal import error: {self._import_error}"
        raise ImportError(error_msg)


# Try to import litellm, fall back to stub if it fails
try:
    import litellm  # noqa: E402
    litellm.suppress_debug_info = True
except ImportError as e:
    print(
        f"Warning: litellm import failed: {e}",
        file=sys.stderr
    )
    print(
        "Some functionality will be limited. Install with: pip install litellm",
        file=sys.stderr
    )
    litellm = LiteLLMStub()
    litellm._import_error = str(e)
except Exception as e:
    print(
        f"Warning: litellm initialization failed: {e}",
        file=sys.stderr
    )
    print(
        "Some functionality will be limited. Try reinstalling: pip install --force-reinstall litellm",
        file=sys.stderr
    )
    litellm = LiteLLMStub()
    litellm._import_error = str(e)

__all__ = ["litellm"]
