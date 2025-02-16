"""
AI integration module for CodeSmelt
Supports both OpenAI and xAI APIs for generating code documentation

Author: Shiraz Akmal & AI

"""

import os
from typing import Optional
from openai import OpenAI, OpenAIError, BadRequestError

def get_ai_client(provider: str = "openai") -> Optional[OpenAI]:
    """Initialize AI client based on available API keys"""
    try:
        if provider == "xai":
            api_key = os.getenv("XAI_API_KEY")
            if api_key:
                return OpenAI(
                    api_key=api_key,
                    base_url="https://api.x.ai/v1"
                )
        else:  # openai
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                return OpenAI(api_key=api_key)
        return None
    except Exception as e:
        print(f"Warning: Failed to initialize {provider} client: {e}")
        return None

def generate_summary(content: str, provider: str = "openai", custom_model: Optional[str] = None) -> Optional[str]:
    """Generate documentation summary using AI"""
    client = get_ai_client(provider)
    if not client:
        print(f"Notice: Could not initialize {provider} client. Skipping summary generation.")
        return None

    try:
        # Limit content size based on model
        max_tokens = 4000  # Default for most models
        if custom_model:
            if custom_model.startswith("grok"):
                max_tokens = 130000  # xAI models have larger context
            elif custom_model in ["gpt-4", "gpt-4o"]:
                max_tokens = 7000  # Leave room for response
            print(f"Debug: Using token limit of {max_tokens} for model {custom_model}")

        # More conservative token estimation (3 chars per token instead of 4)
        content_preview = content[:max_tokens * 3]  # Approximate token count
        print(f"Debug: Content preview length: {len(content_preview)} characters")

        prompt = """
        Please analyze the following source code and generate a comprehensive README-style documentation.
        Focus on:
        1. Project structure and organization
        2. Key functionality and features
        3. Important classes and their purposes
        4. Notable algorithms or patterns used
        5. Dependencies and requirements

        Respond in markdown format.

        Source code:

        {content}
        """.format(content=content_preview)

        # Use custom model if provided, otherwise use defaults
        if custom_model:
            model = custom_model
        elif provider == "xai":
            model = "grok-2-1212"
        else:
            model = "gpt-4o"

        print(f"Using AI model: {model}")  # Debug info for user

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert code analyst specializing in generating clear, comprehensive documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "text"}
        )

        return response.choices[0].message.content

    except BadRequestError as e:
        # Handle specific OpenAI errors (like token limits) gracefully
        print(f"Notice: {provider} API request failed - {str(e)}")
        if "context_length_exceeded" in str(e):
            print("The content is too long for this model's context window. Try using a model with larger context (e.g., grok-2-1212)")
        return None
    except OpenAIError as e:
        # Handle other OpenAI-specific errors
        print(f"Notice: {provider} API error occurred - {str(e)}")
        return None
    except Exception as e:
        print(f"Notice: Failed to generate summary using {provider} with model {model}: {e}")
        # Try the alternative provider if the first one fails and no custom model was specified
        if provider == "openai" and not custom_model:
            print("Trying xAI as fallback...")
            return generate_summary(content, provider="xai")
        return None

def try_all_providers(content: str, custom_model: Optional[str] = None) -> Optional[str]:
    """Try all available AI providers and return the first successful result"""
    # If custom model is specified, determine the provider based on the model name
    if custom_model:
        if custom_model.startswith("grok"):
            if not os.getenv("XAI_API_KEY"):
                print("Notice: XAI_API_KEY environment variable is not set. "
                      "Required for using Grok models.")
                return None
            return generate_summary(content, provider="xai", custom_model=custom_model)
        else:
            if not os.getenv("OPENAI_API_KEY"):
                print("Notice: OPENAI_API_KEY environment variable is not set. "
                      "Required for using OpenAI models.")
                return None
            return generate_summary(content, provider="openai", custom_model=custom_model)

    # Try OpenAI first, then fall back to xAI if no custom model specified
    for provider in ["openai", "xai"]:
        if provider == "openai" and not os.getenv("OPENAI_API_KEY"):
            print("Notice: OPENAI_API_KEY not found, trying xAI...")
            continue
        if provider == "xai" and not os.getenv("XAI_API_KEY"):
            print("Notice: XAI_API_KEY not found, no more providers to try.")
            return None
        print(f"Attempting to generate summary using {provider}...")
        summary = generate_summary(content, provider)
        if summary:
            return summary
    return None