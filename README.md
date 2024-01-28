# Generates text completion using the together.xyz API

## Args

- **history**: A list of dictionaries representing the conversation history. Each dictionary should have 'role' and 'content' keys, where 'role' represents the role of the speaker and 'content' represents the text spoken by the speaker.
- **temp** (float, optional): The temperature parameter controls the randomness of the generated text. Higher values (e.g., 1.0) make the output more random, while lower values (e.g., 0.1) make it more deterministic. Defaults to 0.33.
- **top_p** (float, optional): The top-p parameter controls the diversity of the generated text. Higher values (e.g., 0.95) allow more diverse outputs, while lower values (e.g., 0.1) make the output more focused. Defaults to 0.95.
- **top_k** (int, optional): The top-k parameter controls the number of candidate tokens considered during text generation. Higher values (e.g., 42) allow more diverse outputs, while lower values (e.g., 5) make the output more focused. Defaults to 42.
- **presence_penalty** (float, optional): The presence penalty parameter encourages the model to generate text that covers a wider range of topics. Higher values (e.g., 1.07) make the output more diverse, while lower values (e.g., 0.5) make it more focused. Defaults to 1.07.

## Returns

- **dict**: A dictionary containing the generated text and additional information.
    - **obj**: The raw response object from the together.xyz API.
    - **text**: The generated text.
    - **stop_reason**: The reason for stopping the generation process.

## Raises

- **Exception**: If the together.xyz API returns a non-200 status code.

## Note

- The 'history' argument must be a list of dictionaries, where each dictionary represents a conversation turn.
- Each dictionary should have 'role' and 'content' keys, where 'role' represents the role of the speaker and 'content' represents the text spoken by the speaker.