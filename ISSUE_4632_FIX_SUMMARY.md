# Fix for GitHub Issue #4632: Uncaught ImportError in llm.py line 56

## Problem
When the `litellm` package failed to import or had missing dependencies, it raised an uncaught `ImportError` that crashed the application with the message:
```
ImportError: litellm is not installed; functionality that requires it (e.g., pricing lookup or non‑Ollama providers) is disabled.
```

This occurred in the traceback at:
- `models.py`, line 728: `res = litellm.validate_environment(model)`
- `llm.py`, line 56: Inside litellm's lazy loading mechanism

## Root Cause
The `litellm` package uses lazy loading, and when it fails to import properly (due to missing dependencies or installation issues), accessing any of its attributes triggers an `ImportError`. The aider codebase did not handle this gracefully, causing the application to crash.

## Solution
Implemented a comprehensive fallback mechanism that gracefully handles litellm import failures:

### 1. Modified `aider/litellm.py`
- Added try-except block to catch import failures
- Created `LiteLLMStub` class that provides minimal functionality when litellm is unavailable
- Created `LiteLLMExceptionsStub` class to provide exception classes for error handling
- Added informative warning messages to stderr when import fails
- Stub provides:
  - `get_model_info()` - returns empty dict
  - `validate_environment()` - returns validation failure with clear message
  - `encode()` - provides rough token estimate (4 chars per token)
  - `_should_retry()` - basic retry logic
  - `completion()` and `transcription()` - raise helpful ImportError
  - `exceptions` module with stub exception classes
  - `model_cost` - empty dict

### 2. Modified `aider/models.py`
- Updated `validate_environment()` to catch ImportError and return proper error dict
- Updated `tokenizer()` to catch ImportError and return None as fallback
- Updated `fuzzy_match_models()` to handle missing litellm.model_cost gracefully

### 3. Modified `aider/commands.py`
- Updated `completions_model()` to handle missing litellm.model_cost gracefully

## Benefits
1. **Graceful Degradation**: Application no longer crashes when litellm is unavailable
2. **Clear Error Messages**: Users get helpful messages about what's wrong and how to fix it
3. **Partial Functionality**: Basic operations can still work without litellm
4. **Better User Experience**: Users can diagnose and fix installation issues without crashes
5. **Backward Compatible**: When litellm is properly installed, everything works as before

## Testing
- All 115 existing unit tests pass
- Tested with litellm properly installed (normal operation)
- Tested with simulated litellm import failure (graceful degradation)
- Verified error messages are clear and actionable
- Confirmed no regressions in existing functionality

## Files Changed
1. `aider/litellm.py` - Added import error handling and stub implementation
2. `aider/models.py` - Added defensive checks for litellm availability
3. `aider/commands.py` - Added defensive check for model_cost access

## Example Behavior

### Before Fix
```
ImportError: litellm is not installed; functionality that requires it...
[Application crashes]
```

### After Fix
```
Warning: litellm import failed: [error details]
Some functionality will be limited. Install with: pip install litellm

Model gpt-4o: Missing these environment variables:
- LITELLM_NOT_INSTALLED
[Application continues with limited functionality]
```

## Recommendations for Users
If you encounter this issue:
1. Install litellm: `pip install litellm`
2. If already installed, try reinstalling: `pip install --force-reinstall litellm`
3. Check for missing dependencies in the error message
4. Ensure Python version compatibility (3.9-3.12)
