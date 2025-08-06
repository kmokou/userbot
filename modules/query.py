from gradio_client import Client
from telethon import events
from utils.decorators import admin_only
from config.constants import STANDARD_SYSTEM_PROMPT, SHORT_SYSTEM_PROMPT
import re

TELEGRAM_MSG_LIMIT = 4096

async def query(message: str, system_prompt: str) -> str:
    client = Client("amd/gpt-oss-120b-chatbot")
    result = client.predict(
        message=message,
        system_prompt=system_prompt,
        temperature=0.7,
        api_name="/chat"
    )
    return result

def register(client):
    @client.on(events.NewMessage(pattern=r"^.ai($| )"))
    @admin_only
    async def handler(event):
        text = event.raw_text

        # If no prompt and not replying
        if text.replace(' ', '') == ".ai" and not event.is_reply:
            await event.edit('**Prompt is absent**', parse_mode="md")
            return

        # Get replied message if any
        replied_msg = await event.get_reply_message() if event.is_reply else None
        replied_text = replied_msg.raw_text if replied_msg else None

        # Inform user it's loading
        await event.edit(f"{text}\n\n**Loading...**", parse_mode="md")

        # Extract user prompt after .ai
        user_input = text[4:].strip()

        # Combine replied text and user input
        combined_message = f"{replied_text}\n\n{user_input}".strip() if replied_text else user_input.strip()

        # Get system prompt type
        system_prompt_base = SHORT_SYSTEM_PROMPT if "--short" in combined_message else STANDARD_SYSTEM_PROMPT

        # Extract custom system prompt if present
        bracket_match = re.search(r"\[\[(.*?)\]\]", combined_message, re.DOTALL)
        system_prompt = f"{system_prompt_base}\n{bracket_match.group(1)}" if bracket_match else system_prompt_base

        # Remove [[...]], --short, and --think from prompt
        clean_prompt = re.sub(r"\[\[.*?\]\]", "", combined_message)
        clean_prompt = re.sub(r"--short", "", clean_prompt)
        clean_prompt = re.sub(r"--think", "", clean_prompt)
        clean_prompt = clean_prompt.strip()

        # Query the model
        result = await query(clean_prompt, system_prompt)

        # Handle response split
        parts = result.split('---', 1)
        analysis = parts[0] if len(parts) == 2 else ""
        response = parts[1] if len(parts) == 2 else parts[0]

        # Decide final output
        include_analysis = "--think" in combined_message
        final_response = (analysis + response) if include_analysis else response.lstrip()

        # Compose final message
        display_message = f"**{clean_prompt}**\n\n{final_response}"

        # Truncate if over Telegram limit
        if len(display_message) > TELEGRAM_MSG_LIMIT:
            display_message = display_message[:TELEGRAM_MSG_LIMIT - 20].rstrip() + "\n\n... [truncated]"

        await event.edit(display_message, parse_mode="md")
