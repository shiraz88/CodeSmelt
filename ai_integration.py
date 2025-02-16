"""
AI integration module for CodeSmelt
Supports both OpenAI and xAI APIs for generating code documentation

Author: Shiraz Akmal & AI

"""

import os
from typing import Optional
from openai import OpenAI

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
        return None

    try:
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
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
        """.format(content=content)

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

    except Exception as e:
        print(f"Warning: Failed to generate summary using {provider} with model {model}: {e}")
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
            return generate_summary(content, provider="xai", custom_model=custom_model)
        else:
            return generate_summary(content, provider="openai", custom_model=custom_model)

    # Try OpenAI first, then fall back to xAI if no custom model specified
    for provider in ["openai", "xai"]:
        summary = generate_summary(content, provider)
        if summary:
            return summary
    return None