# Fix for GitHub Issue #4638: Unhelpful "LLM Provider not provided" Error

## Problem
Users encountering the `litellm.BadRequestError: LLM Provider NOT provided` error received an unhelpful error message with no actionable guidance on how to fix the issue.

## Solution
Enhanced the error handling in `aider/coders/base_coder.py` to detect provider-related errors and provide context-specific, actionable guidance.

## Changes Made

### 1. Added Helper Method
Created `_get_helpful_provider_error_message()` method that:
- Detects "LLM Provider NOT provided" errors
- Analyzes the model name to provide specific guidance
- Returns enhanced error messages with troubleshooting steps

### 2. Updated Exception Handler
Modified the `litellm.exceptions.BadRequestError` handler to:
- Check if it's a provider-related error
- Call the helper method to get enhanced message
- Display helpful message instead of raw error

## Example Error Messages

### Before (Unhelpful)
```
BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=local/qwen3-coder:30b
 Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: 
https://docs.litellm.ai/docs/providers
```

### After (Helpful) - For `local/` prefix

```
BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=local/qwen3-coder:30b

This error occurs when the model name doesn't include a valid provider prefix,
or when required environment variables are not set correctly.

You're using model: local/qwen3-coder:30b

The 'local/' prefix is not a standard LiteLLM provider.
For local models via Ollama, you should:

1. Use the 'ollama/' or 'ollama_chat/' prefix instead:
   aider --model ollama/qwen3-coder:30b

2. Set the OLLAMA_API_BASE environment variable (not OPENAI_API_BASE):
   export OLLAMA_API_BASE=http://127.0.0.1:11434

3. Make sure the URL does NOT include '/v1' or a trailing '/'

Example:
   export OLLAMA_API_BASE=http://127.0.0.1:11434
   aider --model ollama/qwen3-coder:30b

For more information:
  - Ollama setup: https://aider.chat/docs/llms.html#ollama
  - All LLM providers: https://aider.chat/docs/llms.html
  - LiteLLM providers: https://docs.litellm.ai/docs/providers
```

### After (Helpful) - For model without provider prefix

```
BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call.

This error occurs when the model name doesn't include a valid provider prefix,
or when required environment variables are not set correctly.

You're using model: qwen3-coder:30b

Model names should include a provider prefix in the format: provider/model-name

Common examples:
  - OpenAI: openai/gpt-4o or just gpt-4o
  - Anthropic: anthropic/claude-3-opus-20240229 or just claude-3-opus-20240229
  - Ollama: ollama/llama3:70b or ollama_chat/llama3:70b
  - Groq: groq/llama3-70b-8192
  - OpenRouter: openrouter/meta-llama/llama-3-70b-instruct

For more information:
  - Ollama setup: https://aider.chat/docs/llms.html#ollama
  - All LLM providers: https://aider.chat/docs/llms.html
  - LiteLLM providers: https://docs.litellm.ai/docs/providers
```

## Key Improvements

1. **Specific guidance for `local/` prefix**: Directly addresses the most common issue mentioned in the GitHub issue
2. **Clear environment variable instructions**: Explicitly states to use `OLLAMA_API_BASE` not `OPENAI_API_BASE`
3. **URL format warnings**: Warns about common mistakes like including `/v1` or trailing `/`
4. **Concrete examples**: Shows exact commands to use
5. **Relevant documentation links**: Points to aider-specific documentation, not just generic LiteLLM docs
6. **Pattern-based guidance**: Different messages for different error patterns (local/, no prefix, etc.)

## Testing

All existing tests pass:
- ✅ 18/18 tests in `tests/test_coder.py` pass
- ✅ Custom test script validates all error message patterns
- ✅ Error handling for non-provider errors unchanged
- ✅ Backward compatibility maintained

## Files Modified

- `aider/coders/base_coder.py`: Added helper method and enhanced exception handler

## Addresses Issue #4638

This fix directly addresses all the pain points mentioned in the issue:
- ✅ Explains what the error means
- ✅ Provides specific guidance for `local/` prefix users
- ✅ Clarifies the difference between `OPENAI_API_BASE` and `OLLAMA_API_BASE`
- ✅ Warns about URL format issues (`/v1`, trailing `/`)
- ✅ Links to relevant aider documentation
- ✅ Shows concrete examples of correct usage
